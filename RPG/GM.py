from Dice import Dice
from Character import *

"""
    There are always three things you need for a good Role Playing Game, be it
over table with friends or on the computer by yourself. One are some rules, which
the computer provides almost by default. The other is Player Characters, which are
of course provided by the player class. The last this is a GameMaster, or GM.
The classes below fill the core functions of the GM..

"""

class Campaign(object): #Fist of course is to lay out the campaign.It is the world the player plays in

    def __init__(self, name): #initalize with an official name

        self.name = str(name)

    def Genre(self, name): # I originally added genre, as a way of choosing and switching genres. May not be used in final product.

        self.genre = name

    def Location(self, name, description, A, B, C, D): # could easily be a class in and of itself. Might make it so with further developments

        self.location = name

        self.description  = description #This is literally what the player reads when they "enter" the location.

        print (description) #And this puts it in a place where we can see it.

        self.optionA = A #I gave the player 4 options by default. Would not have minded making this aspect more modular, but that is currently beyond my skills.

        self.optionB = B

        self.optionC = C

        self.optionD = D

        print ("\n\nOPTION A: ",A,"\nOPTION B: ",B,"\nOPTION C: ",C,"\nOPTION D: ",D) #We print the different options so the player knows what to do.

        self.Select() # and allow the player to select their option, of course.

    def Select(self):

        selected = "" #we initialize a variable selected as an empty string

        selection = input("\nWhat do you do?: ") #What almost every DM or GM asks their players when its their turn to act.

        if (selection == "A" or selection == "a"): #All made to work with lower or uppercase character. Might be an easier way to type this.

            selected = self.optionA

        elif (selection == "B" or selection == "b"):

            selected = self.optionB

        elif (selection == "C" or selection == "c"):

            selected = self.optionC

        elif (selection == "D" or selection == "d"):

            selected = self.optionD

        else:

            print ("That is not a valid option. Select A,B,C,or D.") # considering throwing an exception instead, but this will work for now.

            self.Select()

        self.selected = selected #designates what's selected

        return(selected) #We can use this method as a variable as well. Might be unnecessary, though.

    def Results(self, results): # this is more for when you get results but you don't change location. Loops back to where you were

        self.results = results

        print ("\n",results,"\n")

        self.Location(self.location, self.description, self.optionA, self.optionB, self.optionC, self.optionD)


class Item(object): #It's not a good RPG unless you can collect some swag.

    def __init__(self, name):#like everythign else in existance, it gets a name upon discovery.

        self.name = str(name)

    def Taken(self, owner): #Whan happens when the main character takes this object?

        self.owner = owner

    def Equip(self): #What happens when you use/wear/arm yourself with said item

        self.equipped = True

    def Unequip(self): #gotta unarm it sometimes.

        self.equipped = False

        if (self.type == "weapon"): #Was originally in the 'Weapon' function, but it makes more sense here.

            self.owner.attack -= int(attack)

            self.owner.damage -= int(damage)

    def Weapon(self, attack, damage): #Declare it as a weapon.

        self.type = "weapon" #set the type

        if (self.equipped == True): #check if equipped. Might need to reimplement. should work when the player equipps and unequipps the weapon.

            self.owner.attack = int(attack) #add the weapons attack bonus

            self.owner.damage = int(damage) #and damage bonus


    def Armor(self, ac):

        self.type = "armor" #similar problems as with the weapon function. Might need to reimplement

        if (self.equipped == True):

            self.owner.ac += int(ac)

        else:

            self.owner.ac -= int(ac)


class Reward(object): #The reason you came to the table and the thing that allows this to all become one giant hamster wheel...

    def __init__(self, name, recipient): #You name the reward and designate a character as the recipient. Can easily be a monster as well :).

        self.name = str(name)

        self.recipient = recipient

    def Money(self, money): #It's nice to get paid for your hard work.

        recipient = self.recipient

        recipient.money += money

    def XP(self, xp): #It's also nice to gain xp points.

        recipient = self.recipient

        recipient.xp += int(xp)

    def LevelUp(self, xp): #and uh... what happens when you get enough xp?

        recipient = self.recipient #I find myself writing this repetitively. Is there a way to scope or replicate this better?

        if (recipient.xp >= xp):

            recipient.level += 1 #Player 1 has gained a level.

            return True

        else:

            return False #or has he?


#Further Notes; Would be nice to have a GUI or Gameloop class as well to make this a proper game. Might develop more in the future outside of class.
