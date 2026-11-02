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
spiderman = Hero("spiderman", 25, 100, 99)
print(f"здоровье до:{spiderman.hero_health}, сила до:{spiderman.hero_strength}")
spiderman.greet()
spiderman.attack()
spiderman.rest()
print(f"здоровье после:{spiderman.hero_health}, сила после:{spiderman.hero_strength}")

ironman = Hero("ironman", 125, 70, 89)
print(f"здоровье до:{ironman.hero_health}, сила до:{ironman.hero_strength}")
ironman.greet()
ironman.attack()
ironman.rest()
print(f"здоровье после:{ironman.hero_health}, сила после:{ironman.hero_strength}")

