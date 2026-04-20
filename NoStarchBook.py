import csv
import matplotlib.pyplot as plt

filename = '/Users/drewwhitting/Documents/VSCodePython/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)

    #for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

ax.set_title("Daily high temps, JUL 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temp (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()


#print(plt.style.available)