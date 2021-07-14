from abc import ABC


class AbstractAuthenticationDetails(ABC):
    ...


class AbstractConnectionDetails(ABC):
    ...


class AbstractHandlerDetails(ABC):
    def __init__(
        self,
        auth_details: AbstractAuthenticationDetails,
        connection_details: AbstractConnectionDetails,
    ):
        ...
