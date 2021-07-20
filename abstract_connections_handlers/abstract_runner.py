from abc import ABC, abstractmethod
from typing import Iterable, Type
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
from abstract_connection_handlers.abstract_connections_handlers.abstract_action_mapper import (
    HandlerSendCommandsActionMapper,
)


class AbstractRunner(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs):
        ...


@dataclass
class SendCommandsRunner(AbstractRunner):
    def __init__(
        self,
        action_mapper: HandlerSendCommandsActionMapper,
        action_handler: AbstractActionHandler,
    ):
        self.action_mapper = action_mapper
        self.action_handler = action_handler

    def __call__(
        self,
        hosts: Iterable[str],
        commands: Iterable[str],
        *,
        stop_on_failed: bool = False
    ):
        mapped_actions = self.action_mapper(
            hosts=hosts, commands=commands, stop_on_failed=stop_on_failed
        )
        handled_actions = self.action_handler(mapped_actions)
        return handled_actions
