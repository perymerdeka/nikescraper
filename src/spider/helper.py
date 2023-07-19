from typing import Union

class FileHelper(object):
    def writetmpfile(self, file_name: str, data: Union[str, bytes]) -> None:
        """write temporary file

        Args:
            file_name (str): _description_
            data (Union[str, bytes]): _description_
        """
        with open(file_name, "wb" if isinstance(data, bytes) else "w", encoding='UTF-8') as file:
            file.write(data)