import datetime

from sqlalchemy import insert, update

from src.posts.models import posts, tasks, TaskStatus


async def add_post_in_db(url, base_url, session):
    stmt = insert(posts).values(social_network=base_url, post_link=url, par_at=datetime.datetime.utcnow()).returning(posts)
    rez_query = await session.execute(stmt)
    post = rez_query.fetchone()
    await session.commit()
    await add_task_in_db(post.id, session)
    return post.id


async def add_task_in_db(id_posts, session):
    stmt = insert(tasks).values(status=TaskStatus.ASSIGNED, posts_id=id_posts).returning(tasks)
    await session.execute(stmt)
    await session.commit()


async def insert_views(views, post_id, session):
    stmt = update(posts).values(views=views).where(posts.c.id == post_id)
    await session.execute(stmt)
    await session.commit()


async def change_status(status: TaskStatus, post_id, session):
    stmt = update(tasks).values(status=status).where(tasks.c.posts_id == post_id)
    await session.execute(stmt)
    await session.commit()