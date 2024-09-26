import redis.asyncio
from fastapi_users.authentication import AuthenticationBackend, CookieTransport
from hrms_back.auth.manager import get_user_manager
from hrms_back.auth.models import User
from fastapi_users import FastAPIUsers
import uuid

from hrms_back.auth.redis import RedisStrategy

cookie_transport = CookieTransport(cookie_max_age=3600)
redis = redis.asyncio.from_url("redis://redis:6379", decode_responses=True)


def get_redis_strategy() -> RedisStrategy:
    """Return a RedisStrategy instance."""
    return RedisStrategy(redis, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="cookie",
    transport=cookie_transport,
    get_strategy=get_redis_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)
