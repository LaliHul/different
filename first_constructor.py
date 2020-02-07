class Critter(object):
    def __init__(self):
        print('a new animal was born')
    def talk(self):
        print("hi! I'm an animal instance of the Critter class")

crit1 = Critter()
crit2 = Critter()
crit1.talk()
crit2.talk()
input('press enter')