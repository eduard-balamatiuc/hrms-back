from fastapi import Depends, HTTPException, Request
from fastapi_users.manager import BaseUserManager

from hrms_back.auth.config import COOKIE_NAME
from hrms_back.auth.dependencies import get_user_manager
from hrms_back.config import ROLE_REDIS_STRATEGY
from hrms_back.database.redis import get_redis_strategy


async def get_role_from_redis(token: str, user_manager: BaseUserManager) -> str:
    """Get the role of the user from Redis."""
    try:
        redis_strategy = get_redis_strategy()
        user_data = await redis_strategy.read_token(token, user_manager)
        return user_data.get(ROLE_REDIS_STRATEGY)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


def role_required_from_redis(required_role: str or list[str]):
    """Check if the user has the required role."""

    async def role_checker(request: Request, user_manager=Depends(get_user_manager)):
        token = request.cookies.get(COOKIE_NAME)
        if not token:
            raise HTTPException(status_code=401, detail="Token not found")

        try:
            role = await get_role_from_redis(token, user_manager)
        except HTTPException as e:
            raise e
        except Exception:
            raise HTTPException(status_code=500, detail="Internal server error")

        if isinstance(required_role, list):
            if role not in required_role:
                raise HTTPException(status_code=403, detail="Not authorized")
        else:
            if role != required_role:
                raise HTTPException(status_code=403, detail="Not authorized")

        if role in required_role or role == required_role:
            print(role, "lalalalalalalalalalla")

    return role_checker
