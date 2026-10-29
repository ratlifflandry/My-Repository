from datascience import *
import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#SQL Dataset
SQL = Table.read_table('MySQL.csv')
print(SQL)

#Year, Month, Day
year = make_array()
month = make_array()
day = make_array()

for i in range(0, SQL.num_rows):
    year = np.append(year, int(SQL.column('date_of_birth')[i].split('-')[0]))
    month = np.append(month, int(SQL.column('date_of_birth')[i].split('-')[1]))
    day = np.append(day, int(SQL.column('date_of_birth')[i].split('-')[2]))

#Age Column
from datetime import date

today = date.today()
print(today)

age =  make_array()

for i in range(0, SQL.num_rows):
    birthday = date(int(year[i]), int(month[i]), int(day[i]))

    age = np.append(age, round(int(str(today - birthday).split(' ')[0])/365, 2))

SQL = SQL.with_column('age', age).select('customer_id', 'first_name', 'last_name', 'date_of_birth', 'age', 'phone', 'email', 'address', 'customer_notes')
print(SQL)

#First Names Bar Chart
SQL.select('first_name', 'customer_id').group('first_name', collect = len).sort('customer_id len', descending = True).relabel('customer_id len', 'count').barh('first_name', 'count')
plt.show()

#Last Name Bar Chart
SQL.select('last_name', 'customer_id').group('last_name', collect = len).sort('customer_id len', descending = True).relabel('customer_id len', 'count').barh('last_name', 'count')
plt.show()

#Summary Statistics of Age
print("Summary Statistics:")
print(f"Maximum Age of Customers: {np.round(np.max(SQL.column('age')), 2)}")
print(f"Average Age of Customers: {np.round(np.mean(SQL.column('age')), 2)}")
print(f"Median Age of Customers: {np.round(np.median(SQL.column('age')), 2)}")
print(f"Minimum Age of Customers: {np.round(np.min(SQL.column('age')), 2)}")
print(f"Standard Deviation Age of Customers: {np.round(np.std(SQL.column('age'), ddof = 0), 2)}")
print(f"Coefficient of Variation Age of Customers: {np.round(np.std(SQL.column('age'), ddof = 0)/np.mean(SQL.column('age')) * 100, 2)}%")

#Bar Chart of Address
SQL.select('address', 'customer_id').group('address', collect = len).sort('customer_id len', descending = True).relabel('customer_id len', 'count').barh('address', 'count')
plt.show()

#SQL.to_csv("Cleaned_MySQL.csv")

