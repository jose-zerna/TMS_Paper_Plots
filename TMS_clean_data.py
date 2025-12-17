import pandas as pd

# Load the CSV file
file = "Figures/Graphana (edits)/DL Throughput - DRB.UEThpDl-data-as-joinbyfield-2025-12-05 12_25_21.csv"

with open(file, 'r') as infile:
    lines = infile.readlines()

with open(file, 'w') as outfile:
    # Skip the first line and write the rest to a new file
    for line in lines[1:]:
        outfile.write(line)

# print(lines)