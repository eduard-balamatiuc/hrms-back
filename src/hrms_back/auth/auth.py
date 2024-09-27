from fastapi_users.authentication import AuthenticationBackend, CookieTransport
from fastapi_users import FastAPIUsers

import uuid

from hrms_back.auth.config import COOKIE, COOKIE_NAME, COOKIE_MAX_AGE
from hrms_back.database.redis import get_redis_strategy
from hrms_back.auth.dependencies import get_user_manager
from hrms_back.auth.models import User

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
