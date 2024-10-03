from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

from hrms_back.auth.config import PATIENT, DOCTOR, ADMIN


class UserRole(str, Enum):
    PATIENT = PATIENT
    DOCTOR = DOCTOR
    ADMIN = ADMIN


class Status(str, Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"


class User(BaseModel):
    idnp: str = Field(nullable=False, unique=True, min_length=13, max_length=50)
    email: str = Field(nullable=False, max_length=50)
    hashed_password: str = Field(nullable=False, max_length=255)
    name: str = Field(nullable=False, max_length=50)
    surname: str = Field(nullable=False, max_length=50)
    location: str = Field(nullable=False, max_length=255)
    phone: int
    image_uri: Optional[str] = None
    role: UserRole


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


class Appointment(BaseModel):
    patient_user_id: str = Field(nullable=False)
    doctor_user_id: str = Field(nullable=False)
    start_time: datetime
    end_time: Optional[datetime] = None
    comments: str = Field(nullable=False)
    status: Status
