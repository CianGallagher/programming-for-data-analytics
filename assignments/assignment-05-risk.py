# Author cian Gallagher
# A python programme that simulates dice battles in the board game Risk, then plots the results.

import numpy as np
import matplotlib.pyplot as plt

battles = 1000
attackers = 3
defenders = 2
seed = 1337
rng = np.random.default_rng(seed)

total_attacker_losses = 0
total_defender_losses = 0

for _ in range(battles):
    attacker_rolls = sorted(rng.integers(1, 7, size=attackers), reverse=True)
    defender_rolls = sorted(rng.integers(1, 7, size=defenders), reverse=True)

    attacker_losses = 0
    defender_losses = 0

    faceoff = zip(attacker_rolls, defender_rolls)
    
    for attacker_roll, defender_roll in faceoff:
        if attacker_roll > defender_roll:
            defender_losses += 1
        else:
            attacker_losses += 1

    total_attacker_losses += attacker_losses
    total_defender_losses += defender_losses

average_attacker_losses = total_attacker_losses / battles
average_defender_losses = total_defender_losses / battles

plt.figure(figsize=(8, 6))

labels = ['Attacker', 'Defender']
averages = [average_attacker_losses, average_defender_losses]

plt.bar(labels, averages, color=['#D81B60', '#1E88E5'], edgecolor='black', hatch=['//', '\\'])
plt.ylabel('Average Troops Lost')
plt.title('Average Troops Lost per Risk Battle Simulation')
plt.grid(axis='y', linestyle='--')

plt.show()

