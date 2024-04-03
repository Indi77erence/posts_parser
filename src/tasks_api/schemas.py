from pydantic import BaseModel


class UrlSchema(BaseModel):
    link: list[str]


class AnswerCreateTask(BaseModel):
    detail: str
