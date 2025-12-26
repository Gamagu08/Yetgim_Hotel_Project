from abc import ABC, abstractmethod

class Room(ABC):
    def __init__(self, room_number, base_price):
        self._room_number = room_number
        self._base_price = base_price

    @property
    def room_number(self):
        return self._room_number

    @property
    def price(self):
        return self._base_price

    @abstractmethod
    def calculate_price(self, stay_duration):
        pass

    def __str__(self):
        return f"Room {self._room_number} | Type: {self.__class__.__name__} | Price: ${self._base_price}/night"

class StandardRoom(Room):
    def calculate_price(self, stay_duration):
        return self._base_price * stay_duration

class SuiteRoom(Room):
    def calculate_price(self, stay_duration):
        total = self._base_price * stay_duration
        if stay_duration > 3:
            total *= 0.90 
        return total