import random
import math

class Vampire:
    
    hp = 100
    mp = 25
    status = 'OK'

    def __init__(self,
                 name:str,
                 height:float) -> None:
        self.name = name
        self.height = height
    
    def take_damage(self, x:float) -> None:
        self.hp -= x
        if self.hp <= 0:
            print('Felicidades, has vencido al vampiro')
    
    def leech_blood(self, target) -> None:
        dmg = random.randint(1,8)
        target.take_damage(dmg)
        self.hp += math.floor(dmg/2)
        print(f'Golpeas por {dmg} y te curas {math.floor(dmg/2)}')
    
    def hypnosis(self, target) -> None:
        if self.mp >= 5:
            self.mp -= 5
            target.set_status('confusion')
            print('El objetivo esta confundido')
        else:
            print('El vampiro se queda mirando con la mirada perdida')
    
    def attack(self,target) -> None:
        if self.status=='confusion':
            dice = random.randint(1,20)
            if dice >=17:
                dmg = random.randint(5,20)
                target.take_damage(dmg)
                print(f'{self.name} golpea a {target.name} por {dmg} de daño')
            else:
                dmg = random.randint(5,20)
                self.take_damage(dmg)
                print(f'{self.name} se golpea por {dmg} de daño')
    
    ## Darle las acciones que quieran

class Person:

    possible_weapons = ['sword','axe']
    status = 'OK'

    def __init__(self, name:str, weapon:str) -> None:
        self.name = name
        if weapon not in self.possible_weapons:
            raise ValueError('El arma debe ser sword o axe')
        self.weapon = weapon
        self.atk = 10 if self.weapon=='axe' else 8
        self.hp = 80 if  self.weapon=='axe' else 85

    def take_damage(self, x:float) -> None:
        self.hp -= x
        if self.hp <= 0:
            print('C Murió :c')

    def set_status(self, status:str):
        self.status = status
    
    ## Darle las acciones que quieran

if __name__ == '__main__':

    print('bienvenido a la aventura')
    player_name = input('dime tu nombre: ')
    weapon = None
    
    while weapon not in ['sword','axe']:
        print('puedes usar una espada o un hacha')
        print('ingresa la opcion que prefieras')
        print('1. Espada')
        print('2. Hacha')
        weapon_choice = input('ingresa el numero: ')
        if str(weapon_choice) == '1':
            weapon = 'sword'
        elif str(weapon_choice) == '2':
            weapon = 'axe'
        else:
            weapon= 'INVALID LOL'
    
    player = Person(player_name, weapon)
    print(f'Eres {player.name} y cargas una {player.weapon}')
    print('Caminas por la ciudad y ves una figura misteriosa')

    ## Instanciar un vampiro
    ## Presentar en texto

    # Gameplay loop
    # while player.hp>0 and vampire.hp>0:

    # Menu input
    #tomar la accion del rival

    
