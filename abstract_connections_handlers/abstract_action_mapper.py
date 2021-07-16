from abc import ABC, abstractmethod
from abstract_connection_handlers.abstract_connections_handlers.abstract_action import (
    AbstractHandlerAction,
)


class AbstractActionMapper(ABC):
    def __init__(
        self, action: AbstractHandlerAction, action_hander_mapper: map = map
    ):
        self.action = action
        self.action_hander_mapper = action_hander_mapper

    @abstractmethod
    def __call__(self, *args, **kwargs) -> map:
        ...
