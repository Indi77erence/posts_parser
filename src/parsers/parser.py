import time

from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from seleniumwire import webdriver
from urllib.parse import urlparse
from src.posts.models import TaskStatus
from src.tasks_api.schemas import UrlSchema
from src.tasks_api.service import add_post_in_db, change_status, insert_views


async def parse_website(urls: UrlSchema, session):
    for url in urls.link:
        views = None
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        post_id = await add_post_in_db(url, base_url, session)

        await change_status(TaskStatus.IN_PROGRESS, post_id, session)

        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(2)
        page = driver.page_source
        soup = BeautifulSoup(page, 'html.parser')

        if base_url == "https://www.youtube.com":
            span_tag = soup.find('div', class_='style-scope ytd-watch-info-text')
            views_tag = span_tag.find('span', class_='bold style-scope yt-formatted-string')
            views = views_tag.text.split(" ")[0]

        elif base_url == "https://vk.com":
            span_tag = soup.find('div', class_='wl_post_actions_wrap clear_fix'). \
                find('div', class_="like_views like_views--inActionPanel")
            views = span_tag["title"].split(" ")[0]

        driver.close()

        if views:
            await insert_views(int(views), post_id, session)
            await change_status(TaskStatus.COMPLETED, post_id, session)
        else:
            await change_status(TaskStatus.FAILED, post_id, session)
