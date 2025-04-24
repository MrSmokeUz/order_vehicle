import logging

from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO)

class Vehicle(ABC):

    def __init__(self,vehicle_name:str,number_of_seats:int,available_seats:int):

        if number_of_seats < 0:
            raise ValueError("Number cannot be negative")

        if not (0<=available_seats<=number_of_seats):
            raise ValueError("Available seats must be between 0 and number_of_seats.")

        self.vehicle_name = vehicle_name
        self.number_of_seats = number_of_seats
        self.available_seats = available_seats

    def book_seat(self):
        if self.available_seats <= 0:
          raise RuntimeError("No available  seats to book")
        else:
            self.available_seats -= 1
            logging.info(f"Booked successfully. {self.available_seats} remaining")

    def cancel_seat(self):
        if self.available_seats >= self.number_of_seats:
            raise RuntimeError("Cannot cansel seats more than the number of seats")
        else:
            self.available_seats += 1
            logging.info("Cancelled successfully")
    @property
    def occupied_seats(self):
        return self.number_of_seats - self.available_seats

    def is_full(self):
        return self.available_seats == 0

    @abstractmethod
    def get_info(self):
        pass

    def __str__(self):
        return self.get_info()

class Bus(Vehicle):
    def __init__(self, vehicle_name: str, route_number:str, number_of_seats:int,available_seats:int):
        super().__init__(vehicle_name,number_of_seats,available_seats)
        self.route_number = route_number


    def get_info(self):
        info = f"Bus {self.vehicle_name} | Route: {self.route_number} | Number of seats: {self.number_of_seats} | Number of Available seats {self.available_seats}"
        logging.info(info)
        return info


class Train(Vehicle):
    def __init__(self,vehicle_name: str,train_number:str,number_of_seats:int,available_seats:int,has_dining_car:bool):
        super().__init__(vehicle_name,number_of_seats,available_seats)
        self.train_number = train_number
        self.has_dining_car = has_dining_car


    def get_info(self):
            info = (
                f"Train: {self.vehicle_name} | Train number: {self.train_number} | Number of seats: {self.number_of_seats} |"
                f"Number of Available seats: {self.available_seats} | Has dinning car: {'Yes' if self.has_dining_car else 'No'}"
            )
            logging.info(info)
            return info


class Plane(Vehicle):

    def __init__(self,vehicle_name:str,flight_number:str,number_of_seats:int,available_seats:int,airline:str,international:bool):
        super().__init__(vehicle_name,number_of_seats,available_seats)
        self.flight_number = flight_number
        self.airline = airline
        self.international = international


    def get_info(self):
        info = (
            f"Plane: {self.vehicle_name} |"
            f"Flight number: {self.flight_number} |"
            f"Number of seats: {self.number_of_seats} |"
            f"Number of Available seats: {self.available_seats} |"
            f"Airline: {self.airline} |"
            f"International: {'Yes' if self.international else 'No'}"
        )
        logging.info(info)
        return info

bus = Bus('Mersedes Bus', '33', 33,25)

bus.book_seat()

print(bus)
bus.book_seat()

train = Train('ATTO express','BLACKWELL 1351',500,450,True)

train.book_seat()

print(train)
