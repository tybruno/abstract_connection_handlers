from abc import ABC, abstractmethod

from typing import Iterable, Generator


class AbstractHandlerAction(ABC):
    @abstractmethod
    def __call__(self, connection_handler: Iterable) -> Generator:
        ...
