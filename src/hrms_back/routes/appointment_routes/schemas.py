from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class Status(str, Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"


class Appointment(BaseModel):
    user_id: str = Field(nullable=False)
    doctor_user_id: str = Field(nullable=False)
    start_time: datetime
    end_time: Optional[datetime] = None
    comments: str = Field(nullable=False)
    status: Status


class AppointmentCreate(BaseModel):
    user_id: UUID = Field(nullable=False)
    doctor_user_id: UUID = Field(nullable=False)
    start_time: datetime
    end_time: Optional[datetime] = None
    comments: str = Field(nullable=False)
    status: Status = Status.pending
