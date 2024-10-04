from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class BloodType(str, Enum):
    A_POSITIVE = "A+"
    A_NEGATIVE = "A-"
    B_POSITIVE = "B+"
    B_NEGATIVE = "B-"
    AB_POSITIVE = "AB+"
    AB_NEGATIVE = "AB-"
    O_POSITIVE = "O+"
    O_NEGATIVE = "O-"


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class GeneralLInformationCreate(BaseModel):
    user_id: UUID = Field(nullable=False)
    height: int
    weight: float
    blood_type: BloodType
    gender: Gender
    date_of_birth: datetime


class GeneralLInformationUpdate(BaseModel):
    user_id: Optional[UUID] = None
    height: Optional[int] = None
    weight: Optional[float] = None
    blood_type: Optional[BloodType] = None
    gender: Optional[Gender] = None
    date_of_birth: Optional[datetime] = None
