from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import Iterable


from abstract_connection_handlers.abstract_action_handler import (
    AbstractActionHandler,
)
from abstract_connection_handlers.abstract_action_mapper import (
    HandlerSendCommandsActionMapper,
)
from abstract_connection_handlers.abstract_handler_details import (
    HandlerDetails,
)


class AbstractRunner(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs):
        ...


@dataclass
class CommandRunnerDetails:
    hosts: Iterable
    handler_details: HandlerDetails
    commands: Iterable[str]


@dataclass
class CommandRunner(AbstractRunner):
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
