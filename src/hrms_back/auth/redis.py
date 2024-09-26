import secrets
from typing import Generic, Optional

import redis.asyncio

from fastapi_users import exceptions, models
from fastapi_users.authentication.strategy.base import Strategy
from fastapi_users.manager import BaseUserManager
import json


class RedisStrategy(Strategy[models.UP, models.ID], Generic[models.UP, models.ID]):
    def __init__(
        self,
        redis: redis.asyncio.Redis,
        lifetime_seconds: Optional[int] = None,
        *,
        key_prefix: str = "fastapi_users_token:",
    ):
        self.redis = redis
        self.lifetime_seconds = lifetime_seconds
        self.key_prefix = key_prefix

    async def read_token(
            self, token: Optional[str], user_manager: BaseUserManager[models.UP, models.ID]
    ) -> Optional[models.UP]:
        if token is None:
            return None

        user_data_json = await self.redis.get(f"{self.key_prefix}{token}")
        if user_data_json is None:
            return None

        try:
            user_data = json.loads(user_data_json)
            parsed_id = user_manager.parse_id(user_data["user_id"])

            # You can access the role from user_data["role"] if needed
            # role = user_data["role"]

            return await user_manager.get(parsed_id)
        except (exceptions.UserNotExists, exceptions.InvalidID):
            return None

    async def write_token(self, user: models.UP) -> str:
        token = secrets.token_urlsafe()
        user_data = {
            "user_id": str(user.id),
            "role": user.role,
        }
        await self.redis.set(
            f"{self.key_prefix}{token}", json.dumps(user_data), ex=self.lifetime_seconds
        )
        return token

    async def destroy_token(self, token: str, user: models.UP) -> None:
        await self.redis.delete(f"{self.key_prefix}{token}")
