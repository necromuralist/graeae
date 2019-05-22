# python
from pathlib import Path

# pypi
import requests

# this project
from graeae import SysLogBase


class TextDownloader(SysLogBase):
    """Downloads a text file if it doesn't exist

    Args:
     url: where to download the file from
     target: path to output the file to
    """
    def __init__(self, url: str, target: Path) -> None:
        super().__init__()
        self.url = url
        self.target = target
        self._directory_path = None
        self._download = None
        return
    
    @property
    def directory_path(self) -> Path:
        """The directory portion
        
        This will attempt to make the directory if it doesn't exist
        """
        if self._directory_path is None:
            self._directory_path = self.target.parent
            if not self._directory_path.is_dir():
                self._directory_path.mkdir()
        return self._directory_path
    
    @property
    def download(self):
        """The text string

        downloads and saves the file if it doesn't exist        
        """
        if self._download is None:
            if self.target.is_file():
                self.log.info(f"{self.target} exists, opening it")
                self._download = self.target.open().read()
            else:
                self.log.info(f"Pulling file from {self.url}")
                response = requests.get(self.url)
                self._download = response.text
                assert self.directory_path.is_dir()
                with self.target.open("w") as writer:
                    writer.write(self._download)
        return self._download
