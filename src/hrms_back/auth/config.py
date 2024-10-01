from hrms_back.config import get_env_or_raise

SECRET_KEY = get_env_or_raise("SECRET_KEY")

COOKIE = get_env_or_raise("COOKIE")
COOKIE_NAME = get_env_or_raise("COOKIE_NAME")
COOKIE_MAX_AGE = get_env_or_raise("COOKIE_MAX_AGE")

PATIENT = get_env_or_raise("PATIENT")
DOCTOR = get_env_or_raise("DOCTOR")
ADMIN = get_env_or_raise("ADMIN")
