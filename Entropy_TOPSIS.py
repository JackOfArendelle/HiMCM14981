import pandas as pd
import numpy as np
import os

os.system('cls')

data = pd.read_excel('sport_data_final.xlsx')

# Entropy Weight

normalized_data = data[0:]

mode = input()
if mode != 'test':
    print(normalized_data)
else:
    n_rows, n_cols = normalized_data.shape
    print(n_rows)
    print(n_cols)
    col_sums = normalized_data.sum(axis=0)
    print(col_sums)
    p_matrix = normalized_data / col_sums
    print(p_matrix)
    k = 1.0 / np.log(n_rows)
    entropy = -k * ((p_matrix * np.log(p_matrix + 1e-10)).sum(axis=0))
    print("Entropy：\n", entropy)
    entropy_df = pd.DataFrame([entropy], columns=normalized_data.columns)
    entropy_df.index = ['Entrophy']
    # entropy_df.to_excel("data_final_entropy.xlsx")
    # print("Entropy Saved")

    redundancy = 1 - entropy
    print("Entropy Redundancy：\n", redundancy)
    redundancy_df = pd.DataFrame([redundancy], columns=normalized_data.columns)
    redundancy_df.index = ['Redundancy']
    # redundancy_df.to_excel("data_final_redundancy.xlsx", index=True)
    # print("Entropy Redundancy Saved")

    weights = redundancy / redundancy.sum()
    print("Weight：\n", weights)

    weights_df = pd.DataFrame([weights], columns=normalized_data.columns)
    weights_df.index = ['Weight']
    weights_df.to_excel("data_final_weight.xlsx", index=True)
    print("Weight Saved")

    max_values = normalized_data.max()
    min_values = normalized_data.min()
    extreme_values = pd.DataFrame([max_values, min_values], index=['Max', 'Min'])
    print(extreme_values)
    # extreme_values.to_excel("data_final_extreme.xlsx", index=True)
    # print("Max and Min Value Saved")

    # TOPSIS

    normalized_data = data

    distances_to_max = np.sqrt((((normalized_data - max_values) ** 2)*weights).sum(axis=1))
    distances_to_min = np.sqrt((((normalized_data - min_values) ** 2)*weights).sum(axis=1))
    normalized_data['Dis2Max'] = distances_to_max
    normalized_data['Dis2Min'] = distances_to_min
    print("Data With Distance：\n", normalized_data)
    # normalized_data.to_excel("data_final_distance.xlsx", index=True)
    # print("Per Row Max and Min Saved")
    scores = distances_to_min / (distances_to_min + distances_to_max)
    normalized_data['Unnormalized_score'] = scores

    print("Unnormalized Score：\n", scores)
    # normalized_data.to_excel("data_final_unnormalized_score.xlsx", index=True)
    # print("Unnormalized Score Saved")

    scores2 = scores / scores.sum()
    normalized_data['Normalized_score'] = scores2

    print("Normalized Score：\n", scores2)
    normalized_data.to_excel("data_final_normalized_score.xlsx", index=True)
    print("Normalized Score Saved")