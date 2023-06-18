from typing import Optional, Any
from httpx import Client
from bs4 import BeautifulSoup
from os.path import join
from loguru import logger

from spider.config import Config as cfg
from spider.helper import FileHelper

class NikeSpider(FileHelper):
    def __init__(self, keyword: str,  locale: Optional[str]="id") -> None:
        self.base_url: str = "https://www.nike.com"
        self.locale = locale
        self.keyword = keyword
        self.client = Client()

        # check log and temp dir
        self.ensure_directory_exists(cfg.LOGDIR)
        self.ensure_directory_exists(cfg.TEMP_DIR)


    def get_page(self):
        params: dict[str, Any] = {
            "q": self.keyword,
            "vst": self.keyword
        }

        # headers
        headers: dict[str, Any] = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }

        url: str = f"{self.base_url}/{self.locale}/w"
        response = self.client.get(url, params=params, headers=headers)

        # write tmp file for checking
        self.writetmpfile(join(cfg.TEMP_DIR, 'response.html'), data=response.text)


        #  scraping process
        if response.status_code == 200:
            soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')

            

        else:
            logger.debug(f"Returned Status Code {response.status_code} writing log file")
            self.writetmpfile(join(cfg.TEMP_DIR, f"{response.status_code}.html"))
            


