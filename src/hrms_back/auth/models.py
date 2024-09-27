from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import BigInteger, Boolean, Column, String
from hrms_back.database.database import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    idnp: str = Column(String, nullable=False, unique=True)
    email: str = Column(String, unique=True, index=True, nullable=False)
    hashed_password: str = Column(String, nullable=False)
    name: str = Column(String, nullable=False)
    surname: str = Column(String, nullable=False)
    location: str = Column(String, nullable=False)
    phone: BigInteger = Column(BigInteger, nullable=True)
    image_uri: str = Column(String, nullable=True)
    role: str = Column(String, nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
