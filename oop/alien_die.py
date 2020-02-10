#alien die

class Player(object):
    def blast(self, enemy):
        print('the player shoots the alien\n')
        enemy.die()

class Alien(object):
    def die(self):
        print('man may have won this battle, but next time we will take over this miserable planet\n')

print('\t\tDie alien\n')
hero = Player()
invader = Alien()
hero.blast(invader)
input('press enter')