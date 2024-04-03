# Роутер для управления задачами
from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.config import current_user
from src.database import get_async_session
from src.parsers.parser import parse_website
from src.tasks_api.schemas import UrlSchema, AnswerCreateTask

router = APIRouter(
	tags=['Tasks']
)



@router.post("/create_task", response_model=AnswerCreateTask)
async def create_parser_task(urls: UrlSchema, background_tasks: BackgroundTasks, user=Depends(current_user),
							 session: AsyncSession = Depends(get_async_session)):
	background_tasks.add_task(parse_website, urls, session)
	return AnswerCreateTask(detail="Задача создана")
