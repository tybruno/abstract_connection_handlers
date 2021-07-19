from abc import ABC, abstractmethod
from abstract_connection_handlers.abstract_connections_handlers.abstract_action import (
    AbstractHandlerAction,
)
from typing import Iterable


class AbstractActionMapper(ABC):
    def __init__(
        self, action: AbstractHandlerAction, action_hander_mapper: map = map
    ):
        self.action = action
        self.action_hander_mapper = action_hander_mapper


class BasicConnectMapper(AbstractActionMapper):
    def __init__(
        self,
        connection_handlers: Iterable,
        action: AbstractHandlerAction,
        action_hander_mapper: map = map,
    ):
        super().__init__(
            action=action, action_hander_mapper=action_hander_mapper
        )
        self.connection_handlers = connection_handlers

    def __call__(self, *action_args, **action_kwargs) -> map:
        # Initialize Modifier
        action = self.action(*action_args, **action_kwargs)

        mapping = map(action, self.connection_handlers)

        return mapping
