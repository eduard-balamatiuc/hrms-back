import uuid

from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend, CookieTransport

from hrms_back.auth.config import COOKIE, COOKIE_MAX_AGE, COOKIE_NAME
from hrms_back.auth.dependencies import get_user_manager
from hrms_back.auth.models import User
from hrms_back.database.redis import get_redis_strategy

cookie_transport = CookieTransport(cookie_name=COOKIE_NAME, cookie_max_age=COOKIE_MAX_AGE)


auth_backend = AuthenticationBackend(
    name=COOKIE,
    transport=cookie_transport,
    get_strategy=get_redis_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)
