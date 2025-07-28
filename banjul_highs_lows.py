import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = 'data/banjul.csv' # file directory
with open(filename) as f: # Open file as f
    reader = csv.reader(f) # reading the entire
    header_row = next(reader) # getting the first line
    
    # for index, column_row in enumerate(header_row):
    #     print(index, column_row)
    dates, temp_maxs, temp_mins = [], [], []
    for row in reader:
        date = datetime.strptime(row[1], '%Y-%m-%d')
        t_max = int(float(row[2]))  # Covert the str to  float and then to int
        t_min = int(float(row[3]))
        dates.append(date)
        temp_maxs.append(t_max) # append temp max values
        temp_mins.append(t_min)

    plt.style.use('seaborn-v0_8-deep')
    fig, ax = plt.subplots()
    ax.plot(dates, temp_maxs, c='green', alpha=0.5) # set the plot
    ax.plot(dates, temp_mins, c='red', alpha=0.5)

    plt.title("Daily High and Low Temperatures in Banjul\n(July–August) 2025", fontsize=18)
    plt.xlabel('', fontsize=12)
    fig.autofmt_xdate()
    plt.fill_between(dates, temp_maxs, temp_mins, facecolor='green', alpha=0.1)
    plt.ylabel('Temperature (F)', fontsize=12)
    plt.tick_params(axis='both',  which='major', labelsize=12, color='blue')

    plt.show()
    # plt.savefig('images/banjul_tem_max_min_trans.png', bbox_inches="tight", edgecolor='none')


