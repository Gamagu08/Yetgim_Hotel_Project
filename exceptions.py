class HotelError(Exception):
    pass

class RoomNotFoundError(HotelError):
    pass

class RoomOccupiedError(HotelError):
    pass

class InvalidDateError(HotelError):
    pass