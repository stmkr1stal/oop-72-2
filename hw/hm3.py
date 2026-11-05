from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает…")
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):
    def attack(self):
        print(f"Воин {self.name} атакует мечом!")

class Mage(Hero):
    def attack(self):
        print(f"Маг {self.name} использует магию!")

class Assassin(Hero):
    def attack(self):
        print(f"Ассасин {self.name} атакует из-под тишка!")

lolo = Warrior("Lolo", 100, 50, 500)
polo = Mage("Polo", 75, 350, 2500)
kolo = Assassin("Kolo", 150, 850, 400)

lolo.greet()
lolo.attack()
lolo.rest()

polo.greet()
polo.attack()
polo.rest()

kolo.greet()
kolo.attack()
kolo.rest()
