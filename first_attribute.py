class Critter(object):
    def __init__(self, name):
        print('a new animal was born')
        self.name = name

    def __str__(self):
        rep = 'class object Critter\n'
        rep += 'name:' + self.name + '\n'
        return rep

    def talk(self):
        print('Hi! My name', self.name, '\n')

crit1 = Critter('Bob')
crit1.talk()
crit2 = Critter('Mur')
crit2.talk()
print('crit1: ')
print(crit1)
print('crit1.name: ')
print(crit1.name)
input('Press enter')