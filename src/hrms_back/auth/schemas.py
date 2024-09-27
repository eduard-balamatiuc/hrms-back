from fastapi_users import schemas

import uuid
from enum import Enum
from typing import Optional
from pydantic import Field

from hrms_back.auth.config import PATIENT, DOCTOR, ADMIN


class UserRole(str, Enum):
    patient = PATIENT
    doctor = DOCTOR
    admin = ADMIN


class UserRead(schemas.BaseUser[uuid.UUID]):
    idnp: str = Field(max_length=50)
    name: str = Field(max_length=50)
    surname: str = Field(max_length=50)
    location: str = Field(max_length=255)
    phone: Optional[int]
    image_uri: Optional[str]
    role: UserRole
    is_active: bool
    is_superuser: bool
    is_verified: bool


class UserCreate(schemas.BaseUserCreate):
    idnp: str = Field(max_length=50)
    name: str = Field(max_length=50)
    surname: str = Field(max_length=50)
    location: str = Field(max_length=255)
    phone: Optional[int]
    image_uri: Optional[str]
    role: UserRole


class UserUpdate(schemas.BaseUserUpdate):
    idnp: Optional[str] = Field(max_length=50)
    name: Optional[str] = Field(max_length=50)
    surname: Optional[str] = Field(max_length=50)
    location: Optional[str] = Field(max_length=255)
    phone: Optional[int]
    image_uri: Optional[str]
    role: Optional[UserRole]
