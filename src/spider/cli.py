from typer import Typer, Option
from typing import Optional


from spider.nike import NikeSpider
from spider.debug import NikeSpiderDebug

app: Typer = Typer()

@app.command(name="pages", help="generate pages data from nike")
def get_pages(debug: Optional[bool]=Option(False, help="if this option is true, then debug activated"), keyword: Optional[str]=""):
    if debug:
        spider_debug: NikeSpiderDebug = NikeSpiderDebug()
        spider_debug.get_from_page()
    else:
        spider: NikeSpider = NikeSpider(keyword=keyword)
        spider.get_page()
