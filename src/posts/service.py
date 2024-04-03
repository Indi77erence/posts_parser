from sqlalchemy import select, join

from src.posts.models import posts, tasks
from src.posts.schemas import PostSchema, GetPostByStatus, GetPostByStatusViews


async def get_posts(status, session):
    stmt = select(posts.c.id, posts.c.social_network, posts.c.post_link, tasks.c.status, posts.c.views).select_from(join(posts, tasks)).where(
        tasks.c.status == status)
    result = await session.execute(stmt)
    posts_with_status = result.fetchall()
    if status.value == "успешно":
        answer = [GetPostByStatusViews(id=post.id, social_network=post.social_network, post_link=post.post_link, status=post.status, views=post.views) for post in posts_with_status]
        return answer
    answer = [GetPostByStatus(id=post.id, social_network=post.social_network, post_link=post.post_link, status=post.status)
        for post in posts_with_status]
    return answer
