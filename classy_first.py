class Critter(object):
    total = 0 
    @staticmethod
    def status():
        print('total animals now', Critter.total)
    
    def __init__(self, name):
        print('a new animal was born')
        self.name = name
        Critter.total += 1 

print('find the value of the class attribute Critter.total:', end=' ')
print(Critter.total)
print('creating animals')
crit1 = Critter('animal 1')
crit2 = Critter('animal 2')
crit3 = Critter('animal 3')
Critter.status()
print('accessing the class attribute via an object:', end=' ')
print(Critter.total)
input('press enter')