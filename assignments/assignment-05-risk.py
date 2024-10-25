# Author cian Gallagher
# A python programme that simulates dice battles in the board game Risk, then plots the results.

import numpy as np
import matplotlib.pyplot as plt

battles = 10
attackers = 3
defenders = 2
dice = [1, 2, 3, 4, 5, 6]

seed = 1337
rng = np.random.default_rng(seed)

faceoff = []

for battle in range(battles):

    attacker_roll = sorted(rng.choice(dice, size=attackers), reverse=True)
    defender_roll = sorted(rng.choice(dice, size=defenders), reverse=True)

    faceoff.append((attacker_roll, defender_roll))


# Probably need another loop - line up the two lists in each index of faceoff and write if statements for Risks' rules of engagement. 

# print(faceoff)
print(faceoff[0])
# print(type(faceoff))
