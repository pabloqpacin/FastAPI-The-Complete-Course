class Enemy:
    def __init__(self,type_of_enemy,health_points=10,attack_damage=1):
        self.__type_of_enemy=type_of_enemy  # private: can't be changed when instanciated (encapsulation)
        self.health_points=health_points    # public: can be changed when instanciated
        self.attack_damage=attack_damage    # "
    def get_type_of_enemy(self):
        return self.__type_of_enemy
    # def set_type_of_enemy(self,type_of_enemy):
    #     self.__type_of_enemy=type_of_enemy

    def talk(self):
        print(f'I am a {self.__type_of_enemy}. Be prepared to fight.')
    def walk_forward(self):
        print(f'{self.__type_of_enemy} moves closer to you.')
    def attack(self):
        print(f'{self.__type_of_enemy} attacks for {self.attack_damage} damage.')
    def special_attack(self):
        print(f'Enemy has no special attack')
