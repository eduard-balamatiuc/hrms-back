import uuid
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from hrms_back.auth.auth import auth_backend
from hrms_back.auth.schemas import UserRead, UserCreate
from hrms_back.auth.manager import get_user_manager
from hrms_back.auth.database import User

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/session",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
