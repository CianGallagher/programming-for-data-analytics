# Author cian Gallagher
# A python programme that simulates the board game risk and plotting the results.

import numpy as np
import matplotlib.pyplot as plt

battles = 10
attackers = 3
defenders = 2
dice = [1, 2, 3, 4, 5, 6]

seed = 1337
rng = np.random.default_rng(seed)

dice_roll = rng.choice(dice)

attacker_rolls = []
defender_rolls = []

for battle in range(battles):
    print(dice_roll)
    attacker_rolls.append(dice_roll)
    defender_rolls.append(dice_roll)

print(attacker_rolls)
print(defender_rolls)
