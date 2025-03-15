import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class GameCharacter(Prototype):
    def __init__(self,name,weapon,health):
        self.name = name
        self.weapon = weapon
        self.health = health
    
    def __str__(self):
        return f"Character: {self.name}, Weapon: {self.weapon}, Health: {self.health}"

warrior = GameCharacter("Warrior","Sword",100)

archer = warrior.clone()
archer.name = "Archer"
archer.weapon = "Bow"

print(warrior)
print(archer)