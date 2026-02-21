class Flight():
    def __init__(self, flight_no, base_price, total_seats):
        self.flight_no = flight_no
        self.base_price= base_price
        self.total_seats= total_seats
    def display_flight_info(self):
        print (f"flight number is {self.flight_no}, with base price {self.base_price}, and available seats is {self.total_seats}")
class DomesticFlight (Flight):
    def __init__(self, flight_no, base_price, total_seats, tax_percent):
        super().__init__(flight_no, base_price, total_seats)
        self.tax_percent= tax_percent
    def calculate_price_with_tax(self):
        return self.base_price + (self.base_price*self.tax_percent/100)
    
class BookingFlight(DomesticFlight):
    def __init__(self, flight_no, base_price, total_seats,tax_percent, seats_booked):
        super().__init__(flight_no, base_price, total_seats,tax_percent)
        self.seats_booked=seats_booked

    def check_seat_availability(self):
        if self.seats_booked <= self.total_seats:
            print("Seats are available")
            return True
        else:
            print ("Seats are not available")
            return False
    def book_seats(self):
        if self.check_seat_availability():
            self.total_seats -= self.seats_booked
            print(f"Booking succesfull!!! seats left are {self.total_seats}")
        else:
            print("booking failed!")
    def get_final_price(self):
        price_per_seat = self.calculate_price_with_tax()
        final_price = price_per_seat * self.seats_booked
        print (f"Final price for booking: {final_price}")


    

booking1 = BookingFlight("FL123", 10000, 12, 10, 2)
booking1.display_flight_info()
booking1.check_seat_availability()
booking1.book_seats()
booking1.get_final_price()