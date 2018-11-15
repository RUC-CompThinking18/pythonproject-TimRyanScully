#TIMOTHY RYAN SCULLY

from Dice import Dice
from Character import *
from GM import *

print("\n\n!-------------------------------------------------WELCOM TO THE REAL LIFE RPG--------------------------------------------------------------------!")

name = input("\n\nPlease enter your name :")

Game = Campaign("rlRPG")
Player = Character(name)
hours = 6
minutes = 30
time = str(hours) + ":" + str(minutes) + "AM";

Game.Location("\nYour Room", "You wake up home alone to the sound of your alarm clock. You are in bed and deciding what to do.", "Get up", "hit the snooze", "Check what time it is", "Stay in bed")


def GameLoop():
    if (Game.selected == "Get up"):
        Game.Location("Your Room", "You get up out of bed and streatch. Your bedroom door lies in front of you To your right is the bathroom door. To your left is your bedroom beauru. Behind you is your bed. Your bed is currently not made. ", "Make Bed", "Go to Bedroom Door", "Go to the Bathroom", "Examine Beauru")
    elif (Game.selected == "hit the snooze"):
        Game.Results("You slam the snooze button on your alarm clock and sleep five more minutes.")
        GameLoop()
    elif (Game.selected == "Check what time it is"):
        Game.Results("You fumble with the alarm clock and see it says " + time + ". You need to be at work by eight.")
        GameLoop()
    elif(Game.selected == "Stay in bed"):
        print("You turn off your alarm clock and roll over. You miss work, and have one less sick day.")

GameLoop()
print ("\n\nIf you want to play more of this game, please send the developer $500.00. \n\nOtherwise, thank you for playing ", Player.name, "!")
