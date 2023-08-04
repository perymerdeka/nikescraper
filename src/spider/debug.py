# Nike Scraper for debug mode
from os.path import join
from bs4 import BeautifulSoup
from typing import Any

from spider.config import Config as cfg
from spider.helper import Formatter


class NikeSpiderDebug(Formatter):
    def get_from_page(self) -> list[dict[str, Any]]:
        results: list[dict[str, Any]] = []
        with open(join(cfg.TEMP_DIR, "response.html"), "r+", encoding="UTF-8") as files:
            source: str = files.read()

            #  scraping process
            soup: BeautifulSoup = BeautifulSoup(source, "html.parser")

            product_grid = soup.find("div", attrs={"id": "skip-to-products"})

            products = product_grid.find_all(
                "div", attrs={"data-testid": "product-card"}
            )

            for product in products:
                link: str = product.find(
                    "a", attrs={"class": "product-card__link-overlay"}
                )["href"]
                name = product.find(
                    "div", attrs={"class": "product-card__title", "role": "link"}
                ).text.strip()
                category = product.find(
                    "div", attrs={"class": "product-card__subtitle", "role": "link"}
                ).text.strip()
                available_color = product.find(
                    "div", attrs={"class": "product-card__product-count"}
                ).text.strip()
                price = product.find(
                    "div", attrs={"data-testid": "product-price", "role": "link"}
                ).text.strip()

                data_dict: dict[str, Any] = {
                    "product name": name,
                    "product link": link,
                    "category": category,
                    "available color": available_color,
                    "price": price,
                }

                results.append(data_dict)

            return results

    def get_product_detail(self):
        with open(
            join(cfg.TEMP_DIR, "product_detail.html"), "r+", encoding="UTF-8"
        ) as files:
            source: str = files.read()

            # data_dict: dict[str, Any] = {}
            #  scraping process
            soup: BeautifulSoup = BeautifulSoup(source, "html.parser")
            container = soup.find("div", attrs={"class": "app-root"})

            # get items form json
            json_script = soup.find("script", attrs={"type": "application/ld+json"})
            datas = self.javascript_to_json(json_script.text.strip())

            # extract data
            results: list[dict[str, Any]] = []
            for _ in datas.items():
                # print("Ini Key: ", key, "Ini Value: ", value)

                name = datas["name"]
                brand = datas["brand"]["name"]
                price = datas["offers"]["price"]
                seller = datas["offers"]["seller"]["name"]
                sku = datas["sku"]
                image = datas["image"]
                release = datas["releaseDate"]

                # formatting
                data_dict: dict[str, Any] = {
                    "name": name,
                    "brand": brand,
                    "price": price,
                    "seller": seller,
                    "sku": sku,
                    "image": image,
                    "release": release,
                }
                # append data
                results.append(data_dict)

            # process the data
            results = self.remove_duplicate(datas=results)
            return self.list_to_dict(results)
