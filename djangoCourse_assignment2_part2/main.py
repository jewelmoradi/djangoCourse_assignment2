# assignment 2
# part 2: abstraction

from abc import ABC, abstractmethod


class MarineAnimal(ABC):

    def __init__(self, name: str, habitat: str):
        self.name = name
        self.habitat = habitat

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Fish(MarineAnimal):

    def __init__(self, name: str, habitat: str, fin_type: str, swim_speed: str):
        super().__init__(name, habitat)
        self.fin_type = fin_type
        self.swim_speed = swim_speed

    def move(self):
        print('fishes swim')

    def eat(self):
        print('fishes eat planktons and sea plants')


class Crustacean(MarineAnimal):

    def __init__(self, name: str, habitat: str, shell_type: str, crawl_speed: str):
        super().__init__(name, habitat)
        self.shell_type = shell_type
        self.crawl_speed = crawl_speed

    def move(self):
        print('crustaceans crawl')

    def eat(self):
        print('crustaceans eat algae and smaller creatures')


fish = Fish('Garfish', 'brackish waters', 'dorsal fin', 'fast')
crustacean = Crustacean('Lobster', 'ocean floor', 'hard-shell', 'slowly')

fish.move()
fish.eat()
crustacean.move()
crustacean.eat()
