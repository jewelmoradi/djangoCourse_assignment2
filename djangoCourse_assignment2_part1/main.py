# assignment 2
# part 1: inheritance

class Vehicle:

    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print('Vehicle started')


class Car(Vehicle):

    def __init__(self, make: str, model: str, year: int, doors: int):
        super().__init__(make, model, year)
        self.doors = doors

    def start(self):
        print('Car started')


class Motorcycle(Vehicle):

    def __init__(self, make: str, model: str, year: int, type: str):
        super().__init__(make, model, year)
        self.type = type

    def start(self):
        print('Motorcycle started')


car = Car('Hyundai Motor', 'Sonata', 2015, 4)
car.start()

motorcycle = Motorcycle('Kawasaki', 'Ninja', 2020, 'sport')
motorcycle.start()
