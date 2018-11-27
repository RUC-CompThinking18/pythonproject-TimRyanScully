#TIMOTHY RYAN SCULLY

from Dice import Dice
from Character import *
from GM import *

"""
    This is it... The final masterpeice. I hope everything I build can come together. Seriously doubting already that everything I made will make it into the final product.
I hope you enjoy this game for what it is worth. If this works well, might use it in further personal projectsself.

Enjoy!
"""

#We start with the title screen, complete with an introduction and a place to put your name. Gives the main character object a name in the process.
print("\n\n!-------------------------------------------------WELCOME TO THE REAL LIFE RPG--------------------------------------------------------------------!")

print("\nWhat if your life was like a Role Playing Game? \n\nWouldn't it be fun? \n\nScary? \n\nExciting? \n\nThrilling? \n\nProbably not. \n\nTruth be told, when you strip the things that make a story exciting, you get something like this...")

name = input("\n\nPlease enter your name: ")

Game = Campaign("rlRPG") #kind of useless, but why not?

#Roll your character sheet!
Player = Character(name)
Player.HP(10)

#A list both figurative and literal of locations and their options. WARNING; contents contain spoilers. Please play game before reading code, it possible.
Bed = Location("Bed", "\nYou wake up home alone to the sound of your alarm clock. You are laying in bed and deciding what to do.", "Get up", "hit the snooze", "Check what time it is", "Stay in bed")

Room = Location("Room", "\n\nYou slowly get out of bed with a groan. Streaching upright and punching the alarm clock, you see that the time is 6:30 AM. You need to get ready for work. ", "Go outside", "Go to the bathroom", "Get dressed", "Go back to bed")

Street = Location("Street", "\n\nYou are now out on the street. It is up to you to get to work on time", "If you take the bus to work, you might end up late." ," Then again, the office building is right around the block, Maybe cutway through the alleyway?" , " Or you could just take the taxi. Expensive, but doable.", "Or maybe just come back in and call it a day? You got more sick days...")

Alley = Location("Alley", "\n\n You decide to cut through the alleyway. It's dark, and if you pardon the cliche', just a little too quiet. You do see your office building just up ahead, but before you get there a man comes from around the corner. He asks casually \"Do you have the time?\"", "Tell him the time", "Tell him to get lost", "Try to get past him", "Do something completely random..." )

Fight = Location("Fight", "\n\nIt's you versus the mugger! ROLL INITIATIVE!", "ATTACK", "SURRENDER", "RUN", "SWITCH WEAPON")

Work = Location("Work", "\n\n You finally...FINALLY make it to work. As you make your way past reception and come to the floor with your cubicle farm in it, you see your boss standing outside your cubicle. He scowls at you as you make your way in...", "Say hi to boss", "Ask him what's wrong", "Go to cubicle", "Grab a coffee from the break room")

Locations = [Bed, Room, Street, Alley, Fight, Work]

#I then use a recursive loop to basically manage the flow of the game. Was kind of fustrating to implement, but necessary to avoid spaghetti code.
def GameLoop(Location, index):

    Location.Menu()

    if (Location.selected == Location.optionA):

        if (index < 5):

            if (Location == Street): #special clause for the Street Location.

                print("\n\nWhelp, the bus was about an hour late, and the hobo in the back threw up on your briefcase. Your watch STILL says 6:30 AM though. I guess whoever made the time was lazy...")

                index = 4 #Go straight to work!

            if (Location == Alley):

                print ("\n\n\"It's 6:30 AM\" You say off the top of your head. The guy looks puzzled. \n\"How did you know that so fast?\"\n\"It's been that time all day\"\n\"Whatever\" he says, pulling out a switchblade, \"Gimme your wallet!\"")

                Combat()

            index += 1 #Exit one Location and enter another. Loop works off of the index, so that's all we touch.

        else:

            Talk()

            END() #GAME OVER. YOU WIN?

            return 0


    elif (Location.selected == Location.optionB):

        if(Location == Bed):

            print("\nYou slam the snooze button on your alarm clock and sleep five more minutes.")

        elif (Location == Room):

            print("\n\nYou go to the bathroom and do your business. This game is for decent folk so I will spare you the details. \n\n You do however get +2 HP for hygene!")

            Player.hp += 2

    elif (Location.selected == Location.optionC):

        print("\nYou fumble with the alarm clock and see it says 6:30AM. Even after you pressed the snooze. Weird.") #I couldn't get a time function to work so I improvised.

    elif(Location.selected == Location.optionD):

        if(Location == Bed):

            print("\nYou turn off your alarm clock and roll over. You miss work, and have one less sick day.")

            return 0

    GameLoop(Locations[index], index)#Loop around according to the index, as stated above.

#There is a special scene that requires its own loop. I leave it to you to guess which one.
def Combat():

    print("\n\n COMBAT WORKS" )

#Okay, make that two scenes. Bosses sure do like to talk, don't they?
def Talk():

    if (Work.selected == Work.optionA):

        print("\n\n\"Hello", Player.name, ".\" says the boss man \"You are late. AGAIN. Get to work now or your fired.\" You look at your watch, and it says 6:30AM. He leaves without saying a word.")

    elif (Work.selected == Work.optionB):

        print("\n\n\" What's wrong?\" the boss says, \"WHATS WRONG>?! LOOK AT THE TIME, IT'S... 6:30 AM. Weird. But anyway you have been late for the past five days. Stop playing games and GET TO WORK!\" He stomps away before you can even respond.")

    elif (Work.selected == Work.optionC):

        print("\n\nYour bosses shakes his head in dissaproval. \"If you are late one more time, you're fired\" he says, and walks away before you can even reply. ")

    elif (Work.selected == Work.optionD):

        print("\n\nThe boss blocks your path and says \"Where do you think YOU'RE going?! GET TO WORK. If you are late one more time, you're fired!\" you slink back into your cubicle as he walks away.")



#This is essentially the GAME OVER SCREEN when you beat the game.
def END():

    print("\n\nYou enter your cubicle. Slumping back into your chair, you can't help but feel exhausted. \nIt's STILL 6:30 AM and you have eight grueling hours to go. \nYour not sure why, but time seems to float away forever in this place. \nNo worries, though. Even in this infinite void of sadness that is your life, there's always one thing you can do. \nYou whip out your headphones and finishing updating your newest copy of LEVELGRINDER RPG. \nYou plug in and log in and enter a world of infinite possibilites. \nAfter all; life would be better if it were a game. \n\n\n ...right?")


GameLoop(Locations[0], 0) #THE GAME BEGINS


#annnd the game ends. Thanks for playing!
print ("\n\nTHE END\n\nIf you want to play more of this game, please send the developer $500.00. \n\nOtherwise, thank you for playing,",Player.name,"!\n")
