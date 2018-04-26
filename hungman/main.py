import random
from hungman.functions import *

random_word = random.choice(open("sample.txt").read().split('\n'))

game(random_word)

