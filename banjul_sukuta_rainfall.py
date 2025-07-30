import csv

import matplotlib.pyplot as plt

from datetime import datetime

# Formatting banjul data
banjul_filename = 'data/banjul.csv'
with open(banjul_filename) as bf:
    b_reader = csv.reader(bf)
    b_header = next(b_reader)

    
    # Get the readers cols values
    b_dates, b_rainfalls = [], []
    for row in b_reader:
        b_current_date = datetime.strptime(row[1], "%Y-%m-%d")
        try:
            b_rain = float(row[10]) # Get the precip 
        except ValueError:
            print(f"Misssing data for {b_current_date}")
        else:
            b_dates.append(b_current_date)
            b_rainfalls.append(b_rain)
        
# Formatting Sukuta data
sukuta_filename = 'data/sukuta.csv'
with open(sukuta_filename) as sf:
    s_reader = csv.reader(sf)
    s_header = next(s_reader)

    # for index, s_col_row in enumerate(s_header):
    #     print(index, s_col_row)

    # Get the readers cols values
    s_dates, s_rainfalls = [], []
    for row in s_reader:
        s_current_date = datetime.strptime(row[1], "%Y-%m-%d")
        try:
            s_rain = float(row[10])  # Get the precip
        except ValueError:
            print(f"Misssing data for {s_current_date}")
        else:
            s_dates.append(s_current_date)
            s_rainfalls.append(s_rain)

    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots()
    fig.autofmt_xdate()
    # Plot bajul data
    ax.plot(b_dates, b_rainfalls, c='red', label="Banjul",
            alpha=0.5, marker='o', linewidth=2)

    # Plot sukuta data
    ax.plot(s_dates, s_rainfalls, c='green', label="Sukuta",
            alpha=0.5, marker='o', linewidth=2)
        
    ax.legend()
    ax.set_ylim()

    plt.title("Daily Rainfall: Banjul vs Sukuta\nJuly-August 2025", fontsize=18)
    plt.xlabel('', fontsize=16)
    plt.ylabel("Rain Fall (F)", fontsize=16)
    plt.tick_params(axis='both',  which='major', labelsize=12, color='blue')

    plt.savefig('images/banjul_sukuta_rainfall_light.png')
    plt.show()
