# Guess Me game
# game generates random number between 1 to 1000
# user is given chances to guess the number 10 times
from random import randint

max_chance = 10


class Game(object):
    def __init__(self):
        self.user = None
        self.max_chance = max_chance
        self.rv = self.__generate_number()
        self.__compare()

    def __generate_number(self):
        return randint(1, 1000)

    def __compare(self):
        chance = 1
        while chance <= self.max_chance:
            try:
                prompt = "Chance : {}\n Enter the number : "
                self.user = int(raw_input(prompt.format(chance)))
            except ValueError, err:
                print err
                print
                continue
            if self.user < self.rv:
                print 'input is less'
            elif self.user > self.rv:
                print 'input is more'
            else:
                print 'YOU WON !!!'
                break
            chance += 1
            print
        else:
            print 'expected number : ', self.rv
            print 'YOU LOSE :( :( :('

Game()
