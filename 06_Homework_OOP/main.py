# Task 1
class Temperature:
    _conversion_count = 0  

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Convert Celsius to Fahrenheit."""
        Temperature._conversion_count += 1
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """Convert Fahrenheit to Celsius."""
        Temperature._conversion_count += 1
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def get_conversion_count():
        """Return the total number of conversions."""
        return Temperature._conversion_count



print(Temperature.celsius_to_fahrenheit(25)) 
print(Temperature.fahrenheit_to_celsius(77))  
print(Temperature.get_conversion_count())  


#Task 2
class Airplane:
    def __init__(self, model, passenger_capacity, current_passengers=0):
        self.model = model
        self.passenger_capacity = passenger_capacity
        self.current_passengers = current_passengers

    
    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.model == other.model
        return False

   
    def __add__(self, passengers):
        if self.current_passengers + passengers <= self.passenger_capacity:
            return Airplane(self.model, self.passenger_capacity, self.current_passengers + passengers)
        else:
            raise ValueError("Exceeding the maximum passenger capacity!")

    def __sub__(self, passengers):
        if self.current_passengers - passengers >= 0:
            return Airplane(self.model, self.passenger_capacity, self.current_passengers - passengers)
        else:
            raise ValueError("Number of passengers cannot be negative!")

   
    def __iadd__(self, passengers):
        if self.current_passengers + passengers <= self.passenger_capacity:
            self.current_passengers += passengers
            return self
        else:
            raise ValueError("Exceeding the maximum passenger capacity!")

    def __isub__(self, passengers):
        if self.current_passengers - passengers >= 0:
            self.current_passengers -= passengers
            return self
        else:
            raise ValueError("Number of passengers cannot be negative!")

    # (>, <, <=, >=)
    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.passenger_capacity < other.passenger_capacity
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.passenger_capacity <= other.passenger_capacity
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.passenger_capacity > other.passenger_capacity
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.passenger_capacity >= other.passenger_capacity
        return NotImplemented

    def __int__(self):
        return self.current_passengers

    def __str__(self):
        return f"Model: {self.model}, Capacity: {self.passenger_capacity}, Current Passengers: {self.current_passengers}"



plane1 = Airplane("Boeing 737", 200, 50)
plane2 = Airplane("Airbus A320", 180, 60)


print(plane1 == plane2)  


plane1 += 20
print(plane1)  

plane1 -= 30
print(plane1)  


print(plane1 > plane2)  


print(int(plane1))  
print(str(plane1)) 
