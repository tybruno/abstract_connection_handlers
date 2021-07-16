from abc import ABC, abstractmethod
from dataclasses import dataclass
from abstract_connection_handlers.abstract_connections_handlers.abstract_handlers_generators import (
    AbstractHandlersGenerator,
)
from abstract_connection_handlers.abstract_connections_handlers.abstract_handler_details import (
    HandlerDetails,
)
from abstract_connection_handlers.abstract_connections_handlers.abstract_action import (
    AbstractHandlerAction,
)


@dataclass
class AbstractRunBook(ABC):
    handler_generator: AbstractHandlersGenerator
    handler_action: AbstractHandlerAction

    @abstractmethod
    def __call__(self, hosts):
        ...
