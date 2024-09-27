from fastapi_users.authentication import AuthenticationBackend, CookieTransport
from hrms_back.auth.dependicies import get_user_manager
from hrms_back.auth.models import User
from fastapi_users import FastAPIUsers

import uuid

from hrms_back.database.redis import get_redis_strategy

cookie_transport = CookieTransport(cookie_name="fastapiusersauth", cookie_max_age=3600)


auth_backend = AuthenticationBackend(
    name="cookie",
    transport=cookie_transport,
    get_strategy=get_redis_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)
