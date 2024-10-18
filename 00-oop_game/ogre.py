import random
from enemy import *

class Ogre(Enemy):
    def __init__(self,health_points,attack_damage):
        super().__init__(type_of_enemy='Ogre',
                         health_points=health_points,
                         attack_damage=attack_damage)

    def talk(self):
        print('Ogre is slamming hands all around.')
    def special_attack(self):
        did_special_attack_work=random.random()<.20
        if did_special_attack_work:
            self.attack_damage+=4
            print('Ogre attack has increased by 4!')
