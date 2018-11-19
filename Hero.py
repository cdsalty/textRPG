class Hero(object):
    def __init__(self, name):
        self.name = name
        self.health = 10
        # self.health = random.randint(10, 20) ---- if you want random
        self.power = 5
        # self.power = random.randint(1, 5)  --- if you want random
theHero = Hero("Link")
print theHero.power