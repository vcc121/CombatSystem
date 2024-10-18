import random

class Character(object):
    def __init__(self, name="Unknown", hitPoints=0, hitChance=0, maxDamage=0, armor=0):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor
     
    def testInt(self, value, min = 0, max = 100, default = 0):
        """ takes in value 
            checks to see if it is an int between
            min and max.  If it is not a legal value
            set it to default """

        out = default

        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value 
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an int")

        return out
     

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def hitPoints(self):
        return self._hitPoints
    
    @hitPoints.setter
    def hitPoints(self, value):
        value = self.testInt(value, 0, 1000, 0)
        self._hitPoints = value
        
    @property
    def hitChance(self):
        return self._hitChance
    
    @hitChance.setter
    def hitChance(self, value):
        value = self.testInt(value, 0, 100, 0)
        self._hitChance = value
    
    @property
    def maxDamage(self):
        return self._maxDamage
    
    @maxDamage.setter
    def maxDamage(self, value):
        value = self.testInt(value, 0, 1000, 0)
        self._maxDamage = value
    
    @property
    def armor(self):
        return self._armor
    
    @armor.setter
    def armor(self, value):
        value = self.testInt(value, 0, 1000, 0)
        self._armor = value
        
    def printStats(self):
        print(f"""
        {self.name}
        ===================
        Hit points: {self.hitPoints}
        Hit chance: {self.hitChance}
        Maximum damage: {self.maxDamage}
        Armor rating: {self.armor}
            """)
    
    def hit(self, enemy):
        if random.randint(1, 100) <= self.hitChance:
            print(f"{self.name} hits {enemy.name}...")
            damage = random.randint(1, self.maxDamage)
            print (f"for {damage} damage.")
            damage -= enemy.armor
            if enemy.armor > 0:
                print(f"{enemy.name}'s armor absorbs {enemy.armor} points")
            enemy.hitPoints -= damage
        else:
            damage = 0
            print(f"{self.name} missed, dealing {damage} damage.")
        return damage

def basicFight(player1,player2):
    keepGoing = True
    while keepGoing:
        player1.hit(player2)
        player2.hit(player1)
        
        print(f"{player1.name} HP: {player1.hitPoints}")
        print(f"{player2.name} HP: {player2.hitPoints}")
        print()
        
        if player1.hitPoints <= 0:
            print (f"{player1.name} loses.")
            keepGoing = False
        if player2.hitPoints <= 0:
            print (f"{player2.name} loses.")
            keepGoing = False
         