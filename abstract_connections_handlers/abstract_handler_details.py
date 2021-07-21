from dataclasses import (
    MISSING,
    asdict,
    dataclass,
    fields,
    is_dataclass,
)
from typing import NamedTuple, Iterable


class _UNSET(type(MISSING)):
    ...


UNSET = _UNSET()


@dataclass
class Details:
    def as_dict(self):
        dictionary = {}

        for f in fields(self):
            attr = getattr(self, f.name)
            if isinstance(attr, Details):
                dictionary.update(attr.as_dict())
            elif is_dataclass(attr):
                dictionary.update(asdict(attr))
            elif isinstance(attr, _UNSET):
                continue
            elif attr:
                dictionary[f.name] = attr

        return dictionary


@dataclass
class AuthenticationDetails(Details):
    auth_username: str
    auth_password: str
    auth_secondary: str


@dataclass
class ConnectionDetails(Details):
    ...


@dataclass
class HandlerDetails(Details):
    auth_details: AuthenticationDetails
    connection_details: ConnectionDetails


@dataclass
class RunnerDetails:
    hosts: Iterable
    handler_details: HandlerDetails
    commands: Iterable[str]
