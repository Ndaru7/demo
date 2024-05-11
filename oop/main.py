class Hero:
    health = 100

    def take_dmg(self,damage):
        self.health -= damage


hero1 = Hero()
hero1.take_dmg(59)
print(hero1.health)
