# python
from pathlib import Path
import tempfile
import zipfile

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


class ZipDownloader(SysLogBase):
    """Downloads a zip file and unpacks it

    Args:
     url: URL to the zip file
     target: directory to unzip the contents into
     verbose: whether to emit statements
    """
    def __init__(self, url: str, target: str, verbose: bool=True):
        super().__init__()
        self.url = url
        self.target = Path(target).expanduser()
        self.verbose = verbose
        return
    
    def download(self) -> None:
        if not self.target.is_dir():
            if self.verbose:
                self.timer.message = "Finished Downloading and unzipping"
                self.timer.start()
                self.log.info("Downloading the zip file")
            response = requests.get(self.url)
            with tempfile.NamedTemporaryFile() as zip_file:
                zip_file.write(response.content)
                with zipfile.ZipFile(zip_file) as unzipper:
                    unzipper.extractall(self.target)
            if self.verbose:
                self.timer.stop()
        else:
            if self.verbose:
                print("Files exist, not downloading")
        assert self.target.is_dir()
        return
    
    def __call__(self):
        """calls the download method"""
        self.download()
        return


class PureZipDownloader:
    """Downloads a zip file and unpacks it

    Args:
     url: URL to the zip file
     target: directory to unzip the contents into
     verbose: whether to emit statements
    """
    def __init__(self, url: str, target: str, verbose: bool=True):
        self.url = url
        self.target = Path(target).expanduser()
        self.verbose = verbose
        return
    
    def download(self) -> None:
        if not self.target.is_dir():
            if self.verbose:
                print("Downloading the zip file")
            response = requests.get(self.url)
            with tempfile.NamedTemporaryFile() as zip_file:
                zip_file.write(response.content)
                with zipfile.ZipFile(zip_file) as unzipper:
                    unzipper.extractall(self.target)
            if self.verbose:
                print("Finished downloading and unzipping the file")
        else:
            if self.verbose:
                print("Files exist, not downloading")
        assert self.target.is_dir()
        return
    
    def __call__(self):
        """calls the download method"""
        self.download()
        return
