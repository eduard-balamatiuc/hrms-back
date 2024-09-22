import uuid
from enum import Enum

from sqlalchemy import Boolean, Column, DateTime
from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy import ForeignKey, Integer, MetaData, String, Table
from sqlalchemy.dialects.postgresql import UUID

metadata = MetaData()


class UserRole(str, Enum):
    patient = "patient"
    doctor = "doctor"
    admin = "admin"


user = Table(
    "user",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("idnp", String(50), nullable=False),
    Column("email", String(50), nullable=False),
    Column("hashed_password", String(255), nullable=False),
    Column("name", String(50), nullable=False),
    Column("surname", String(50), nullable=False),
    Column("location", String(255), nullable=False),
    Column("phone", Integer),
    Column("image_uri", String(255)),
    Column("role", SQLAlchemyEnum(UserRole), nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=True, nullable=False),
    Column("is_verified", Boolean, default=True, nullable=False),
)

general_information = Table(
    "general_information",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("user_id", UUID(as_uuid=True), ForeignKey(user.c.id)),
    Column("height", Integer),
    Column("weight", Integer),
    Column("blood_type", String),
    Column("gender", String),
    Column("date_of_birth", DateTime),
)

appointment = Table(
    "appointment",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("user_id", UUID(as_uuid=True), ForeignKey(user.c.id)),
    Column("doctor_user_id", UUID(as_uuid=True), ForeignKey(user.c.id)),
    Column("start_time", DateTime),
    Column("end_time", DateTime),
    Column("comments", String),
)
