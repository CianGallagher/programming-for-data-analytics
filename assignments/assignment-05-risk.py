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

attacker_turns = []
defender_turns = []

for battle in range(battles):

    defender_roll = []
    attacker_roll = []

    dice_roll = rng.choice(dice)
    attacker_roll.append(dice_roll)
    dice_roll = rng.choice(dice)
    attacker_roll.append(dice_roll)
    dice_roll = rng.choice(dice)
    attacker_roll.append(dice_roll)

    attacker_turns.append(attacker_roll)

    dice_roll = rng.choice(dice)
    defender_roll.append(dice_roll)
    dice_roll = rng.choice(dice)
    defender_roll.append(dice_roll)

    defender_turns.append(defender_roll)

    defender_roll = []
    attacker_roll = []   


print(attacker_turns)
print(defender_turns)
