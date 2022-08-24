import random

class Monster:
    alive = True
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk
    
    def take_damage(self, dmg):
        self.hp -= dmg
    
    def attack(self, target):
        dmg = random.randint(self.atk-5, self.atk)
        target.take_damage(dmg)

class Dragon(Monster):
    def __init__(self,hp=200,atk=15):
        super().__init__(hp,atk)
    
    def breathe_fire(self,target):
        target.take_damage(25)

class Goblin(Monster):
    def __init__(self,hp=20,atk=5):
        super().__init__(hp,atk)   

class LizardWizard(Monster):
    mp = 25
    
    def __init__(self,hp=85,atk=8):
        super().__init__(hp,atk)
    
    def fire_bolt(self,target):
        if self.mp >= 5:
            dmg = random.randint(10,30)
            target.take_damage(dmg)
            self.mp -=5
        else:
            pass
    
    def mp_to_hp(self):
        if self.mp >=10:
            self.mp -= 10
            self.hp += 10
        else:
            pass

class Bunny(Monster):
    def __init__(self, hp=10, atk=0):
        super().__init__(hp, atk)
    
    def attack(self, target):
        print('this unit cant attack')

