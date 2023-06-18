class User:
    def __init__(self, health):
        self.health = health

    def attack(self, target):
        damage = 10
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage


class Mage(User):
    def cast_spell(self, target):
        damage = 20
        target.take_damage(damage)


class Warrior(User):
    def swing_sword(self, target):
        damage = 15
        target.take_damage(damage)


class Archer(User):
    def shoot_arrow(self, target):
        damage = 12
        target.take_damage(damage)

