from datascience import *
import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#Tornado Dataset
Tornado = Table.read_table('US_Tornado_Dataset.csv')
print(Tornado)

#Renaming Columns
Tornado = Tornado.relabel('yr', 'Year').relabel('mo', 'Month').relabel('dy', 'Day').relabel('date', 'Date').relabel('st', 'State').relabel('mag', 'Enhanced Fujita Scale').relabel('inj', 'Injuries').relabel('fat', 'Fatalities').relabel('slat', 'Start Latitude').relabel('slon', 'Start Longitude').relabel('elat', 'End Latitude').relabel('elon', 'End Longitude').relabel('len', 'Length').relabel('wid', 'Width')

#Decimal Date & Decade
decimal_date = make_array()
decade = make_array()
year = 0
month = 0
day = 0

for i in range(0, Tornado.num_rows):

    year = Tornado.column('Year')[i]

    decade = np.append(decade, (year // 10) * 10)

    if Tornado.column('Month')[i] == 1:
        month = 0
    elif Tornado.column('Month')[i] == 2:
        month = 31
    elif Tornado.column('Month')[i] == 3:
        month = 59
    elif Tornado.column('Month')[i] == 4:
        month = 90
    elif Tornado.column('Month')[i] == 5:
        month = 120
    elif Tornado.column('Month')[i] == 6:
        month = 151
    elif Tornado.column('Month')[i] == 7:
        month = 181
    elif Tornado.column('Month')[i] == 8:
        month = 212
    elif Tornado.column('Month')[i] == 9:
        month = 243
    elif Tornado.column('Month')[i] == 10:
        month = 273
    elif Tornado.column('Month')[i] == 11:
        month = 304
    elif Tornado.column('Month')[i] == 12:
        month = 334

    day = Tornado.column('Day')[i]

    decimal_date = np.append(decimal_date, year + (day + month)/365)

Tornado = Tornado.with_columns('Decimal Date', decimal_date, 'Decade', decade)

#Convert State Codes → Full State Names (TX --> Texas)
state_map = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "DC": "Washington, DC",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "PR": "Puerto Rico",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VI": "Virgin Islands",
    "VT": "Vermont",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming"
}

state = make_array(*(state_map[i] for i in Tornado.column('State')))

Tornado = Tornado.drop('State').with_column('State', state)

#Echanced Fujita Scale Column, Wind Column, & Damage Column
magnitude_map = {
    -9: -1,
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5
}

wind_map = {
    -9: "nan",
    0: "65-85 mph",
    1: "86-110 mph",
    2: "111-135 mph",
    3: "136-165 mph",
    4: "166-200 mph",
    5: ">200 mph"
}

damage_map = {
    -9: "nan",
    0: "Minor Damage",
    1: "Moderate Damage",
    2: "Considerable Damage",
    3: "Severe Damage",
    4: "Extreme Damage",
    5: "Massive Damage"
}

magnitude = make_array(*(magnitude_map[i] for i in Tornado.column('Enhanced Fujita Scale')))
wind = make_array(*(wind_map[i] for i in Tornado.column('Enhanced Fujita Scale')))
damage = make_array(*(damage_map[i] for i in Tornado.column('Enhanced Fujita Scale')))

Tornado = Tornado.drop('Enhanced Fujita Scale').with_columns('Enhanced Fujita Scale', magnitude, 'Wind Speed', wind, 'Damage', damage)

#Length Miles -> Kilometers; Width Yards -> Meters
length = np.round(Tornado.column('Length') * 1.61, 0)
width = np.round(Tornado.column('Width') * 0.9144, 0)

Tornado = Tornado.drop('Length').drop('Width').with_columns('Length', length, 'Width', width)

#Rename Wind Speed, Length, & Width
Tornado = Tornado.relabel('Wind Speed', 'Wind Speed (mph)').relabel('Length', 'Length (km)').relabel('Width', 'Width (m)')

#Drop Puerto Rico & U.S. Virgin Islands
Tornado = Tornado.where('State', are.not_equal_to('Puerto Rico')).where('State', are.not_equal_to('Virgin Islands'))

#Date + State column
date_state = make_array()

for i in range(0, Tornado.num_rows):
    date_state = np.append(date_state, Tornado.column('Date')[i] + ' ' + Tornado.column('State')[i])

Tornado = Tornado.with_columns('Date State', date_state)

#Reorder Columns
Tornado = Tornado.select('Date State', 'Date', 'Decimal Date', 'Decade', 'Year', 'Month', 'Day', 'State', 'Enhanced Fujita Scale', 'Wind Speed (mph)', 'Damage', 'Injuries', 'Fatalities', 'Start Latitude', 'Start Longitude', 'End Latitude', 'End Longitude', 'Length (km)', 'Width (m)')

#Drop -1 EF-Rating Tornado
Tornado = Tornado.where('Enhanced Fujita Scale', are.not_equal_to(-1))

#Convert to CVS File, Make visuals in new .PY File
Tornado.to_csv('Cleaned_US_Tornado_Dataset.csv')

#Most Powerful Tornados
print("---Most Powerful Tornadoes---")
print(Tornado.where('Enhanced Fujita Scale', are.equal_to(5)).sort('Decimal Date', descending = True))