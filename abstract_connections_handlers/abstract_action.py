from abc import ABC, abstractmethod

from typing import Iterable, Generator


class AbstractHandlerAction(ABC):
    @abstractmethod
    def __call__(self, connection_handler):
        ...


class AbstractSendCommandsAction(AbstractHandlerAction):
    def __init__(self, commands: Iterable[str], stop_on_failed: bool = False):
        self.commands = commands
        self.stop_on_failed = stop_on_failed

    @abstractmethod
    def __call__(self, connection_handler):
        ...
