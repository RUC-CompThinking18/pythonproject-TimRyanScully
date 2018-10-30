from Dice import Dice
from Character import *

class Campaign(object):

    def __init__(self, name):

        self.name = str(name)

    def Genre(self, name):

        self.genre = name

    def Location(self, name, description, choices):

        self.location = name

        self.description  = description

        self.choices = int(choices)

    def Instructions(self, instructions):

        self.instructions = instructions

    def Option(self, name, input, choice):

        self.option = name

        input = ("What do you do?\nEnter your choice here -> ")

        if input ==


class Item(object):

    def __init__(self, name):

        self.name = str(name)

    def Taken(self, owner):

        self.owner = owner

    def Equip(self):

        self.equipped = True

    def Unequip(self):

        self.equipped = False;

    def Weapon(self, attack, damage):

        self.type = "weapon"

        if (self.equipped == True):

            self.owner.attack = int(attack)

            self.owner.damage = int(damage)

        else:

            self.owner.attack -= int(attack)

            self.owner.damage -= int(damage)

    def Armor(self, ac):

        self.type = "armor"

        if (self.equipped == True):

            self.owner.ac += int(ac)

        else:

            self.owner.ac += int(ac)


class Reward(object):

    def __init__(self, name, recipient):

        self.name = str(name)

        self.recipient = recipient

    def Money(self, money):

        recipient = self.recipient

        recipient.money += money

    def XP(self, xp):

        recipient = self.recipient

        recipient.xp += int(xp)

    def LevelUp(self, xp):

        recipient = self.recipient

        if (recipient.xp >= xp):

            recipient.level += 1

            return True

        else:

            return False
