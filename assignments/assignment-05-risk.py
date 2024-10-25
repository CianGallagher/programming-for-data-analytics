# Author cian Gallagher
# A python programme that simulates dice battles in the board game Risk, then plots the results.

import numpy as np
import matplotlib.pyplot as plt

battles = 1
attackers = 3
defenders = 2
dice = [1, 2, 3, 4, 5, 6]

seed = 1337
rng = np.random.default_rng(seed)

faceoff = []

for battle in range(battles):

    attacker_roll = rng.choice(dice, size=attackers)
    defender_roll = rng.choice(dice, size=defenders)

    faceoff.append((attacker_roll, defender_roll))

print(faceoff)
# print(attacker_turns)
# print(defender_turns)
