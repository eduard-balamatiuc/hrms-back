import uuid
from enum import Enum

from sqlalchemy import Column, DateTime, ForeignKey, MetaData, String, Table
from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy.dialects.postgresql import UUID

from hrms_back.models.models import user

metadata = MetaData()

appointment = Table(
    "appointment",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("user_id", UUID(as_uuid=True), ForeignKey(user.c.id)),
    Column("doctor_user_id", UUID(as_uuid=True), ForeignKey(user.c.id)),
    Column("start_time", DateTime),
    Column("end_time", DateTime),
    Column("comments", String),
    Column("status", String, nullable=False),
)
