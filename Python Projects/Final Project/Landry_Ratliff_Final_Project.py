#Final Project
from datascience import *
import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Final Project Guide
# 1. Overview
# Complete an end-to-end data science project that shows what you learned this term.
# Pick a topic/dataset you care about (needs instructor approval).
# Do the full pipeline: question → data → cleaning → EDA/visuals → inference or prediction → conclusions.
# Use method from the course (e.g., hypothesis test).
# Communicate clearly: explain what you did and why, show key figures, and interpret results.
# Due: Dec 10, 2025
# Submit written report + code on Canvas by class time.
# Give a 10–15 minute in-class presentation on Dec 10.

# 2. Deliverables
# Written report: narrative, methods, results, figures, key code snippets.
# Runnable code: clear structure, instructions to reproduce.
# Slides for a 10–15 minute talk (file.py or Microsoft PowerPoint).

# 3. Structure
# Abstract (10 pts)
# Introduction (10 pts)
# Dataset (20 pts)
# Exploratory Data Analysis (EDA) (20 pts)
# Hypothesis Testing (30 pts)
# Summary of learning (10 pts)

# ===========================
# 🏃‍♂️Running World Record Project
# ===========================

#Abstract:
#This project investigates the historical progression of elite mile running performances to understand the physiological limits of human endurance.
#The results suggest the fastest possible mile time of 3:42.2.

#Summary:
#I learned to clean and transform real-world data, create visualizations, apply regression and hypothesis testing, and interpret results in the context of human physiology and performance limits.

# Research Questions:
# How have world records in running (mile, 5K, half-marathon, and marathon) changed over time?
# Are improvements slowing down — i.e., are humans approaching a physiological limit?
# Do environmental or technological factors (e.g., shoe technology, altitude, weather, course elevation, or course surface) explain changes in performance?
# Does the distribution of elite finishing times predict who might set the next record?

# Datasets:
# World Athletics Records Database -> https://worldathletics.org/records
# Wikipedia (World Record Progression) -> https://en.wikipedia.org/wiki/Mile_run_world_record_progression

# Analysis:
# Exploratory Data Analysis: Plot world record times vs. year
# Compare 1900s vs. 2000s

# Statistical Inference: Fit a regression model of record time vs. year and test whether the rate of improvement is statistically significant.

# Prediction: Predict what the fastest time possible is using exponential decay

# ===========================
# One-Mile Run Analysis
# ===========================
mile_world_record = 223.13  #(Hicham El Guerrouj, 3:43.13 in 1999)
print("The Mile World Record in 2025:")
print(f"The mile world record is {mile_world_record} seconds ({int(mile_world_record/60)}:{mile_world_record % 60:.2f} minutes), set by Hicham El Guerrouj in 1999.")

# ===========================
# World Records Table
# ===========================
world_records = Table.read_table('world_records.csv')  # Read CSV file with world records
print(world_records)

#One-Mile Records Table
mile_records = Table.read_table('one-mile.csv')  # Read CSV file with one-mile records
print(mile_records)

# ===========================
# Decimal Date
# ===========================
#Converts date strings ('30-Mar-25' -> 2025.2438) into numeric year with fractional day
decimal_date = make_array()
year = 0
month = 0
day = 0

for i in range(mile_records.num_rows):

    day = int(mile_records.column('Date')[i].split('-')[0])
    month = mile_records.column('Date')[i].split('-')[1]
    year = int(mile_records.column('Date')[i].split('-')[2])

    if int(year) < 50:
        year = year + 2000
    else:
        year = year + 1900

    if month == 'Jan':
        month = 0
    elif month == 'Feb':
        month = 31
    elif month == 'Mar':
        month = 59
    elif month == 'Apr':
        month = 90
    elif month == 'May':
        month = 120
    elif month == 'Jun':
        month = 151
    elif month == 'Jul':
        month = 181
    elif month == 'Aug':
        month = 212
    elif month == 'Sep':
        month = 243
    elif month == 'Oct':
        month = 273
    elif month == 'Nov':
        month = 304
    elif month == 'Dec':
        month = 334

    decimal_date = np.append(decimal_date, year + (day + month)/365.25)

mile_records = mile_records.with_column('Date #', decimal_date).with_column('Year', np.floor(decimal_date))

# ===========================
# Time Formatting Function
# ===========================
#Converts mark strings (e.g., '3:26.00') to total seconds
time = make_array()
minute = 0
second = 0

for i in range(mile_records.num_rows):

    minute = mile_records.column('Mark')[i].split(':')[0]
    second = mile_records.column('Mark')[i].split(':')[1]

    if 'h' in second:
        second = second.replace('h', '')

    time = np.append(time, float(minute) * 60 + float(second))

mile_records = mile_records.with_column('Mark #', time)

# ===========================
# Mile Records Chart
# ===========================
print(mile_records.group('Competitor',  collect = min).relabel('Rank min', 'Rank').relabel('Mark min', 'Mark').relabel('Mark # min', 'Mark #').relabel('DOB min', 'DOB').relabel('Nat min', 'Nat').relabel('Venue min', 'Venue').relabel('Date min', 'Date').relabel('Results Score min', 'Results Score').select('Competitor', 'Rank', 'Mark', 'Mark #', 'DOB', 'Nat', 'Venue', 'Date', 'Results Score').sort('Mark #'))

print("_______________________________")
print("Mile Records")
print("_______________________________")

#Count
mile_count = len(mile_records.column('Mark #'))
print(f"Count: {mile_count}")

#Mean
mile_mean = np.mean(mile_records.column('Mark #'))
print(f"Mean: {int(mile_mean/60)}:{np.round(mile_mean % 60, 2)}")

#Median
mile_median = np.median(mile_records.column('Mark #'))
print(f"Median: {int(mile_median/60)}:{np.round(mile_median % 60, 2)}")

#Maximum
mile_max = np.max(mile_records.column('Mark #'))
print(f"Maximum: {int(mile_max/60)}:{np.round(mile_max % 60, 2)}")

#Minimum
mile_min = np.min(mile_records.column('Mark #'))
print(f"Minimum: {int(mile_min/60)}:{np.round(mile_min % 60, 2)}")

#Standard Deviation
mile_standard_deviation = np.std(mile_records.column('Mark #'), ddof=0)
print(f"Standard Deviation: {int(mile_standard_deviation/60)}:{np.round(mile_standard_deviation, 2)}")

#Coefficient of Variation
print(f"Coefficient of Variation: {np.round(mile_standard_deviation/mile_mean * 100, 2)}%")

# ===========================
# Scatter Plot: Marks Over Time
# ===========================
mile_records.scatter('Date #', 'Mark #')
plt.title('Mile Runs over Time')
plt.xlabel('Date #')
plt.ylabel('Mark #')
plt.show()

# ===========================
# World Records
# ===========================
mile_records = mile_records.sort('Date #', descending = False)  #Sort records chronologically
record = make_array()
year_record = make_array()
competitor_record = make_array()
fastest_time = 300  #Maximum mark (5-minute mile)

for i in range(mile_records.num_rows):
    mark = mile_records.column('Mark #')[i]
    year = mile_records.column('Year')[i]
    competitor = mile_records.column('Competitor')[i]

    #Check for new world record
    if mark < fastest_time:
        fastest_time = mark
        record = np.append(record, mark)
        year_record = np.append(year_record, year)
        competitor_record = np.append(competitor_record, competitor)

#Create summary table of world records
world_record = Table().with_columns(
    'Competitor', competitor_record,
    'Year', year_record,
    'Mark #', record,
)

print('World Record Progression')
print(world_record.select('Competitor', 'Year', 'Mark #').take(np.arange(0, 19)))

# ===========================
# World Record Progression
# ===========================
world_record.bar('Year', 'Mark #')
plt.title('World Record Progression')
plt.xlabel('Year')
plt.ylabel('Mark #')
plt.show()

# ===========================
# Population-Weighted Years
# ===========================
population = [
    2685894860, 2685894860, 2852618337, 2911249671, 3123374315, 3264487339,
    3334533703, 3404041125, 3473412880, 4070735277, 4070735277, 4368539528,
    4447606236, 4528777306, 4528777306, 4528777306, 4868943465, 5591544797,
    6067758458, 8300000000
]

population_years = []
for i in range(len(world_record.column('Year'))):
    year = world_record.column('Year')[i]
    elapsed = year - 1954  #Years since 1954
    population_years.append(elapsed * population[i])

world_record = world_record.with_column('Population-Years', population_years)

# ===========================
# Percent-Change
# ===========================
percent_change = [0]

for i in range(len(world_record.column('Mark #')) - 1):
    new = float(world_record.column('Mark #')[i + 1])
    old = float(world_record.column('Mark #')[i])
    percent_change.append(np.round((old - new)/old * 100, 4))

world_record = world_record.with_column('Percent Change', percent_change)

world_record.bar('Year', 'Percent Change')
plt.title('World Record Progression Percent Change')
plt.xlabel('Year')
plt.ylabel('Percent Change')
plt.show()

# ===========================
# Linear Regression
# ===========================
x = np.array(world_record.column('Year'))
y = np.array(world_record.column('Mark #'))

#y = a * x + b
coefficients = np.polyfit(x, y, 1)
a = coefficients[0]     #Slope
b = coefficients[1]     #Y-Intercept

x_fit = x
y_fit = a * x + b

plt.scatter(x, y, label='Data Points')
plt.plot(x_fit, y_fit, color='red', label=f'y={a:.2f}x + {b:.2f}')
plt.title('Linear Regression')
plt.xlabel('Year')
plt.ylabel('Mark #')
plt.legend()
plt.grid(True)
plt.show()

r = np.corrcoef(x, y)[0, 1]
print(f"Correlation coefficient: {r:.4f}")

# ===========================
# Polynomial Regression
# ===========================
x = np.array(world_record.column('Year'))
y = np.array(world_record.column('Mark #'))

#y = a * x^2 + b * x + c
coefficients = np.polyfit(x, y, 2)
a = coefficients[0]     #Quadratic
b = coefficients[1]     #Slope
c = coefficients[2]     #Y-Intercept

x_fit = x
y_fit = a * x_fit ** 2 + b * x_fit + c

plt.scatter(x, y, label='Data Points')
plt.plot(x_fit, y_fit, color='red', label=f'y={a:.3f}x^2+{b:.3f}x+{c:.3f}')
plt.title('Polynomial Regression')
plt.xlabel('Year')
plt.ylabel('Mark #')
plt.legend()
plt.grid(True)
plt.show()

r_poly = np.corrcoef(y, y_fit)[0, 1]
print(f"Correlation coefficient: {r_poly:.4f}")

# ===========================
# Exponential Regression with Asymptote
# ===========================
def exponential(x, a, b, c):
    return a * np.power(np.e, b * x) + c

x = np.array(world_record.column('Population-Years'))
y = np.array(world_record.column('Mark #'))

#y = a * e^(b * x) + c
a = max(y) - min(y)
b = -0.0000000001
c = min(y)

parameters = curve_fit(exponential, x, y, p0 = [a, b, c], maxfev = 100_000)[0]
a = parameters[0]   #Amplitude
b = parameters[1]   #Growth_rate
c = parameters[2]   #Asymptote

x_fit = x
y_fit = a * np.power(np.e, b * x) + c

plt.scatter(x, y, label = 'Data Points')
plt.plot(x_fit, y_fit, color = 'red', label = f'y = {a:.3f} * e^({b:.15f} * x) + {c:.3f}')
plt.title('Exponential Regression with Asymptote')
plt.xlabel('Population-Years')
plt.ylabel('Mark #')
plt.axhline(y=c, color='blue', linestyle='--', label=f'Asymptote: y = {c:.3f}')
plt.legend()
plt.grid(True)
plt.show()

r_exp = np.corrcoef(y, y_fit)[0, 1]
print(f"Correlation coefficient: {r_exp:.4f}")

#Theoretical fastest mile
print(f"The fastest mile possible: {np.round(c, 3)} seconds")
print(f"{int(c/60)}:{np.round(c % 60, 2)} minutes")

# ===========================
# Future Outlook: Jakob Ingebrigtsen 2026 Claim
# ===========================
print("Future Predictions:")
print("Jakob Ingebrigtsen, the 25-year-old Norwegian middle-distance star, says he’s targeting the world records in the 1500m, mile, and 5000m next year (2026).")
print(f"Based on our exponential regression and population-weighted analysis, the theoretical fastest mile is {int(c/60)}:{np.round(c % 60, 2)} minutes.")
print("While our model predicts an asymptotic limit, Ingebrigtsen’s attempt could provide valuable real-world data to refine these projections and test how close elite athletes can approach human physiological limits.")