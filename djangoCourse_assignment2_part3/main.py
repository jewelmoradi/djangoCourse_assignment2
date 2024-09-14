# assignment 2
# part 3: polymorphism

class Animal:

    def make_sound(self):
        print('Some generic sound')


class Dog(Animal):

    def make_sound(self):
        print('Woof')


class Cat(Animal):

    def make_sound(self):
        print('Meow')


def animal_sound(creature):
    creature.make_sound()


animal_list = [Dog(), Cat(), Cat(), Dog(), Dog()]

for item in animal_list:
    item.make_sound()
