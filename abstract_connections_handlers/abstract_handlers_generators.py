from abstract_connection_handlers.abstract_connections_handlers.abstract_handler_details import (
    HandlerDetails,
)
from abc import abstractmethod, ABC
from typing import Iterable


class AbstractConnectionHandlersGenerator(ABC):
    def __init__(self, default_details: HandlerDetails, handler_factory):
        self.default_details = default_details
        self.handler_factory = handler_factory

    @abstractmethod
    def __call__(self, hosts: Iterable[str]):
        ...
