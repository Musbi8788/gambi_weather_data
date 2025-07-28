import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = 'data/banjul.csv' # file directory
with open(filename) as f: # Open file as f
    reader = csv.reader(f) # reading the entire
    header_row = next(reader) # getting the first line
    
    # for index, column_row in enumerate(header_row):
    #     print(index, column_row)
    dates, temp_max = [], []
    for row in reader:
        date = datetime.strptime(row[1], '%Y-%m-%d')
        temp = int(float(row[2]))  # Covert the str to  float and then to int
        dates.append(date)
        temp_max.append(temp) # append temp max values

    plt.style.use('seaborn-v0_8-deep')
    fig, ax = plt.subplots()
    ax.plot(dates, temp_max, c='green') # set the plot

    plt.title("High Temperatures in Banjul (July–August) 2025", fontsize=18)
    plt.xlabel('', fontsize=12)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=12)
    plt.tick_params(axis='both',  which='major', labelsize=12, color='blue')

    # plt.show()
    plt.savefig('images/banjul_tem.png', bbox_inches="tight", edgecolor='none')


