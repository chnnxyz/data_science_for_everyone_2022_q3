import random
import math
import time

class Vampire:
    
    hp = 100
    mp = 25
    status = 'OK'
    active_turn = True

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
        print(f'Golpea por {dmg} y te curas {math.floor(dmg/2)}')
        self.set_turn_activity(False)
    
    def hypnosis(self, target) -> None:
        if self.mp >= 5:
            self.mp -= 5
            target.set_status('confusion')
            print('El objetivo esta confundido')
        else:
            print('El vampiro se queda mirando con la mirada perdida')
        self.set_turn_activity(False)
    
    def attack(self,target) -> None:
        if self.status=='confusion':
            dice = random.randint(1,20)
            if dice >=10:
                dmg = random.randint(5,20)
                target.take_damage(dmg)
                print(f'{self.name} golpea a {target.name} por {dmg} de daño')
            else:
                dmg = random.randint(5,20)
                self.take_damage(dmg)
                print(f'{self.name} se golpea por {dmg} de daño')
        self.set_turn_activity(False)
    
    ## Darle las acciones que quieran
    def set_turn_activity(self, activity) -> None:
        self.active_turn = activity

class Person:

    possible_weapons = ['sword','axe']
    status = 'OK'
    potions = 2
    active_turn = True #Determina si te toca o le toca al oponente
    safe = False 

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
    def set_turn_activity(self, activity) -> None:
        self.active_turn = activity

    def attack(self, target) -> None:
        # Genera daño aleatorio cercano a su daño base
        dmg = random.randint(self.atk - 5, self.atk + 5)
        # Genera posibilidad de golpe critico
        dice = random.randint(1,20)
        dmg = 2 * dmg if dice==20 else dmg
        if self.status=='confusion':
            dice2 = random.randint(1,20)
            if dice2 >= 10:          
                print(f'golpeas a {target.name} por {dmg}')
                target.take_damage(dmg)
            else:
                self.take_damage(dmg)
                print(f'{self.name} se golpea por {dmg} de daño')

        self.set_turn_activity(False)
    
    def drink_potion(self) -> None:
        if self.potions >= 0:
            dice1 = random.randint(1,4)
            dice2 = random.randint(1,4)
            heal = dice1 + dice2 + 2
            self.hp += heal
            print(f'te curas {heal} ahora tu hp es de {self.hp}')
            self.set_turn_activity(False)
        else:
            print('Buscas en tu mochila una pocion')
            time.sleep(2)
            print('Pierdes tu turno por no saber manejar tu inventario')
    
    def check_inventory(self):
        print(f'tienes {self.potions} pociones')
    
    def escape(self) -> None:
        # Tira un dado para ver si escapas
        dice = random.randint(1,20)
        if dice == 20:
            self.safe = True
            print('Te escapas')
        else:
            print('Tratas de correr, pero tu oponente sabe correr como naruto')

def change_turns(player,vampire):
    player.active_turn = not player.active_turn
    vampire.active_turn = not vampire.active_turn


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
    time.sleep(1)
    print(f'Eres {player.name} y cargas una {player.weapon}')
    print('Caminas por la ciudad y ves una figura misteriosa')

    #instanciar y presentar un vampiro
    vampire_names = ['Dio','Kars','Wamu','Santana']
    vampire_heights = [120, 170, 180, 190, 200, 210]
    vampire_name = random.choice(vampire_names)
    vampire_height = random.choice(vampire_heights)

    vampire = Vampire(vampire_name, vampire_height)
    time.sleep(1)
    print(f'Ves una figura a la distancia, parece medir {vampire.height} cm')
    time.sleep(3)
    print(f'SOY {vampire.name.upper()} Y VENGO A CHUPAR TU SANGRE Y ROBAR TUS VACAS')
    
    # Preparar el combate
    time.sleep(2)
    print('\n\n')
    print('Te preparas para luchar')

    time.sleep(1)
    #define quien inicia
    coin = random.randint(1,2)
    if coin == 1:
        player.set_turn_activity(True)
        vampire.set_turn_activity(False)
    else:
        player.set_turn_activity(False)
        vampire.set_turn_activity(True)
    
    # Checa que ambos sigan con vida o el jugador no haya escapado
    while player.hp > 0 and vampire.hp > 0 and not player.safe:
        while player.active_turn:
            print('#'*80)
            print(f'Tu HP: {player.hp}')
            print(f'HP de tu rival: {vampire.hp}')
            print(f'#'*80)

            actions = [1,2,3,4]
            action = 0
            while action not in actions:
                print('\n')
            
                print('Elige tu accion')
                print(f'1. Atacar'+ ' '*20 +'2. Tomar pocion')
                print(f'3. Escapar'+ ' '*20 +'4. Checar inventario')

                action = int(input('Que quieres hacer? '))
            
            if action == 1:
                player.attack(vampire)
            elif action == 2:
                player.drink_potion()
            elif action == 3:
                player.escape()
            else:
                player.check_inventory()
        
        while vampire.active_turn:
            print('#'*80)
            print(f'Tu HP: {player.hp}')
            print(f'HP de tu rival: {vampire.hp}')
            print(f'#'*80)
            print('\n')
            dice = random.randint(1,20)
            if dice <= 12:
                vampire.attack(player)
            elif dice <=17:
                vampire.leech_blood(player)
            else:
                vampire.hypnosis(player)

        vampire.set_turn_activity(not vampire.active_turn)
        player.set_turn_activity(not player.active_turn)
    
    if vampire.hp <= 0:
        print('Venciste al vampiro')
    elif player.safe:
        print('Escapaste del vampiro')
    else:
        print('Perdiste')

