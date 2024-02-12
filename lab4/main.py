class Transport:
    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def move(self):
        print(f"{self.name} is moving at {self.speed} mph.")

    def stop(self):
        print(f"{self.name} has stopped.")

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__})"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.speed})"


class Car(Transport):
    def __init__(self, name: str, speed: float, num_wheels: int):
        super().__init__(name, speed)
        self.num_wheels = num_wheels

    def honk(self):
        print("Beep beep!")

    def __str__(self):
        return f"{super().__str__()}, {self.num_wheels} wheels"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.speed}, {self.num_wheels})"


class Truck(Transport):
    def __init__(self, name: str, speed: float, cargo_capacity: float):
        super().__init__(name, speed)
        self.cargo_capacity = cargo_capacity

    def load_cargo(self):
        print(f"{self.name} is loading cargo.")

    def __str__(self):
        return f"{super().__str__()}, cargo capacity: {self.cargo_capacity} lbs"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.speed}, {self.cargo_capacity})"


class Bus(Transport):
    def __init__(self, name: str, speed: float, passengers: int):
        super().__init__(name, speed)
        self.passengers = passengers

    def BusStop(self):
        print(f"{self.name} has {self.passengers} seats.")

    def __str__(self):
        return f"{super().__str__()}, {self.passengers} passengers"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.speed}, {self.passengers})"


my_car = Car("Tesla Model S", 150, 4)
my_truck = Truck("Ford F-150", 100, 2000)
my_bus = Bus("Mercedes-Benz", 60, 52)

print(my_car)
print(my_truck)
print(my_bus)
