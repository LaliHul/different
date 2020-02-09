class Critter(object):
    def __init__(self, name, mood):
        print('a new animal was born')
        self.name = name            # public attribute
        self.__mood = mood          # private attribute

    def talk(self):
        print( '\n', 'my name is', self.name)
        print('now I feel like', self.__mood, '\n')


    def __private_method(self):
        print('this is a closed method')

    def public_method(self):
        print('this is an open method')
        self.__private_method()

crit = Critter(name = 'Bob', mood = 'good')
crit.talk()
crit.public_method()
