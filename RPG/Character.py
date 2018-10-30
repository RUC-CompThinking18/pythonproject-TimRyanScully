from Dice import Dice

class Character(object):

    def __init__(self, name):

        self.name = str(name)

    def HP(self, hp):

        self.hp = int(hp)

    def AC(self, ac):

        self.ac = int(ac)

    def Level(self, level):

        self.level = int(level)

    def XP(self, xp):

        self.xp = int(xp)

    def Money(self, money):

        self.money = int(money)

    def SkillCheck(self, skill, ability, DC):

        roll= Dice(1, 20, skill.mod + ability.mod)

        if (roll.Check(DC) == True):

            return True

        else:

            return False

    def Attack(self, other, ability,):

        roll = Dice(1, 20, self.attack + ability.mod)

        if (roll.Check(other.ac) == True):

            self.Damage(other)

            return True

        else:

            return False

    def Damage(self, other):

            other.hp -= self.damage

class Ability(object):

    def __init__(self, name, mod):

        self.name = name

        self.mod = int(mod)

class Skill(object):

    def __init__(self, name, mod):

        self.name = name

        self.mod = int(mod)
