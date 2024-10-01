import os

from dotenv import load_dotenv

load_dotenv()


def get_env_or_raise(key: str) -> str:
    """Get an environment variable or raise an exception."""
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"Environment variable {key} is not set")
    return value


POSTGRES_HOST = get_env_or_raise("POSTGRES_HOST")
POSTGRES_PORT = get_env_or_raise("POSTGRES_PORT")
POSTGRES_USER = get_env_or_raise("POSTGRES_USER")
POSTGRES_PASSWORD = get_env_or_raise("POSTGRES_PASSWORD")
POSTGRES_DB = get_env_or_raise("POSTGRES_DB")

MONGO_INITDB_DATABASE = get_env_or_raise("MONGO_INITDB_DATABASE")

REDIS_HOST = get_env_or_raise("REDIS_HOST")
REDIS_PORT = get_env_or_raise("REDIS_PORT")

KEY_PREFIX_REDIS_STRATEGY = get_env_or_raise("KEY_PREFIX_REDIS_STRATEGY")
USER_ID_REDIS_STRATEGY = get_env_or_raise("USER_ID_REDIS_STRATEGY")
ROLE_REDIS_STRATEGY = get_env_or_raise("ROLE_REDIS_STRATEGY")
