import os
import csv
import pandas

os.system('cls')

cntM = 0
cntF = 0

with open("data/athlete_events.csv", "r", encoding='utf-8') as file:
    rows = csv.reader(file)
    for row in rows:
        if row[13].find("Swimming") != -1:
            if row[2] == 'M':
                cntM += 1
            elif row[2] == 'F':
                cntF += 1

print(f"Male : {cntM}, Female : {cntF}")