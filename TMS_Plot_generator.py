import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the CSV file
file_path = "Figures/Graphana (edits)/DL Throughput - DRB.UEThpDl-data-as-joinbyfield-2025-12-05 12_25_21.csv"
df = pd.read_csv(file_path, skiprows=1)

df.columns = ['Time', 'value gNb-1-C1', 'value gNb-3-C2', 'value gNb-6-C3']

# Convert 'Time' from epoch milliseconds to datetime
df['Time'] = pd.to_datetime(df['Time'], unit='ms')
df['TimeStr'] = df['Time'].dt.strftime('%H:%M:%S')

# Rename value columns for shorter labels
df.rename(columns={
    'value gNb-1-C1': 'gNb-1-C1',
    'value gNb-3-C2': 'gNb-3-C2',
    'value gNb-6-C3': 'gNb-6-C3'
}, inplace=True)

plt.figure(figsize=(10, 5))
plt.plot(df['Time'], df['gNb-1-C1'], label='gNb-1-C1', color='tab:blue')
plt.plot(df['Time'], df['gNb-3-C2'], label='gNb-3-C2', color='tab:orange')
plt.plot(df['Time'], df['gNb-6-C3'], label='gNb-6-C3', color='tab:green')

plt.xlabel("Time", fontsize=12)
plt.ylabel("Throughput (kbps)", fontsize=12)
plt.title("Downlink Throughput (DRB.UEThpDl)", fontsize=13)
plt.legend(fontsize=10)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))  # HH:MM:SS format
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())            # auto spacing
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)

plt.grid(True, which='major', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()
