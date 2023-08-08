# helper for Nikespider configuration

import json

from os.path import exists, join
from os import makedirs
from loguru import logger
from typing import Union, Any

from spider.config import Config as cfg

class Formatter(object):

    def ensure_directory_exists(self, path: str):
        """function to check directory os exist or not

        Args:
            path (_type_): string path
        """
        if not exists(path):
            makedirs(path)
            logger.info(f"Directory created: {path}")
        else:
            logger.info(f"Directory already exists: {path}")

    def writetmpfile(self, file_name: str, data: Union[str, bytes]) -> None:
        """write temporary file

        Args:
            file_name (str): _description_
            data (Union[str, bytes]): _description_
        """
        with open(file_name, "wb" if isinstance(data, bytes) else "w", encoding='UTF-8') as file:
            file.write(data)
    
    def javascript_to_json(self, javascript: str) -> dict:
        text = javascript.replace('<script type="application/ld+json">', "").replace("</script>", "")
        json_data = json.loads(text)

        return json_data
    
    def remove_duplicate(self, datas: list[dict[str, Any]]) -> list[dict[str, Any]]:
        seen = set()
        output_list = []
        for item in datas:
            json_item = json.dumps(item, sort_keys=True)
            if json_item not in seen:
                seen.add(json_item)
                output_list.append(item)
        return output_list
    
    def list_to_dict(self, datas: list[dict[str, Any]]) -> dict[str, Any]:
        result_dict: dict[str, Any] = {}
        for item in datas:
            result_dict.update(item)
        return result_dict
    
    def save_url(self, datas: list[dict[str, Any]]):
        logger.info("Save URL to Local file")
        urls: list[str] = []
        for url in datas:
            if url.get("product link") is not None:
                urls.append(url['product link'])
            
        with open(join(cfg.TEMP_DIR, 'urls.json'), 'w+') as urls_file:
            json.dump(urls, urls_file)
            
        logger.info("URL Saved on {}".format(join(cfg.TEMP_DIR, 'urls.json')))

class HttpHelper(object):
    def rotator(self):
        pass