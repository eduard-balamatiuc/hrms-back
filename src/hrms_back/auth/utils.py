from fastapi import Depends, HTTPException, Request
from fastapi_users.manager import BaseUserManager

from hrms_back.database.redis import get_redis_strategy
from hrms_back.auth.dependicies import get_user_manager


async def get_role_from_redis(token: str, user_manager: BaseUserManager) -> str:
    try:
        redis_strategy = get_redis_strategy()
        user_data = await redis_strategy.read_token(token, user_manager)
        return user_data.get("role")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


def role_required_from_redis(required_role: str):
    async def role_checker(request: Request, user_manager=Depends(get_user_manager)):
        token = request.cookies.get("fastapiusersauth")
        if not token:
            raise HTTPException(status_code=401, detail="Token not found")

        try:
            role = await get_role_from_redis(token, user_manager)
        except HTTPException as e:
            raise e
        except Exception:
            raise HTTPException(status_code=500, detail="Internal server error")

        if role != required_role:
            raise HTTPException(status_code=403, detail="Not authorized")
        return role

    return role_checker
