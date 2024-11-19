import os
import matplotlib.pyplot as plt
import numpy as np
import csv

os.system('cls')

factors = ["TI", "GR", "PY", "OT", "AG", "VS", "IR", "AR", "CI", "CT"]

score_changes_S = []
with open("sport_SA.csv", "r", encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        for i in range(len(row)):
            score_changes_S.append(float(row[i]))

score_changes_S = [round(num*100.0, 2) for num in score_changes_S]

print("Sport : ", score_changes_S)

score_changes_D = []
with open("discipline_SA.csv", "r", encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        for i in range(len(row)):
            score_changes_D.append(float(row[i]))

score_changes_D = [round(num*100.0, 2) for num in score_changes_D]

print("Discipline : ", score_changes_D)

# Plot

bar_width = 0.35
index = np.arange(len(factors))

plt.figure(figsize=(10, 6))

cmap_S = plt.get_cmap('Blues')
cmap_D = plt.get_cmap('Greens')

plt.bar(index, score_changes_S, bar_width, label='Sport', color=[cmap_S((i+10)/(len(index)+20)) for i, _ in enumerate(index)])
plt.bar(index + bar_width, score_changes_D, bar_width, label='Discipline', color=[cmap_D((len(index)+10-i)/(len(index)+20)) for i, _ in enumerate(index)])

plt.legend(fontsize = 'x-large')

for i, v in enumerate(score_changes_S):
    plt.text(i - 0.1 * bar_width, v + 0.0001, str(v)+'%', ha='center', va='bottom', color='black',fontsize=12)
for i, v in enumerate(score_changes_D):
    plt.text(i + 1.1 * bar_width, v + 0.0001, str(v)+'%', ha='center', va='bottom', color='black',fontsize=12)

plt.xlabel('Factors', fontsize=30)
plt.ylabel('Sensitivity (%)', fontsize=30)
plt.title('Sensitivity Analysis of Factors in Entropy Weight-TOPSIS', fontsize=30)
plt.xticks(index + bar_width / 2, factors, fontsize=20)
plt.yticks(fontsize=20)
plt.tight_layout()
plt.show()