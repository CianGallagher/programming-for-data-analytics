# Author cian Gallagher
# A python programme that simulates dice battles in the board game Risk, then plots the results.

import numpy as np
import matplotlib.pyplot as plt

battles = 3
attackers = 3
defenders = 2
dice = [1, 2, 3, 4, 5, 6]

seed = 1337
rng = np.random.default_rng(seed)

for battle in range(battles):

    attacker_rolls = sorted(rng.choice(dice, size=attackers), reverse=True)
    defender_rolls = sorted(rng.choice(dice, size=defenders), reverse=True)



    faceoff = list(zip(attacker_rolls, defender_rolls))

    print(f"Battle {battle + 1}:")
    print(f"Attacker rolls: {attacker_rolls}")
    print(f"Defender rolls: {defender_rolls}")
    print("Dice pairs:", faceoff)

    for i, (attacker_single_roll, defender_single_roll) in enumerate(faceoff):
        if attacker_single_roll > defender_single_roll:
            print("Attacker Wins!")
        else:
            print("Defender Wins")


# Probably need another loop - line up the two lists in each index of faceoff and write if statements for Risks' rules of engagement. 
  
# print(attacker_roll)
# print(defender_roll)


