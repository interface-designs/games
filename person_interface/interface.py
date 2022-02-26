from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, address, email, phone):
        self.name, self.address, self.email, self.phone = name, address, email, phone

    @abstractmethod
    def info(self):
        pass