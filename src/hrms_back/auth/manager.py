import uuid
from typing import Optional, Any

from fastapi import Request
from fastapi_users import BaseUserManager, UUIDIDMixin, exceptions, models, schemas

from hrms_back.auth.models import User
from hrms_back.auth.config import SECRET_KEY, PATIENT


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET_KEY
    verification_token_secret = SECRET_KEY

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        """Send a welcome message after registration."""
        print(f"User {user.id} has registered.")

    async def create(
        self,
        user_create: schemas.UC,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> models.UP:
        """Create a user."""
        await self.validate_password(user_create.password, user_create)

        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = user_create.create_update_dict() if safe else user_create.create_update_dict_superuser()
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)
        user_dict["role"] = PATIENT
        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user

    async def on_after_forgot_password(self, user: User, token: str, request: Optional[Request] = None):
        """Send a forgot password message."""
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(self, user: User, token: str, request: Optional[Request] = None):
        """Send a verification message."""
        print(f"Verification requested for user {user.id}. Verification token: {token}")

    async def parse_id(self, value: Any) -> uuid.UUID:
        """Parse the ID."""
        return uuid.UUID(str(value))
