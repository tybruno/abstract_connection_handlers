from abc import ABC, abstractmethod
from dataclasses import dataclass
from abstract_connection_handlers.abstract_connections_handlers.abstract_handlers_generators import (
    AbstractConnectionHandlersGenerator,
)
from abstract_connection_handlers.abstract_connections_handlers.abstract_handler_details import (
    HandlerDetails,
)
from abstract_connection_handlers.abstract_connections_handlers.abstract_action import (
    AbstractHandlerAction,
)
from abstract_connection_handlers.abstract_connections_handlers.abstract_action_handler import (
    AbstractActionHandler,
)
from abstract_connection_handlers.abstract_connections_handlers.abstract_action_mapper import (
    AbstractHandlerSendCommandsActionMapper,
)


class AbstractRunner(ABC):
    def __init__(
        self,
        action_mapper: AbstractHandlerSendCommandsActionMapper,
        action_handler: AbstractActionHandler,
    ):
        self.action_mapper = action_mapper
        self.action_handler = action_handler

    @abstractmethod
    def __call__(self, *args, **kwargs):
        ...
