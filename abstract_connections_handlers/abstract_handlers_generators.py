from abc import ABC, abstractmethod
from typing import Type, Iterable


class AbstractHandlersGenerator:
    def __init__(self, handler: Type):
        ...

    @abstractmethod
    def __call__(self, hosts: Iterable[str]):
        ...
