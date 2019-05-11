# python
from datetime import datetime
from typing import Callable

# pypi
try:
    import pyttsx3
    SPEAKABLE = True
except ImportError:
    print("pyttsx3 not available")
    SPEAKABLE = False

# this project
from graeae.infrastructure import SysLogBuilder


if not SPEAKABLE:
    class EngineMock:
        """A fake engine"""

    class pyttsx3:
        """A fake module"""
        engine = EngineMock
        engine.Engine = None


class Timer:
    """Emits the time between calling start and end

    Args:
     speak: If true, say something at the end
     message: what to say
     prefix: something to add to the strings
     emit: if False, just stores the times
     output: callable to send the output to
    """
    def __init__(self, beep: bool=True, message: str="All Done",
                 prefix: str = "",
                 emit:bool=True, output=None) -> None:
        self.beep = beep
        self.message = message
        self.emit = emit
        self.prefix = prefix
        if self.prefix:
            self.prefix = f"({prefix}) "
        self._output = output
        self._speaker = None
        self.started = None
        self.ended = None
        return

    @property
    def output(self) -> Callable:
        """The object to output the strings"""
        if self._output is None:
            self._output = SysLogBuilder(__name__).logger.info
        return self._output

    @property
    def speaker(self) -> pyttsx3.engine.Engine:
        """The espeak speaker"""
        if self._speaker is None:
            self._speaker = pyttsx3.init()
        return self._speaker

    def start(self) -> None:
        """Sets the started time"""
        self.started = datetime.now()
        if self.emit:
            self.output(f"{self.prefix}Started: {self.started}")
        return

    def end(self) -> None:
        """Emits the end and elapsed time"""
        self.ended = datetime.now()
        if self.emit:
            self.output(f"{self.prefix}Ended: {self.ended}")
            self.output(f"{self.prefix}Elapsed: {self.ended - self.started}")
        if SPEAKABLE and self.beep:
            self(self.message)
        return
    
    def __call__(self, message: str) -> None:
        """Sends a message to the speaker"""
        self.speaker.say(message)
        self.speaker.runAndWait()
        return

    stop = end

    def __enter__(self):
        """Starts the timer"""
        self.start()
        return self

    def __exit__(self, type, value, traceback) -> None:
        """Stops the timer"""
        self.end()
        return

    def __del__(self) -> None:
        """Stops the speaker"""
        self.speaker.stop()
        return
