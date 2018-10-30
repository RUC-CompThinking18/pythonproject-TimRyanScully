from Dice import Dice
from Character import *
from GM import *

hero = Character("Ryan Robot")

gizmo = Item("gizmo")

gizmo.Taken(hero)

print (gizmo.owner.name + " has a " + gizmo.name)

gizmo.Equip()

if (gizmo.equipped == True):

    print (gizmo.owner.name + " equipped " + gizmo.name)


gizmo.Weapon(4, 5)

awesomeness = Ability("awesomeness", 1)

villain = Character("Robodemon")
villain.HP(15)
villian.AC(10)



if (hero.Attack(villian, 0, awesomeness, 0) == True):

    print(hero.name + " hits " + villian.name + " for " + hero.damage + " damage!\n " + villian.name + " has " + villian.hp + " HP.")
