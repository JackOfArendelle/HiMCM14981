import pandas as pd
import numpy as np
import os
import statistics
import matplotlib.pyplot as plt
import csv

os.system('cls')

data = pd.read_excel('sport_data_final.xlsx')

normalized_data = data[0:]

# mode = input("Enter 'test' for sensitivity analysis: ")
mode = 'test'

if mode != 'test':
    print(normalized_data)
else:
    # Entropy
    n_rows, n_cols = normalized_data.shape
    col_sums = normalized_data.sum(axis=0)
    p_matrix = normalized_data / col_sums
    k = 1.0 / np.log(n_rows)
    entropy = -k * ((p_matrix * np.log(p_matrix + 1e-10)).sum(axis=0))
    redundancy = 1 - entropy
    weights = redundancy / redundancy.sum()

    # Max and Min
    max_values = normalized_data.max()
    min_values = normalized_data.min()

    # TOPSIS
    distances_to_max = np.sqrt((((normalized_data - max_values) ** 2) * weights).sum(axis=1))
    distances_to_min = np.sqrt((((normalized_data - min_values) ** 2) * weights).sum(axis=1))
    scores = distances_to_min / (distances_to_min + distances_to_max)

    # Sensitivity Analysis
    score_changes = []

    for i in range(10):
        # Perturb Value
        perturbed_data = normalized_data.copy()
        perturbed_data.iloc[:,i] = normalized_data.iloc[:,i] * 1.10

        # Calculate Distance and Score
        distances_to_max = np.sqrt((((perturbed_data - max_values) ** 2) * weights).sum(axis=1))
        distances_to_min = np.sqrt((((perturbed_data - min_values) ** 2) * weights).sum(axis=1))
        perturbed_scores = distances_to_min / (distances_to_min + distances_to_max)
        score_changes.append(statistics.mean(perturbed_scores - scores))

    with open("sport_SA.csv", "w", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(score_changes)