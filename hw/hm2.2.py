#Наследование и полиморфизм в ООП

class Hero:
    def __init__(self, name, level, health, strength):
        self.hero_name = name
        self.hero_level = level
        self.hero_health = health
        self.hero_strength = strength

    def greet(self):
        print(f'Привет, я {self.hero_name}, мой уровень {self.hero_level}')
    def attack(self):
        print(f"{self.hero_name} наносит удар!")
        self.hero_strength -= 1
    def rest(self):
        print(f"{self.hero_name} отдыхает…")
        self.hero_health += 1
class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.hero_stamina = stamina

    def attack(self):
        print(f"Воин {self.hero_name} атакует мечом!")
class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.hero_mana = mana

    def attack(self):
        print(f"Маг {self.hero_name} кастует заклинание!")

class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.hero_stealth = stealth

    def attack(self):
        print(f"Ассасин {self.hero_name} атакует из-под тишка!")

lolo = Warrior("Lolo", 100, 50, 500, 5000)
print(lolo.hero_name)
polo = Mage("Polo", 75, 350, 2500, 2000)
print(polo.hero_name)
kolo = Assassin("Kolo", 150, 850, 400, 3000)
print(kolo.hero_name)

#крестики нолики

import random

heroes = ["Warrior", "Mage", "Assassin"]

player = input("Выберите героя (Warrior / Mage / Assassin): ")
enemy = random.choice(heroes)

print("Вы выбрали:", player)
print("Противник:", enemy)

if player == enemy:
    print("Ничья!")
elif player == "Warrior" and enemy == "Assassin":
    print("Warrior победил!")
elif player == "Assassin" and enemy == "Mage":
    print("Assassin победил!")
elif player == "Mage" and enemy == "Warrior":
    print("Mage победил!")
else:
    print(enemy, "победил!")