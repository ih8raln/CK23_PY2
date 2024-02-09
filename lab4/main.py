class Transport:
    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def move(self):
        print(f"{self.name} is moving at {self.speed} mph.")

    def stop(self):
        print(f"{self.name} has stopped.")


class Car(Transport):
    def __init__(self, name: str, speed: float, num_wheels: int):
        super().__init__(name, speed)
        self.num_wheels = num_wheels

    def honk(self):
        print("Beep beep!")


class Truck(Transport):
    def __init__(self, name: str, speed: float, cargo_capacity: float):
        super().__init__(name, speed)
        self.cargo_capacity = cargo_capacity

    def load_cargo(self):
        print(f"{self.name} is loading cargo.")

class Bus(Transport):
    def __init__(self, name: str, speed: float, passengers: int):
        super().__init__(name, speed)
        self.passengers = passengers

    def BusStop(self):
        print(f"{self.name} have {self.passengers} seats.")


my_car = Car("Tesla Model S", 150, 4)
my_truck = Truck("Ford F-150", 100, 2000)
my_bus = Bus("Mercedes-Benz", 60, 52)

my_car.move()
my_car.honk()

my_truck.move()
my_truck.load_cargo()

my_bus.stop()
my_bus.BusStop()