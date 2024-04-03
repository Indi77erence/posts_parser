from typing import Optional

from fastapi_users import schemas


class UserCreate(schemas.BaseUserCreate):
	username: str
	email: str
	password: str
	is_active: Optional[bool] = True
	is_superuser: Optional[bool] = False
	is_verified: Optional[bool] = False


class UserRead(schemas.BaseUser[int]):
	id: int | None
	email: str | None
	username: str | None
	is_active: bool = True
	is_superuser: bool = False
	is_verified: bool = False
