# python
import logging

# pypi
from colorama import Style

# this project
from graeae.infrastructure.logging import SysLogBuilder
from graeae.timers import Timer

class SysLogBase:
    """A parent class that adds a logger and a Timer

    UML:
     SysLogBase o-- logging.Logger
     SysLogBase o-- Timer     
    """
    def __init__(self) -> None:
        self._log = None
        self._timer = None
        self.message = "All is complete"
        self.syslog_format = ("%(asctime)s: %(levelname)s: (wicca) %(name)s:"
                             " %(funcName)s %(message)s")
        return

    @property
    def log(self) -> logging.Logger:
        """A system-logger"""
        if self._log is None:
            self._log = SysLogBuilder(
                f"{Style.BRIGHT}{self.__class__.__name__}{Style.RESET_ALL}",
                log_format=self.syslog_format).logger
        return self._log

    @property
    def timer(self) -> Timer:
        """A time-tracker"""
        if self._timer is None:
            self._timer = Timer(message=self.message,
                                prefix=f"{Style.BRIGHT}{self.__class__.__name__}{Style.RESET_ALL}",
                                output=self.log.info)
        return self._timer
