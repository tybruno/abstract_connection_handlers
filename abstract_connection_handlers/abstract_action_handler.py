from abc import ABC, abstractmethod


class AbstractActionHandler(ABC):
    @abstractmethod
    def __call__(self, mapped_actions: map):
        ...
