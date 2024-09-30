from fastapi_users import exceptions, models
from fastapi_users.authentication.strategy.base import Strategy
from fastapi_users.manager import BaseUserManager

from typing import Generic, Optional
import secrets
import redis.asyncio as redis
import json

from hrms_back.config import (
    REDIS_HOST,
    REDIS_PORT,
    KEY_PREFIX_REDIS_STRATEGY,
    USER_ID_REDIS_STRATEGY,
    ROLE_REDIS_STRATEGY,
)


redis_async_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


class RedisStrategy(Strategy[models.UP, models.ID], Generic[models.UP, models.ID]):
    def __init__(
        self,
        redis: redis.Redis,
        lifetime_seconds: Optional[int] = None,
        *,
        key_prefix: str = KEY_PREFIX_REDIS_STRATEGY,
    ):
        """Create a Redis strategy instance."""
        self.redis = redis
        self.lifetime_seconds = lifetime_seconds
        self.key_prefix = key_prefix

    async def read_token(
        self, token: Optional[str], user_manager: BaseUserManager[models.UP, models.ID]
    ) -> Optional[models.UP]:
        """Read the token from the database and return the user associated with it."""
        if token is None:
            return None

        user_data_json = await self.redis.get(f"{self.key_prefix}{token}")
        if user_data_json is None:
            return None

        try:
            user_data = json.loads(user_data_json)
            parsed_id = await user_manager.parse_id(user_data[USER_ID_REDIS_STRATEGY])
            user = await user_manager.get(parsed_id)
            if user is None:
                raise exceptions.UserNotExists()

            return user_data
        except (json.JSONDecodeError, exceptions.UserNotExists):
            return None

    async def write_token(self, user: models.UP) -> str:
        """Write the token to the database and return it."""
        token = secrets.token_urlsafe()
        user_data = {
            USER_ID_REDIS_STRATEGY: str(user.id),
            ROLE_REDIS_STRATEGY: user.role,
        }
        await self.redis.set(f"{self.key_prefix}{token}", json.dumps(user_data), ex=self.lifetime_seconds)
        return token

    async def destroy_token(self, token: str, user: models.UP) -> None:
        """Destroy the token."""
        await self.redis.delete(f"{self.key_prefix}{token}")


def get_redis_strategy() -> RedisStrategy:
    return RedisStrategy(redis=redis_async_client, lifetime_seconds=3600)
