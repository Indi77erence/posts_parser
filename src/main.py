from fastapi import FastAPI

from src.auth.config import auth_backend, fastapi_users
from src.auth.schemas import UserRead, UserCreate
from src.tasks_api.router import router as tasks_router
from src.posts.router import router as posts_router
app = FastAPI(title='Posts_parser')


def create_app():
	app.include_router(
		fastapi_users.get_register_router(UserRead, UserCreate),
		prefix="/auth",
		tags=["auth"],
	)
	app.include_router(
		fastapi_users.get_auth_router(auth_backend),
		prefix="/api/v1/auth",
		tags=["auth"])

	app.include_router(tasks_router)
	app.include_router(posts_router)
	return app
