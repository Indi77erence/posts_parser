from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.posts.models import TaskStatus
from src.posts.schemas import GetPostByStatus
from src.posts.service import get_posts

router = APIRouter(
	tags=['Posts']
)



@router.get("/posts/{status}", response_model=list[GetPostByStatus])
async def get_posts_by_status(status: TaskStatus, session: AsyncSession = Depends(get_async_session)):
    answer = await get_posts(status, session)
    return answer
