import uuid

from sqlalchemy import Column, DateTime, ForeignKey, Integer, MetaData, String, Table
from sqlalchemy.dialects.postgresql import UUID

from hrms_back.models.models import user

metadata = MetaData()

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
