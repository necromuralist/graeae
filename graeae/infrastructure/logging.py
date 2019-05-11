# python
from argparse import Namespace
from pathlib import Path
import logging
import logging.handlers

SysLogDefaults = Namespace(
    address="/dev/log",
    console_format="%(asctime)s %(name)s %(funcName)s: %(message)s",
    log_format=("%(asctime)s: %(levelname)s: %(name)s:"
                " %(funcName)s %(message)s"),
)


class SysLogBuilder:
    """Builds a logger that writes to the screen and the system log

    Args:
     name: name of the logger (usually __name__)
     console_format: String Format for stdout
     log_format: string format for syslog
     address: sys-log address
    """
    def __init__(self, name, 
                 console_format: str=SysLogDefaults.console_format,
                 log_format: str=SysLogDefaults.log_format,
                 address: str=SysLogDefaults.address,
    ) -> None:
        self.name = name
        self.console_format = console_format
        self.log_format = log_format
        self.address = address
        self._sys_logger = None
        self._console_logger = None
        self._sys_formatter = None
        self._console_formatter = None
        self._logger = None
        return

    @property
    def sys_formatter(self) -> logging.Formatter:
        """Formatter for the system log"""
        if self._sys_formatter is None:
            self._sys_formatter = logging.Formatter(self.log_format)
        return self._sys_formatter

    @property
    def sys_logger(self) -> logging.handlers.SysLogHandler:
        """Log-handler to send it to the system-log"""
        if self._sys_logger is None:
            self._sys_logger = logging.handlers.SysLogHandler(self.address)
            self._sys_logger.setFormatter(self.sys_formatter)
            self._sys_logger.setLevel(logging.DEBUG)
        return self._sys_logger

    @property
    def console_formatter(self) -> logging.Formatter:
        """Formatter for stdout"""
        if self._console_formatter is None:
            self._console_formatter = logging.Formatter(self.console_format)
        return self._console_formatter
    
    @property
    def console_logger(self) -> logging.StreamHandler:
        """Log-Handler for stdout"""
        if self._console_logger is None:
            self._console_logger = logging.StreamHandler()
            self._console_logger.setFormatter(self.console_formatter)
            self._console_logger.setLevel(logging.INFO)
        return self._console_logger
    
    @property
    def logger(self) -> logging.Logger:
        """The logger"""
        if self._logger is None:
            self._logger = logging.getLogger(self.name)
            if not self._logger.handlers:
                self._logger.addHandler(self.sys_logger)
                self._logger.addHandler(self.console_logger)
                self._logger.setLevel(logging.DEBUG)
        return self._logger
