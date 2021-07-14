from abc import ABC


class AbstractActionMapper(ABC):
    def __init__(self, action_hander_mapper: map):
        ...

    def __call__(self, connection_handlers) -> map:
        ...
