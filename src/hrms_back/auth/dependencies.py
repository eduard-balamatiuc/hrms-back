from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from hrms_back.auth.manager import UserManager
from hrms_back.auth.models import User
from hrms_back.database.database import get_async_session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    """Get the user database."""
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(user_db=Depends(get_user_db)):
    """Get the user manager."""
    yield UserManager(user_db)
