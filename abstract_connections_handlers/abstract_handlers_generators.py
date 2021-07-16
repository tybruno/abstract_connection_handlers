from abc import abstractmethod
from typing import Type, Iterable


class AbstractHandlersGenerator:
    def __init__(self, handler_factory: Type):
        ...

    @abstractmethod
    def __call__(self, hosts: Iterable[str]):
        ...
