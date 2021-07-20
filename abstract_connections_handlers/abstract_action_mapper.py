from abc import ABC, abstractmethod
from abstract_connection_handlers.abstract_connections_handlers.abstract_action import (
    AbstractHandlerAction,
)
from abstract_connection_handlers.abstract_connections_handlers.abstract_handler_details import (
    HandlerDetails,
)
from abstract_connection_handlers.abstract_connections_handlers.abstract_handlers_generators import (
    AbstractConnectionHandlersGenerator,
)
from typing import Iterable


class AbstractActionMapper(ABC):
    def __init__(
        self, action: AbstractHandlerAction, mapping_factory: map = map
    ):
        self.action = action
        self.mapping_factory = mapping_factory

    @abstractmethod
    def __call__(self, *args, **kwargs) -> map:
        ...
