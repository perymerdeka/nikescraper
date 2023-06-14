from typing import Optional, Any
from httpx import Client
from bs4 import BeautifulSoup

class NikeSpider(object):
    def __init__(self, keyword: str,  locale: Optional[str]="id") -> None:
        self.base_url: str = "https://www.nike.com"
        self.locale = locale
        self.keyword = keyword
        self.client = Client()

    def get_page(self):
        params: dict[str, Any] = {
            "q": self.keyword,
            "vst": self.keyword
        }
        url: str = f"{self.base_url}/{self.locale}/w"
        res = self.client.get(url, params=params)

        #  scraping process

