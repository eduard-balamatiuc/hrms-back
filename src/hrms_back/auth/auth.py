import redis.asyncio
from fastapi_users.authentication import AuthenticationBackend, CookieTransport, RedisStrategy
from hrms_back.auth.manager import get_user_manager
from hrms_back.auth.models import User
from fastapi_users import FastAPIUsers
import uuid

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
"""
class CookieTransport(Transport):
    scheme: APIKeyCookie

    def __init__(
        self,
        cookie_name: str = "fastapiusersauth",
        cookie_max_age: Optional[int] = None,
        cookie_path: str = "/",
        cookie_domain: Optional[str] = None,
        cookie_secure: bool = True,
        cookie_httponly: bool = True,
        cookie_samesite: Literal["lax", "strict", "none"] = "lax",
    ):
        self.cookie_name = cookie_name
        self.cookie_max_age = cookie_max_age  #seconds
        self.cookie_path = cookie_path
        self.cookie_domain = cookie_domain
        self.cookie_secure = cookie_secure
        self.cookie_httponly = cookie_httponly
        self.cookie_samesite = cookie_samesite
        self.scheme = APIKeyCookie(name=self.cookie_name, auto_error=False)
"""
