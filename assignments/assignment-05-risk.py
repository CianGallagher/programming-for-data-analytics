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

attacker_losses = []
defender_losses = []

for battle in range(battles):

    attacker_rolls = sorted(rng.choice(dice, size=attackers), reverse=True)
    defender_rolls = sorted(rng.choice(dice, size=defenders), reverse=True)

    attacker_losses_round = 0
    defender_losses_round = 0

    faceoff = list(zip(attacker_rolls, defender_rolls))

    # print(f"Battle {battle + 1}:")
    # print(f"Attacker rolls: {attacker_rolls}")
    # print(f"Defender rolls: {defender_rolls}")
    # print("Dice pairs:    ", faceoff)

    for i, (attacker_single_roll, defender_single_roll) in enumerate(faceoff):
        if attacker_single_roll > defender_single_roll:
            print("Attacker Wins!")
            defender_losses_round += 1
        else:
            print("Defender Wins")
            attacker_losses_round += 1
    
    attacker_losses.append(attacker_losses_round)
    defender_losses.append(defender_losses_round)

print(attacker_losses)
print(defender_losses)
