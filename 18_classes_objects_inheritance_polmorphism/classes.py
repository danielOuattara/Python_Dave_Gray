
# (00: 16) What are Classes?

"""
classes are blueprint for creating object
"""

# (00: 35) A Simple Class Example


class Vehicle:
    make: str
    model: str

    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along ...')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")


# ---


# (02: 06) Creating an Object

car_1 = Vehicle(make='Opel', model='Corsa')
car_1.moves()  # Moves along ...
print(car_1.make)
print(car_1.model)


car_2 = Vehicle(make='Lada', model='Inoucha')
car_2.get_make_model()


# (03: 10) _init_ and properties

"""
def __init(self, *arg):
    self.arg = arg
    self.make = make
    self.model = model
    etc...
"""

# (05: 13) Creating a get method

"""
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")
"""


# (06: 57) Create multiple objects from a class

"""
car_2 = Vehicle(make='Lada', model='Inoucha', color='green', price=8_500)

"""
# (07: 50) Class Inheritance


class Airplane(Vehicle):

    faa_id: str

    def __init__(self, make, model, faa_id) -> None:
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print('Flies along ...')


class Truck(Vehicle):

    def moves(self):
        print('Rumbles alone ...')


class GolfCart(Vehicle):
    pass


cessna = Airplane(make='Cessna', model='Shyhawk', faa_id='NE4R5E')
volvo_500 = Truck(make='Volvo', model='Breeze 500')
golf_wagon = GolfCart(make='Yamaha', model='GC1100')

cessna.get_make_model()
cessna.moves()

volvo_500.get_make_model()
volvo_500.moves()

golf_wagon.get_make_model()
golf_wagon.moves()

# (12: 25) Child Class _init_ and super()

"""
    faa_id: int | str

    def __init__(self, make, model, faa_id) -> None:
        super().__init__(make, model)
        self.faa_id = faa_id
"""

# (15: 14) Polymorphism
print('\n\n', 50 * '-')


for obj in (car_1, car_2, cessna, volvo_500, golf_wagon):
    obj.get_make_model()
    obj.moves()
    print(obj.model)
    print(10 * '-')


# (17: 57) Review
