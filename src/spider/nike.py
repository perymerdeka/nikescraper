from typing import Any
from httpx import Client
from bs4 import BeautifulSoup

from spider.helper import FileHelper

class NikeSpider(FileHelper):
    def __init__(self, search_query) -> None:
        self.search_query = search_query
        self.base_url: str = "https://www.nike.com/id/"
        self.client: Client = Client()
        self.user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

    def get_pages(self):
        params: dict[str, Any] = {
            "q": self.search_query,
            "vst": self.search_query
        }

        headers: dict[str, Any] = self.user_agent
        print(headers)
        

        # request ke website
        response = self.client.get(self.base_url, params=params, headers=headers)

        # save hasil response ke html agar bisa debugging
        self.writetmpfile(file_name="response.html", data=response.text)

        

        # proses parsing
        soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
        print(soup.prettify())