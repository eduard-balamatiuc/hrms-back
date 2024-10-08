from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from hrms_back.auth.config import PATIENT
from hrms_back.auth.utils import role_required_from_redis
from hrms_back.database.database import get_async_session
from hrms_back.models.models import general_information
from hrms_back.routes.pacient_routes.schemas import GeneralLInformationCreate

router = APIRouter(
    prefix="/general_information",
    tags=["general_information"],
)


@router.post("/", response_model=GeneralLInformationCreate, status_code=status.HTTP_201_CREATED)
async def create_general_information(
    general_info: GeneralLInformationCreate,
    db: AsyncSession = Depends(get_async_session),
    role: str = Depends(role_required_from_redis(PATIENT)),
):
    """Create general information for a patient."""
    try:
        # Ensure date_of_birth is naive (removing timezone information)
        date_of_birth_naive = (
            general_info.date_of_birth.astimezone().replace(tzinfo=None)
            if general_info.date_of_birth.tzinfo is not None
            else general_info.date_of_birth
        )

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
    except Exception:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred.")


@router.put("/{user_id}", response_model=GeneralLInformationCreate)
async def update_general_information(
    user_id: UUID,
    general_info: GeneralLInformationCreate,
    db: AsyncSession = Depends(get_async_session),
    role: str = Depends(role_required_from_redis(PATIENT)),
):
    """Update general information for a patient."""
    query = select(general_information).where(general_information.c.user_id == user_id)
    result = await db.execute(query)
    existing_info = result.fetchone()

    # Ensure date_of_birth is naive (removing timezone information)
    date_of_birth_naive = (
        general_info.date_of_birth.astimezone().replace(tzinfo=None)
        if general_info.date_of_birth.tzinfo is not None
        else general_info.date_of_birth
    )

    if not existing_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="General information not found")

    update_info = (
        general_information.update()
        .where(general_information.c.user_id == user_id)
        .values(
            height=general_info.height,
            weight=general_info.weight,
            blood_type=general_info.blood_type,
            gender=general_info.gender,
            date_of_birth=date_of_birth_naive,
        )
    )
    await db.execute(update_info)
    await db.commit()
    return general_info


@router.get("/{user_id}", response_model=GeneralLInformationCreate)
async def get_general_information(
    user_id: UUID, db: AsyncSession = Depends(get_async_session), role: str = Depends(role_required_from_redis(PATIENT))
):
    """Get general information for a patient."""
    try:
        query = select(general_information).where(general_information.c.user_id == user_id)
        result = await db.execute(query)
        general_info = result.fetchone()
        if not general_info:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="General information not found")

        return GeneralLInformationCreate(
            patient_user_id=general_info.user_id,
            height=general_info.height,
            weight=general_info.weight,
            blood_type=general_info.blood_type,
            gender=general_info.gender,
            date_of_birth=general_info.date_of_birth,
        )
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred.")
