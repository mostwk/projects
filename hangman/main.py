import random
from hangman.functions import *

random_word = random.choice(open("sample.txt").read().split('\n'))

game(random_word)

