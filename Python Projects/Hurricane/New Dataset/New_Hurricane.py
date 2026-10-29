from datascience import *
import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#Hurricane Dataset
Hurricane = Table.read_table('Cleaned_Hurricane_Dataset.csv')
print(Hurricane)
print(Hurricane.num_rows)
print(Hurricane.num_columns)
print(Hurricane.labels)

#Summary Statistics of Hurricanes including max, mean, median, min, standard deviation
print("Summary Statistics:")
print(f"Maximum Wind Speed: {round(np.max(Hurricane.column('max_wind_mph')), 2)} mph")
print(f"Average Wind Speed: {round(np.mean(Hurricane.column('max_wind_mph')), 2)} mph")
print(f"Standard Deviation Wind Speed: {round(np.std(Hurricane.column('max_wind_mph')), 2)} mph")
print(f"Median Wind Speed: {round(np.median(Hurricane.column('max_wind_mph')), 2)} mph")
print(f"Minimum Wind Speed: {round(np.min(Hurricane.column('max_wind_mph')), 2)} mph")
print(f"Coefficient of Variation: {round(np.std(Hurricane.column('max_wind_mph'))/np.mean(Hurricane.column('max_wind_mph')) * 100 ,2)}% mph")

#Highest Recorded Hurricane Wind Speeds Top 25
print('Top 25 Most Powerful Hurricanes')
print(Hurricane.sort('max_wind_mph', descending = True).take(range(0, 10)).select('storm_id', 'storm_name', 'decimal_date', 'year', 'latitude', 'longitude', 'storm_status', 'max_wind_mph', 'min_pressure_mb'))
print(Hurricane.sort('max_wind_mph', descending = True).take(range(10, 20)).select('storm_id', 'storm_name', 'decimal_date', 'year', 'latitude', 'longitude', 'storm_status', 'max_wind_mph', 'min_pressure_mb'))
print(Hurricane.sort('max_wind_mph', descending = True).take(range(20, 25)).select('storm_id', 'storm_name', 'decimal_date', 'year', 'latitude', 'longitude', 'storm_status', 'max_wind_mph', 'min_pressure_mb'))

#Lowest Recorded Hurricane Air Pressure Top 25
print('Top 25 Lowest Air Pressure Hurricanes')
print(Hurricane.where('min_pressure_mb', are.above(0)).sort('min_pressure_mb', descending = False).take(range(0, 10)).select('storm_id', 'storm_name', 'decimal_date', 'year', 'latitude', 'longitude', 'storm_status', 'max_wind_mph', 'min_pressure_mb'))
print(Hurricane.where('min_pressure_mb', are.above(0)).sort('min_pressure_mb', descending = False).take(range(10, 20)).select('storm_id', 'storm_name', 'decimal_date', 'year', 'latitude', 'longitude', 'storm_status', 'max_wind_mph', 'min_pressure_mb'))
print(Hurricane.where('min_pressure_mb', are.above(0)).sort('min_pressure_mb', descending = False).take(range(20, 25)).select('storm_id', 'storm_name', 'decimal_date', 'year', 'latitude', 'longitude', 'storm_status', 'max_wind_mph', 'min_pressure_mb'))

#Line Plot of Average Wind Speed by Decade
print(f"Pre-2000s Average Wind Speed: {round(np.mean(Hurricane.where('year', are.below(2000)).column('max_wind_mph')), 2)} mph")
print(f"Post-2000s Average Wind Speed: {round(np.mean(Hurricane.where('year', are.above(2000)).column('max_wind_mph')), 2)} mph")

Hurricane.group('decade', np.mean).select('decade', 'max_wind_mph mean').plot('decade', 'max_wind_mph mean')
plt.title('Average Hurricane Wind Speed by Decade')
plt.xlabel('Decade')
plt.ylabel('Average Max Wind Speed')
plt.show()

#Bar Chart Graph of 25 Most Powerful Hurricanes
Hurricane.sort('max_wind_mph', descending = True).take(range(0, 25)).barh('storm_name', 'max_wind_mph')
plt.title('Top 25 Most Powerful Hurricanes')
plt.xlabel('max_wind_mph')
plt.ylabel('storm_name')
plt.show()

#Bar Graph of 25 Lowest Air Pressure Hurricanes
Hurricane.where('min_pressure_mb', are.above(0)).sort('min_pressure_mb', descending = False).take(range(0, 25)).barh('storm_name', 'min_pressure_mb')
plt.title('Top 25 Lowest Air Pressure Hurricanes')
plt.xlabel('min_pressure_mb')
plt.ylabel('storm_name')
plt.show()

#Bar Chart of Categories of Hurricanes
print(Hurricane.where('storm_status', are.not_equal_to('Tropical Depression')).group('storm_status', collect = len).select('storm_status', 'storm_id len').relabel('storm_id len', 'storm_count').sort('storm_count', descending = True))
Hurricane.where('storm_status', are.not_equal_to('Tropical Depression')).group('storm_status', collect = len).select('storm_status', 'storm_id len').relabel('storm_id len', 'storm_count').sort('storm_count', descending = True).barh('storm_status', 'storm_count')
plt.title('Number of Hurricane Categories')
plt.xlabel('Count')
plt.ylabel('Hurricane Categories')
plt.show()

#Bar Chart of Most Hurricanes in a Season
Hurricane.where('storm_status', are.containing('Hurricane')).group('year', collect = len).relabel('storm_id len', 'storm_count').sort('storm_count', descending = True).take(range(0, 25)).barh('year', 'storm_count')
plt.title('Most Hurricanes in a Season')
plt.xlabel('Count')
plt.ylabel('Year')
plt.show()

#Scatter Plot of Wind Speed
Hurricane.scatter('decimal_date', 'max_wind_mph')
plt.title('Wind Speed Distribution')
plt.xlabel('decimal_date')
plt.ylabel('max_wind_mph')
plt.show()

#Linear Regression with max_wind_mph & min_pressure_mb for all pressure above 0
x = np.array(Hurricane.where('min_pressure_mb', are.above(0)).column('max_wind_mph'))
y = np.array(Hurricane.where('min_pressure_mb', are.above(0)).column('min_pressure_mb'))

coefficients = np.polyfit(x, y, 1)
a = coefficients[0] # Slope
b = coefficients[1] # Y-Intercept

x_fit = x
y_fit = a * x + b

plt.scatter(x, y, label='Data Points')
plt.plot(x_fit, y_fit, label=f'y={a:.2f}x + {b:.2f}')
plt.title('Linear Regression')
plt.xlabel('max_wind_mph')
plt.ylabel('min_pressure_mb')
plt.grid(True)
plt.show()

r = np.corrcoef(x, y)[0, 1]
print(f"Linear Equation: y = {a:.2f}x + {b:.2f}")
print('Correlation coefficient (R):', r)