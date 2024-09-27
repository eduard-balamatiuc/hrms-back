# RESTAPI for Pacient routes

# Routes for inserting, updating, getting general_information of a pacient

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from hrms_back.models.models import general_information
from hrms_back.models.schemas import GeneralLInformation
from hrms_back.database import get_async_session
from uuid import UUID

router = APIRouter(
    prefix="/general_information",
    tags=["general_information"],
)

# Root endpoint that does nothing
@router.post("/")
async def create_general_information():
    return


# Insert new general information for a patient
@router.post("/general_information", response_model=GeneralLInformation, status_code=status.HTTP_201_CREATED)
async def create_general_information(
    general_info: GeneralLInformation, db: AsyncSession = Depends(get_async_session)
):
    # Ensure date_of_birth is naive (remove timezone information)
    if general_info.date_of_birth.tzinfo is not None:
        date_of_birth_naive = general_info.date_of_birth.astimezone().replace(tzinfo=None)
    else:
        date_of_birth_naive = general_info.date_of_birth

    new_info = general_information.insert().values(
        user_id=general_info.patient_user_id,
        height=general_info.height,
        weight=general_info.weight,
        blood_type=general_info.blood_type,
        gender=general_info.gender,
        date_of_birth=date_of_birth_naive,
    )
    await db.execute(new_info)
    await db.commit()
    return general_info

# Update existing general information for a patient
@router.put("/general_information/{user_id}", response_model=GeneralLInformation)
async def update_general_information(
    user_id: UUID, general_info: GeneralLInformation, db: AsyncSession = Depends(get_async_session)
):
    query = select(general_information).where(general_information.c.user_id == user_id)
    result = await db.execute(query)
    existing_info = result.scalar()

    if not existing_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="General information not found")

    update_info = general_information.update().where(general_information.c.user_id == user_id).values(
        height=general_info.height,
        weight=general_info.weight,
        blood_type=general_info.blood_type,
        gender=general_info.gender,
        date_of_birth=general_info.date_of_birth,
    )
    await db.execute(update_info)
    await db.commit()
    return general_info


# Get general information for a patient
@router.get("/general_information/{user_id}", response_model=GeneralLInformation)
async def get_general_information(user_id: UUID, db: AsyncSession = Depends(get_async_session)):
    query = select(general_information).where(general_information.c.user_id == user_id)
    result = await db.execute(query)
    general_info = result.scalar_one_or_none()  # Use scalar_one_or_none for clearer intent

    if not general_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="General information not found")

    # Assuming general_info is a row proxy, convert it to a dictionary
    return GeneralLInformation(
        patient_user_id=general_info.user_id,
        height=general_info.height,
        weight=general_info.weight,
        blood_type=general_info.blood_type,
        gender=general_info.gender,
        date_of_birth=general_info.date_of_birth,
    )
