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

        # headers
        self.headers: dict[str, Any] = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }


    def get_page(self) -> Optional[list[dict[str, Any]]]:
        params: dict[str, Any] = {
            "q": self.keyword,
            "vst": self.keyword
        }

        # headers

        url: str = f"{self.base_url}/{self.locale}/w"
        response = self.client.get(url, params=params, headers=self.headers)

        # write tmp file for checking
        self.writetmpfile(join(cfg.TEMP_DIR, 'response.html'), data=response.text)


        #  scraping process
        if response.status_code == 200:
            results: list[dict[str, Any]] = []
            soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')

            product_grid = soup.find("div", attrs={"id": "skip-to-products"})

            products = product_grid.find_all("div", attrs={"data-testid": "product-card"})
            
            for product in products:
                link: str = product.find("a", attrs={"class": "product-card__link-overlay"})['href']
                name = product.find("div", attrs={"class": "product-card__title", "role": "link"}).text.strip()
                category = product.find("div", attrs={"class": "product-card__subtitle", "role": "link"}).text.strip()
                available_color = product.find("div", attrs={"class": "product-card__product-count"}).text.strip()
                price = product.find("div", attrs={"data-testid": "product-price", "role": "link"}).text.strip()
                
                data_dict: dict[str, Any] = {
                    "product name": name,
                    "product link": link,
                    "category": category,
                    "available color": available_color,
                    "price": price
                }

                results.append(data_dict)
            
            return results

        else:
            logger.debug(f"Returned Status Code {response.status_code} writing log file")
            self.writetmpfile(join(cfg.TEMP_DIR, f"{response.status_code}.html"))
    
    def get_detail_product(self, product_url: str):
        response = self.client.get(product_url, headers=self.headers)

        self.writetmpfile(join(cfg.TEMP_DIR, 'product_detail.html'), data=response.text)

        if response.status_code == 200:
            soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')






