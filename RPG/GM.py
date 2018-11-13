from Dice import Dice
from Character import *

"""
    There are always three things you need for a good Role Playing Game, be it
over table with friends or on the computer by yourself. One are some rules, which
the computer provides almost by default. The other is Player Characters, which are
of course provided by the player class. The last this is a GameMaster, or GM.
The classes below fill the core functions of the GM;

"""

class Campaign(object):

    def __init__(self, name):

        self.name = str(name)

    def Genre(self, name):

        self.genre = name

    def Location(self, name, description, A, B, C, D):

        self.location = name

        self.description  = description

        print (description)

        self.optionA = A

        self.optionB = B

        self.optionC = C

        self.optionD = D

        print ("\n\nOPTION A: ",A,"\nOPTION B: ",B,"\nOPTION C: ",C,"\nOPTION D: ",D)

        self.Select()

    def Select(self):

        selected = ""

        selection = input("\nWhat do you do?: ")

        if (selection == "A" or selection == "a"):

            selected = self.optionA

        elif (selection == "B" or selection == "b"):

            selected = self.optionB

        elif (selection == "C" or selection == "c"):

            selected = self.optionC

        elif (selection == "D" or selection == "d"):

            selected = self.optionD

        else:

            print ("That is not a valid option. Select A,B,C,or D.")

            self.Select()

        self.selected = selected

        return(selected)

    def Results(self, results):

        self.results = results

        print ("\n",results,"\n")

        self.Location(self.location, self.description, self.optionA, self.optionB, self.optionC, self.optionD)


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
