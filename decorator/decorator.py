class Marine:
    def __init__(self, damage, armor):
        #your code here
        self.damage = damage
        self.armor = armor

class Marine_weapon_upgrade:
    def __init__(self, marine):
        #your code here
        self.damage = marine.damage + 1
        self.armor = marine.armor

class Marine_armor_upgrade:
    def __init__(self, marine):
        #your code here
        self.damage = marine.damage
        self.armor = marine.armor + 1