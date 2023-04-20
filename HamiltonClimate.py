import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None)
# This loads the data , Hamilton Temps
database = pd.read_csv("hamilton_climate_2022.csv")
# Sort the data by date and time
database.sort_values(by="Date/Time", inplace=True)
# Create a list of month names
themonths = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# Create a new column with month names
database["Month"] = database["Date/Time"].apply(lambda date: themonths[int(date.split("-")[1]) - 1])
# Create a figure with 2 subplots
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(10, 6), dpi=100)
# Plot daily average temperature on the first subplot
ax[0].plot(database["Mean Temp (°C)"], c='gray')
ax[0].set_xticks([])
ax[0].set_xlabel('Daily Average')
ax[0].xaxis.set_label_position('top')
ax[0].set_ylabel('Degrees Celsius')
ax[0].set_title('Hamilton Temperature Statistics By Month and Day for 2022', y=1.2)
ax[0].grid(axis='y', linestyle='--')
sns.boxplot(x="Month", y="Mean Temp (°C)", data=database, color='w', flierprops={'marker': 'o', 'markerfacecolor': 'w', 'markeredgecolor': 'k'},medianprops={'linestyle': 'dotted', 'color': 'k'}, ax=ax[1])
ax[1].set_ylabel('Degrees Celsius')
ax[1].set_xlabel('Monthly Mean, Median, Min and Max (of Daily Average)')
ax[1].xaxis.set_label_position('top')
ax[1].tick_params(top=False)
ax[1].grid(linestyle='--')
plt.show()
# Under 45 lines 
