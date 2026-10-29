from datascience import *
import numpy as np
import math
import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt

#Hurricane Dataset
Hurricane = Table.read_table('Hurricane_Dataset.csv')
print(Hurricane)

#Remove Negative Wind Values
Hurricane = Hurricane.where('max_wind_kt', are.above(0))

#Drop Record_ID Column
#Drop Status Column
Hurricane = Hurricane.drop('record_id').drop('status')

#Number of Rows & Columns
print(Hurricane.num_rows)
print(Hurricane.num_columns)
print(Hurricane)

#Windspeed knots -> mph
wind = make_array()

for i in range(0, Hurricane.num_rows):
    wind = np.append(wind, round(Hurricane.column('max_wind_kt')[i] * 1.15078, 1))

Hurricane = Hurricane.drop('max_wind_kt').with_column('max_wind_mph', wind).select('storm_id', 'storm_name', 'date', 'time', 'latitude', 'longitude', 'max_wind_mph', 'min_pressure_mb')
print(Hurricane)

#Date -> Year/Month/Day
year = make_array()
month = make_array()
day = make_array()
date = Hurricane.column('date')

for i in range(0, Hurricane.num_rows):
    year = np.append(year, int(date[i] / 10_000))
    month = np.append(month, int(date[i] % 10_000 / 100))
    day = np.append(day, int(date[i] % 100))

Hurricane = Hurricane.with_columns('year', year, 'month', month, 'day', day).select('storm_id', 'storm_name', 'date', 'year', 'month', 'day', 'time', 'latitude', 'longitude', 'max_wind_mph', 'min_pressure_mb')
print(Hurricane)

#Date -> Decimal_Date
decimal_date = make_array()
date = Hurricane.column('date')
year = Hurricane.column('year')
month = Hurricane.column('month')
day = Hurricane.column('day')

for i in range(0, Hurricane.num_rows):
    if month[i] == 1:
        decimal_date = np.append(decimal_date, round(year[i] + day[i]/365, 3))
    elif month[i] == 2:
        decimal_date = np.append(decimal_date, round(year[i] + (day[i] + 31)/365, 3))
    elif month[i] == 3:
        decimal_date = np.append(decimal_date, round(year[i] + (day[i] + 59)/365, 3))
    elif month[i] == 4:
        decimal_date = np.append(decimal_date, round(year[i] + (day[i] + 90)/365, 3))
    elif month[i] == 5:
        decimal_date = np.append(decimal_date, round(year[i] + (day[i] + 120)/365, 3))
    elif month[i] == 6:
        decimal_date = np.append(decimal_date, round(year[i] + (day[i] + 151)/365, 3))
    elif month[i] == 7:
        decimal_date = np.append(decimal_date, round(year[i] + (day[i] + 181)/365, 3))
    elif month[i] == 8:
        decimal_date = np.append(decimal_date, round(year[i] + (day[i] + 212)/365, 3))
    elif month[i] == 9:
        decimal_date = np.append(decimal_date, round(year[i] + (day[i] + 243)/365, 3))
    elif month[i] == 10:
        decimal_date = np.append(decimal_date, round(year[i] + (day[i] + 273)/365, 3))
    elif month[i] == 11:
        decimal_date = np.append(decimal_date, round(year[i] + (day[i] + 304)/365, 3))
    elif month[i] == 12:
        decimal_date = np.append(decimal_date, round(year[i] + (day[i] + 334)/365, 3))

Hurricane = Hurricane.with_column('decimal_date', decimal_date).select('storm_id', 'storm_name', 'date', 'decimal_date', 'year', 'month', 'day', 'time', 'latitude', 'longitude', 'max_wind_mph', 'min_pressure_mb')
print(Hurricane)

#Year -> Decade; 2025 -> 2020
decade = make_array()

for i in range(0, Hurricane.num_rows):
    decade = np.append(decade, int(Hurricane.column('year')[i] / 10) * 10)

Hurricane = Hurricane.with_column('decade', decade).select('storm_id', 'storm_name', 'date', 'decimal_date', 'year', 'month', 'day', 'decade', 'time', 'latitude', 'longitude', 'max_wind_mph', 'min_pressure_mb')
print(Hurricane)

#Time -> AM/PM
time = Hurricane.column('time')
UTC = make_array()

for i in range(0, Hurricane.num_rows):
    hours = int(time[i] / 100)
    minutes = int(time[i] % 60)

    #Convert Military time to AM/PM
    period = 'AM'
    hours_12 = 0

    if hours == 0:
        hours_12 = 12
    elif hours == 12:
        hours_12 = 12
        period = 'PM'
    elif hours > 12:
        hours_12 = hours - 12
        period = 'PM'
    else:
        hours_12 = hours

    UTC = np.append(UTC, f"{hours_12}:{minutes:02d} {period}")

Hurricane = Hurricane.drop('time').with_column('time', UTC).select('storm_id', 'storm_name', 'date', 'decimal_date', 'year', 'month', 'day', 'decade', 'time', 'latitude', 'longitude', 'max_wind_mph', 'min_pressure_mb')
print(Hurricane)

#Hurricane Status
#max_wind_mph -> Tropical Depression, Tropical Storm, Category 1 Hurricane, Category 2 Hurricane, Category 3 Hurricane, Category 4 Hurricane, Category 5 Hurricane

storm_status = make_array()
max_wind_mph = Hurricane.column('max_wind_mph')

for i in range(0, Hurricane.num_rows):
    if 0 <= max_wind_mph[i] < 40:
        storm_status = np.append(storm_status, 'Tropical Depression')
    elif 40 <= max_wind_mph[i] < 74:
        storm_status = np.append(storm_status, 'Tropical Storm')
    elif 74 <= max_wind_mph[i] < 96:
        storm_status = np.append(storm_status, 'Category 1 Hurricane')
    elif 96 <= max_wind_mph[i] < 111:
        storm_status = np.append(storm_status, 'Category 2 Hurricane')
    elif 111 <= max_wind_mph[i] < 131:
        storm_status = np.append(storm_status, 'Category 3 Hurricane')
    elif 131 <= max_wind_mph[i] < 155:
        storm_status = np.append(storm_status, 'Category 4 Hurricane')
    elif max_wind_mph[i] >= 155:
        storm_status = np.append(storm_status, 'Category 5 Hurricane')

Hurricane = Hurricane.with_column('storm_status', storm_status).select('storm_id', 'storm_name', 'date', 'decimal_date', 'year', 'month', 'day', 'decade', 'time', 'latitude', 'longitude', 'storm_status', 'max_wind_mph', 'min_pressure_mb')
print(Hurricane)

#Creating table with the highest wind speeds for each unique storm_id
Atlantic_Hurricane = Hurricane.group('storm_id', collect = np.max).select('storm_id', 'max_wind_mph max')

Atlantic_Hurricane = Hurricane.join('storm_id', Atlantic_Hurricane, 'storm_id').sort('date', descending = False)

check = make_array() #Checks to see if storm_id already occurred and skips past it

storm_id = make_array()
storm_name = make_array()
date = make_array()
decimal_date = make_array()
year = make_array()
month = make_array()
day = make_array()
decade = make_array()
time = make_array()
latitude = make_array()
longitude = make_array()
storm_status = make_array()
max_wind_mph = make_array()
min_pressure_mb = make_array()

for i in range(0, Atlantic_Hurricane.num_rows):
    if Atlantic_Hurricane.column('max_wind_mph')[i] == Atlantic_Hurricane.column('max_wind_mph max')[i]:
        if Atlantic_Hurricane.column('storm_id')[i] not in check:
            check = np.append(check, Atlantic_Hurricane.column('storm_id')[i])

            storm_id = np.append(storm_id, Atlantic_Hurricane.column('storm_id')[i])
            storm_name = np.append(storm_name, Atlantic_Hurricane.column('storm_name')[i])
            date = np.append(date, Atlantic_Hurricane.column('date')[i])
            decimal_date = np.append(decimal_date, Atlantic_Hurricane.column('decimal_date')[i])
            year = np.append(year, Atlantic_Hurricane.column('year')[i])
            month = np.append(month, Atlantic_Hurricane.column('month')[i])
            day = np.append(day, Atlantic_Hurricane.column('day')[i])
            decade = np.append(decade, Atlantic_Hurricane.column('decade')[i])
            time = np.append(time, Atlantic_Hurricane.column('time')[i])
            latitude = np.append(latitude, Atlantic_Hurricane.column('latitude')[i])
            longitude = np.append(longitude, Atlantic_Hurricane.column('longitude')[i])
            storm_status = np.append(storm_status, Atlantic_Hurricane.column('storm_status')[i])
            max_wind_mph = np.append(max_wind_mph, Atlantic_Hurricane.column('max_wind_mph')[i])
            min_pressure_mb = np.append(min_pressure_mb, Atlantic_Hurricane.column('min_pressure_mb')[i])

Atlantic_Hurricane = Table().with_columns(
    'storm_id', storm_id,
    'storm_name', storm_name,
    'date', date,
    'decimal_date', decimal_date,
    'year', year,
    'month', month,
    'day', day,
    'decade', decade,
    'time', time,
    'latitude', latitude,
    'longitude', longitude,
    'storm_status', storm_status,
    'max_wind_mph', max_wind_mph,
    'min_pressure_mb', min_pressure_mb
)
print(Atlantic_Hurricane)

#Convert Hurricane to CSV File
Atlantic_Hurricane.to_csv("Cleaned_Hurricane_Dataset.csv")
