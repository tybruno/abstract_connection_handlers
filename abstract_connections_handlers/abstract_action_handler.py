from abc import ABC, abstractmethod
from abstract_connection_handlers.abstract_connections_handlers.abstract_action_mapper import (
    AbstractHandlerSendCommandsActionMapper,
)


class AbstractActionHandler(ABC):
    @abstractmethod
    def __call__(self, mapped_actions: map):
        ...
