# Python
from pathlib import Path
import os

# PyPi
from colorama import Style, Fore
from dotenv import load_dotenv

# this project
from graeae import SysLogBase

class EnvironmentLoader(SysLogBase):
    """Loads the environment variables

    UML:
     SysLogBase <|-- EnvironmentLoader

    Args:
     path: path to the env file
    """
    def __init__(self, path: str="~/.env") -> None:
        super().__init__()
        self.path = path
        self._environment_path = None
        self._environment = None
        return
    
    @property
    def environment_path(self) -> Path:
        """The path to the environment file"""
        if self._environment_path is None:
            self._environment_path = Path(self.path).expanduser()
            assert self._environment_path.is_file(),\
                f"{Style.BRIGHT}{Fore.RED}'{self.path}' is not a file"
            self.log.debug(f"Environment Path: {self._environment_path}")
        return self._environment_path
    
    @property
    def environment(self) -> dict:
        """The enviroment variables"""
        if self._environment is None:
            load_dotenv(self.environment_path, override=True)
            self._environment = os.environ
        return self._environment
    
    def __getitem__(self, variable: str) -> str:
        """Get the value for the environment variable

        Args:
         variable: name of the environment variable to get
        """
        return self.environment.get(variable)

class SubPathLoader(SysLogBase):
    """Loads a sub-environment found in the base environment

    UML:
    
     SysLogBase <|-- SubPathLoader
     SubPathLoader o-- EnvironmentLoader

    Args:
     sub_key: key in the environment that points to the sub-environment
     root: the path to the main env file
    """
    def __init__(self, sub_key: str, root: str="~/.env") -> None:
        super().__init__()
        self.sub_key = sub_key
        self.root = root
        self._root_environment = None
        self._environment = None
        self._environment_path = None
        return
    
    @property
    def root_environment(self) -> EnvironmentLoader:
        """Something to load the root environment"""
        if self._root_environment is None:
            self._root_environment = EnvironmentLoader(self.root)
        return self._root_environment
    
    @property
    def environment_path(self) -> Path:
        """Path to the sub-envirnoment"""
        if self._environment_path is None:
            self._environment_path = Path(
                self.root_environment[self.sub_key]).expanduser()
            assert self._environment_path.is_file(),\
                f"{Style.BRIGHT}{Fore.RED}'{self.path}' is not a file"
            self.log.debug(f"Environment Path: {self._environment_path}")
        return self._environment_path
    
    @property
    def environment(self) -> dict:
        """The environment dict"""
        if self._environment is None:
            load_dotenv(self.environment_path, override=True)
            self._environment = os.environ
        return self._environment
    
    def __getitem__(self, variable: str) -> str:
        """Get the value for the environment variable

        Args:
         variable: name of the environment variable to get
        """
        return self.environment.get(variable)
