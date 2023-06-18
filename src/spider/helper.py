# helper for Nikespider configuration

from os.path import exists
from os import makedirs
from loguru import logger
from typing import Union

class FileHelper(object):

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
        with open(file_name, "wb" if isinstance(data, bytes) else "w") as file:
            file.write(data)

class HttpHelper(object):
    def rotator(self):
        pass