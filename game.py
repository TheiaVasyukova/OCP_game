from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "мечом"

    def __str__(self):
        return "меч"

class Bow(Weapon):
    def attack(self):
        return "из лука"

    def __str__(self):
        return "лук"

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon}.")

    def attack(self):
        if self.weapon is not None:
            print(f"{self.name} наносит удар {self.weapon.attack()}.")
        else:
            print(f"{self.name} не вооружен!")

class Monster:
    def __init__(self, name):
        self.name = name

    def is_defeated(self):
        print(f"{self.name} побежден!")

def main():
    fighter = Fighter("Боец")
    monster = Monster("Монстр")

    sword = Sword()
    fighter.changeWeapon(sword)
    fighter.attack()
    monster.is_defeated()

    bow = Bow()
    fighter.changeWeapon(bow)
    fighter.attack()
    monster.is_defeated()

if __name__ == "__main__":
    main()
