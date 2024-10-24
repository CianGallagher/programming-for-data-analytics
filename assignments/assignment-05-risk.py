# Author cian Gallagher
# A python programme that simulates the board game risk and plotting the results.

import numpy as np
import matplotlib.pyplot as plt

battles = 1000
attackers = 3
defenders = 2
dice = [1, 2, 3, 4, 5, 6]

seed = 1337
rng = np.random.default_rng(seed)

dice_roll = rng.choice(dice)

attacker_rolls = ([])
defender_rolls = ([])

print(dice_roll)