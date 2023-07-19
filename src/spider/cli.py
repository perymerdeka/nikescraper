from typer import Typer, Option, prompt
from typing import Optional


from spider.nike import NikeSpider
from spider.debug import NikeSpiderDebug

app: Typer = Typer()


@app.command(name="pages", help="generate pages data from nike")
def get_pages(
    debug: Optional[bool] = Option(
        False, help="if this option is true, then debug activated"
    )
):
    if debug:
        spider_debug: NikeSpiderDebug = NikeSpiderDebug()
        spider_debug.get_from_page()
    else:
        keyword: str = prompt("Search Product")
        spider: NikeSpider = NikeSpider(keyword=keyword)
        spider.get_page()


@app.command(name="get-product", help="Get Spesific product from Nike.com")
def get_product_detail(
    debug: Optional[bool] = Option(
        False, help="if this option is true, then debug activated"
    ),
    url: Optional[str] = Option("", help="Product URL for Nike Website"),
):
    if debug:
        spider_debug: NikeSpiderDebug = NikeSpiderDebug()
        spider_debug.get_product_detail()
    else:
        spider: NikeSpider = NikeSpider(keyword="")
        spider.get_detail_product(product_url=url)
