from enum import Enum

class HeroClass (Enum):
    Guerreiro = "Guerreiro"
    Mago = "Mago"
    Monge = "Monge"
    Ninja = "Ninja"

class Hero :
    name:str
    age:int
    type:HeroClass


    def __init__(self, name:str, age:int, type:HeroClass):
        self.name = name
        self.age = age
        self.type = type

    def ataque (self):
        match self.type:
            case HeroClass.Guerreiro:
                typeOfAttack = "espada"
            case HeroClass.Mago:
                typeOfAttack = "magia"
            case HeroClass.Monge:
                typeOfAttack = "artes marciais"
            case HeroClass.Ninja:
                typeOfAttack = "shuriken"     

        print(f"O {self.type.value} atacou usando {typeOfAttack}")   
    
myHero = Hero("Henrique", 30, HeroClass.Guerreiro)
myHero.ataque()
myHero = Hero("Fernado", 31, HeroClass.Mago)
myHero.ataque()
myHero = Hero("Roberto", 32, HeroClass.Monge)
myHero.ataque()
myHero = Hero("Eduardo", 33, HeroClass.Ninja)
myHero.ataque()
