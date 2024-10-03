from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from hrms_back.auth.config import PATIENT, DOCTOR, ADMIN
from hrms_back.auth.utils import role_required_from_redis
from hrms_back.database.database import get_async_session
from hrms_back.routes.appointment_routes.models import appointment
from hrms_back.routes.appointment_routes.schemas import AppointmentCreate, AppointmentUpdate

router = APIRouter(
    prefix="/appointment",
    tags=["appointment"],
)


# This is the endpoint that will be used to create a new appointment available for patient, doctor, admin
@router.post("/", response_model=AppointmentCreate, status_code=status.HTTP_201_CREATED)
async def create_appointment(
    new_appointment: AppointmentCreate,
    db: AsyncSession = Depends(get_async_session),
    role: str = Depends(role_required_from_redis([PATIENT, DOCTOR, ADMIN])),
):
    """Create a new appointment."""
    try:
        # Ensure start_time is naive (removing timezone information)
        start_time_naive = (
            new_appointment.start_time.astimezone().replace(tzinfo=None)
            if new_appointment.start_time.tzinfo is not None
            else new_appointment.start_time
        )
        # Ensure end_time is naive (removing timezone information)
        end_time_naive = (
            new_appointment.end_time.astimezone().replace(tzinfo=None)
            if new_appointment.end_time.tzinfo is not None
            else new_appointment.end_time
        )
        new_info = appointment.insert().values(
            user_id=new_appointment.user_id,
            doctor_user_id=new_appointment.doctor_user_id,
            start_time=start_time_naive,
            end_time=end_time_naive,
            comments=new_appointment.comments,
            status=new_appointment.status,
        )

        await db.execute(new_info)
        await db.commit()
        return new_appointment
    except Exception:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred.")


# This is the endpoint that will be used to UPDATE STATUS an appointment available for patient, doctor, admin
@router.put("/{appointment_id}", response_model=AppointmentCreate, status_code=status.HTTP_200_OK)
async def update_appointment(
        appointment_id: UUID,
        appointment_info: AppointmentUpdate,
        db: AsyncSession = Depends(get_async_session),
        role: str = Depends(role_required_from_redis([PATIENT, DOCTOR, ADMIN])),
):
    """Update an appointment."""
    query = select(appointment).where(appointment.c.id == appointment_id)
    result = await db.execute(query)
    existing_appointment = result.fetchone()

    if not existing_appointment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")

    try:
        update_data = appointment_info.dict(exclude_unset=True)

        # Handle timezone information for start_time and end_time if they're provided
        if 'start_time' in update_data and update_data['start_time']:
            update_data['start_time'] = update_data['start_time'].astimezone().replace(tzinfo=None)
        if 'end_time' in update_data and update_data['end_time']:
            update_data['end_time'] = update_data['end_time'].astimezone().replace(tzinfo=None)

        update_query = appointment.update().where(appointment.c.id == appointment_id).values(**update_data)
        await db.execute(update_query)
        await db.commit()

        updated_appointment = await db.execute(select(appointment).where(appointment.c.id == appointment_id))
        return updated_appointment.fetchone()
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"An error occurred: {str(e)}")


# This is the endpoint that will be used to DELETE an appointment available for patient, doctor, admin
@router.delete("/{appointment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_appointment(
    appointment_id: UUID,
    db: AsyncSession = Depends(get_async_session),
    role: str = Depends(role_required_from_redis([PATIENT, DOCTOR, ADMIN])),
):
    """Delete an appointment."""
    query = select(appointment).where(appointment.c.id == appointment_id)
    result = await db.execute(query)
    existing_appointment = result.fetchone()

    if not existing_appointment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")

    try:
        delete_appointment = appointment.delete().where(appointment.c.id == appointment_id)

        await db.execute(delete_appointment)
        await db.commit()
    except Exception:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred.")


# This is the endpoint that will be used to GET all appointments of a DOCTOR,from a starting date available for doctor
@router.get("/doctor/{doctor_id}/{start_date}/{status_required}", response_model=List[AppointmentCreate], status_code=status.HTTP_200_OK)
async def get_doctor_appointments(
        doctor_id: UUID,
        start_date: Optional[str] = None,
        status_required: Optional[str] = None,
        db: AsyncSession = Depends(get_async_session),
        role: str = Depends(role_required_from_redis(DOCTOR)),
):
    """Get all appointments of a doctor, optionally filtered by a starting date and status."""
    query = select(appointment).where(appointment.c.doctor_user_id == doctor_id)

    if start_date:
        query = query.where(appointment.c.start_time >= start_date)

    if status_required:
        query = query.where(appointment.c.status == status_required)

    result = await db.execute(query)
    appointments = result.fetchall()

    return appointments


# This is the endpoint that will be used to GET all appointments of a PATIENT,from a starting date available for doctor
@router.get("/patient/{patient_id}/{start_date}/{status_required}", response_model=List[AppointmentCreate], status_code=status.HTTP_200_OK)
async def get_patient_appointments(
        patient_id: UUID,
        start_date: Optional[str] = None,
        status_required: Optional[str] = None,
        db: AsyncSession = Depends(get_async_session),
        role: str = Depends(role_required_from_redis(DOCTOR)),
):
    """Get all appointments of a patient, optionally filtered by a starting date and status."""
    query = select(appointment).where(appointment.c.patient_user_id == patient_id)

    if start_date:
        query = query.where(appointment.c.start_time >= start_date)

    if status_required:
        query = query.where(appointment.c.status == status_required)

    result = await db.execute(query)
    appointments = result.fetchall()

    return appointments
