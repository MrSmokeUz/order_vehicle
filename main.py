

class Vehicle:
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
            print(f"Booked successfully. {self.available_seats} remaining")

    def get_info(self):
        return f"{self.vehicle_name} has {self.number_of_seats} seats and right now have {self.available_seats} available seats"

    def __str__(self):
        return self.get_info()




seat = Vehicle('Man',30,30)

seat.book_seat()


print(seat)


