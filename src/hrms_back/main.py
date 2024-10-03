from dotenv import load_dotenv
from fastapi import FastAPI

from hrms_back.auth.auth import auth_backend, fastapi_users
from hrms_back.auth.schemas import UserCreate, UserRead
from hrms_back.routes.pacient_routes.router import router as pacient_router
from hrms_back.routes.appointment_routes.router import router as appointment_router


# Load environment variables from .env file
load_dotenv()

app = FastAPI(debug=True)

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

app.include_router(pacient_router)

app.include_router(appointment_router)
