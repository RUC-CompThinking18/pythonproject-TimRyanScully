from Dice import Dice
from Character import *
from GM import *

Game = Campaign("test")

Game.Location("Your Room", "You wake up home alone to the sound of your alarm clock. You are in bed and deciding what to do.", "Get up", "hit the snooze", "Check what time it is", "Stay in bed")


def GameLoop():
    if (Game.selected == "Get up"):
        Game.Location("Your Room", "You get up out of bed and streatch. Your bedroom door lies in front of you To your right is the bathroom door. To your left is your bedroom beauru. Behind you is your bed. Your bed is currently not made. ", "Make Bed", "Go to Bedroom Door", "Go to the Bathroom", "Examine Beauru")
    elif (Game.selected == "hit the snooze"):
        Game.Results("You slam the snooze button on your alarm clock and sleep five more minutes.")
        GameLoop()
    elif (Game.selected == "Check what time it is"):
        Game.Results("You fumble with the alarm clock and see it says 7:20 AM. You are late for work.")
        GameLoop()
    elif(Game.selected == "Stay in bed"):
        Game.Results("You turn off your alarm clock and roll over. You miss work, and have one less sick day.")
    else:
        GameLoop()

GameLoop()
