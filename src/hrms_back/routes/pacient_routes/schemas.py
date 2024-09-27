from datetime import datetime
from enum import Enum
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


class GeneralLInformation(BaseModel):
    patient_user_id: str = Field(nullable=False)
    height: int
    weight: float
    blood_type: BloodType
    gender: Gender
    date_of_birth: datetime
