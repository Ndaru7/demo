#Latihan encapsulasi
class Hero:

    __jumlah = 0

    def __init__(self,name,health,power,armor):
        self.__name = name
        self.__baseHealth = health
        self.__basePower = power
        self.__baseArmor = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__baseHealth * self.__level
        self.__power = self.__basePower * self.__level
        self.__armor = self.__baseArmor * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return f"{self.__name}(level {self.__level}): \n\thealth = {self.__health}/{self.__healthMax} \n\tattack = {self.__power} \n\tarmor = {self.__armor}"

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(f"{self.__name} level up!")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__baseHealth * self.__level
            self.__power = self.__basePower * self.__level
            self.__armor = self.__baseArmor * self.__level

    def attack(self,musuh):
        self.gainExp = 50


antareja = Hero("Antareja", 100, 15, 20)
antasena = Hero("Antasena", 100, 15, 20)
print(antareja.info)

antareja.attack(antasena)
antareja.attack(antasena)
antareja.attack(antasena)
print(antareja.info)
