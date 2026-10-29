from datascience import *
import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#Supermarket Dataset
Super = Table.read_table('Supermarket.csv')
print(Super)
print(Super.num_rows)
print(Super.num_columns)
print(Super.labels)

#Customer Names
print(Super.group('Customer Name').sort('count', descending = True))

#Customers with Most Sales
print(Super.group('Customer Name', collect = np.sum).sort('Sales sum', descending = True).select('Customer Name', 'Sales sum'))

#Countries with Most Customers
print(Super.group('Country').sort('count', descending = True))

#States with Most Customers
print(Super.group('State').sort('count', descending = True))

#Cities with Most Customers
print(Super.group('City').sort('count', descending = True))

#Segments with Most Customers
print(Super.group('Segment').sort('count', descending = True))

postal_code = make_array()

for i in range(0, len(Super.column('Postal Code'))):
    if Super.column('Postal Code')[i] > 0:
        postal_code = np.append(postal_code, Super.column('Postal Code')[i])

print(postal_code)
print(np.min(postal_code))
print(np.average(postal_code))
print(np.std(postal_code, 0))
print(np.max(postal_code))



