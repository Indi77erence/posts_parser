from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey
from src.database import metadata, Base
from enum import Enum
from sqlalchemy.dialects.postgresql import ENUM as PgEnum


class TaskStatus(Enum):
    ASSIGNED = "назначена"
    IN_PROGRESS = "в работе"
    COMPLETED = "завершена"
    FAILED = "провалена"


posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("social_network", String, nullable=False),
    Column("post_link", String, nullable=False),
    Column("par_at", TIMESTAMP, default=datetime.utcnow),
    Column("views", Integer, default=0)
)


tasks = Table(
	"tasks",
	metadata,
	Column("id", Integer, primary_key=True, index=True),
	Column("posts_id", Integer, ForeignKey(posts.c.id, ondelete='CASCADE'), nullable=False),
	Column("status", PgEnum(TaskStatus, name='order_status_enum', create_type=False), nullable=False, default=TaskStatus.ASSIGNED)
)
