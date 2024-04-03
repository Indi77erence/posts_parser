import datetime

from pydantic import BaseModel

from src.posts.models import TaskStatus


class PostSchema(BaseModel):
    id: int
    social_network: str
    post_link: str
    par_at: datetime.datetime
    views: int


class GetPostByStatus(BaseModel):
    id: int
    social_network: str
    post_link: str
    status: TaskStatus


class GetPostByStatusViews(GetPostByStatus):
    views: int


