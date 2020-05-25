
class Weapons:
    '''Class to define a weapon. Requires weapon name, descritpion, and attack value'''
    def __init__(self, name, desc, attack):
        self.name = name
        self.desc = desc
        self.attack = attack


class Room(Weapons):
    '''Class to define room. Requires exits, description, any enemies and inventory'''
    def __init__(self, exits, desc, inventory, location, enemy, weapon):
        self.exits = exits
        self.desc = desc
        self.inventory = inventory
        self.location = location
        self.enemy = enemy
        self.weapon = weapon

class Enemy:
    'Define and enemy. Requires health, attack, weapon type'
    def __init__(self, name, health, attack, weapon, mood):
        self.name = name
        self.health = health
        self.attack = attack
        self.weapon = weapon
        self.mood = mood


class Items:
    '''Class to define items that don't have values like a key. Requires name, description'''
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc


class Food:
    '''Class to define food. Requires name, health value, description'''
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Player:
    'Define player. Takes hit points and empty inventory'
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.weapon = []