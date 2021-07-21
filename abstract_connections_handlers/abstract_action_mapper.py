from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Iterable,
    Type,
)

from abstract_connection_handlers.abstract_connections_handlers.abstract_action import (
    AbstractSendCommandsAction,
)
from abstract_connection_handlers.abstract_connections_handlers.abstract_handler_details import (
    HandlerDetails,
)
from abstract_connection_handlers.abstract_connections_handlers.abstract_handlers_generators import (
    AbstractConnectionHandlersGenerator,
)


class AbstractHandlerActionMapper(ABC):
    @abstractmethod
    def __call__(
        self,
        *args,
        **kwargs,
    ) -> map:
        ...


class AbstractHostsActionMapper(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs) -> map:
        ...


class AbstractHandlerSendCommandsActionMapper(AbstractHandlerActionMapper):
    @abstractmethod
    def __call__(
        self,
        connection_handlers: Iterable,
        commands: Iterable[str],
        *,
        stop_on_failed: bool = False,
    ) -> map:
        ...


class HandlerSendCommandsActionMapper(AbstractHandlerSendCommandsActionMapper):
    def __init__(
        self,
        action: Type[AbstractSendCommandsAction],
        mapping_factory: map = map,
    ):
        self.action = action
        self.mapping_factory = mapping_factory

    def __call__(
        self,
        connection_handlers: Iterable,
        commands: Iterable[str],
        *,
        stop_on_failed: bool = False,
    ) -> map:
        handler_action = self.action(
            commands=commands, stop_on_failed=stop_on_failed
        )
        mapping = map(handler_action, connection_handlers)
        return mapping


class ScrapliHostsSendCommandsActionMapper(AbstractHostsActionMapper):
    def __init__(
        self,
        handler_details: HandlerDetails,
        handler_generator: Type[AbstractConnectionHandlersGenerator],
        mapper: AbstractHandlerActionMapper,
    ):
        self.handler_details = handler_details
        self.handler_generator = handler_generator
        self.mapper = mapper

    def __call__(
        self,
        hosts: Iterable[str],
        commands: Iterable[str],
        *,
        stop_on_failed: bool = False,
    ) -> Iterable:
        # Generate connection handlers from the hosts
        generate_handlers = self.handler_generator(
            default_details=self.handler_details
        )
        scrapli_handlers = generate_handlers(hosts)

        # map actions to the generated connection handlers
        mapped_actions = self.mapper(
            connection_handlers=scrapli_handlers, commands=commands
        )

        return mapped_actions
