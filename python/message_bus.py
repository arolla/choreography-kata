import abc
from typing import List
from dataclasses import dataclass

@dataclass
class Event:
    name: str
    value: int


class Listener(abc.ABC):
    @abc.abstractmethod
    def on_message(self, message: Event):
        ...

class MessageBus:
    def __init__(self):
        self._subs: List[Listener] = []

    def subscribe(self, l: Listener):
        self._subs.append(l)

    def send(self, message: Event):
        for l in self._subs:
            l.on_message(message)
