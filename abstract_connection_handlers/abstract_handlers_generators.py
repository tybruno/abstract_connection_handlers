from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Generator,
    Iterable,
)

from abstract_connection_handlers.abstract_handler_details import (
    Details,
    HandlerDetails,
)


class AbstractConnectionHandlersGenerator(ABC):
    handler_factory = None

    def __init__(self, default_details: HandlerDetails):
        self.default_details = default_details

    @abstractmethod
    def __call__(self, hosts: Iterable[str]):
        ...


class HandlerGenerator(AbstractConnectionHandlersGenerator):
    def __call__(
        self,
        hosts: Iterable[str],
    ) -> Generator:
        if isinstance(hosts, str):
            hosts = (hosts,)

        return self._get_details_from_hosts(hosts)

    def _get_details_from_hosts(self, hosts) -> Generator:
        for host in hosts:
            connection_details = self.default_details.as_dict()
            if isinstance(host, str):
                connection_details["host"] = host

            if isinstance(host, dict):
                connection_details.update(host)

            if isinstance(host, Details):
                connection_details.update(host.as_dict())

            handler = self.handler_factory(**connection_details)
            yield handler
