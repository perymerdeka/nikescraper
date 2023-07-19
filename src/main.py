from spider.nike import NikeSpider


if __name__ == "__main__":
    spider: NikeSpider = NikeSpider(search_query="jordan")
    print(spider.get_pages())