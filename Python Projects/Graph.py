from datascience import *
import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#y = 1
x = np.linspace(-10, 10, 1000)
y = 0 * x + 1
plt.plot(x, y, label='y = 1', color='blue')
plt.title('Graph of y = 1')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

#y = |x|
x = np.linspace(-10, 10, 1000)
y = abs(x)
plt.plot(x, y, label='y = |x|', color='blue')
plt.title('Graph of y = |x|')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

#y = x
x = np.linspace(-10, 10, 1000)
y = x
plt.plot(x, y, label='y = x', color='blue')
plt.title('Graph of y = x')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

#y = x^2
x = np.linspace(-10, 10, 1000)
y = x**2
plt.plot(x, y, label='y = x^2', color='blue')
plt.title('Graph of y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

#y = x^3
x = np.linspace(-10, 10, 1000)
y = x**3
plt.plot(x, y, label='y = x^3', color='blue')
plt.title('Graph of y = x^3')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

#y = √x
x = np.linspace(0, 10, 1000)
y = np.power(x, 1/2)
plt.plot(x, y, label='y = √x', color='blue')
plt.title('Graph of y = √x')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

#y = 1/x
x = np.linspace(-10, 10, 1000)
y = 1/x
plt.plot(x, y, label='y = 1/x', color='blue')
plt.title('Graph of y = 1/x')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

#y = 10^x
x = np.linspace(-10, 10, 1000)
y = np.power(10, x)
plt.plot(x, y, label='y = 10^x', color='blue')
plt.title('Graph of y = 10^x')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

#y = log10(x)
x = np.linspace(0.1, 10, 1000)
y = np.log10(x)
plt.plot(x, y, label='y = log10(x)', color='blue')
plt.title('Graph of y = log10(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

#y = sin(x)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.sin(x)
plt.plot(x, y, label='y = sin(x)', color='blue')
plt.title('Graph of y = sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

#y = cos(x)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.cos(x)
plt.plot(x, y, label='y = cos(x)', color='blue')
plt.title('Graph of y = cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

#y = tan(x)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.tan(x)
plt.plot(x, y, label='y = tan(x)', color='blue')
plt.title('Graph of y = tan(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

#y = arcsin(x)
x = np.linspace(-1, 1, 1000)
y = np.arcsin(x)
plt.plot(x, y, label='y = asin(x)', color='blue')
plt.title('Graph of y = asin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

#y = arccos(x)
x = np.linspace(-1, 1, 1000)
y = np.arccos(x)
plt.plot(x, y, label='y = acos(x)', color='blue')
plt.title('Graph of y = acos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

#y = arctan(x)
x = np.linspace(-10, 10, 1000)
y = np.arctan(x)
plt.plot(x, y, label='y = atan(x)', color='blue')
plt.title('Graph of y = atan(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

#x^2 + y^2 = r^2
theta = np.linspace(0, 2 * np.pi, 1000)
r = 5
x = r * np.cos(theta)
y = r * np.sin(theta)
plt.plot(x, y, label='Circle: x² + y² = r²', color='blue')
plt.title('Graph of a Circle')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()

#x^2/a^2 + y^2/b^2 = 1
theta = np.linspace(0, 2 * np.pi, 1000)
a = 5
b = 1
x = a * np.cos(theta)
y = b * np.sin(theta)
plt.plot(x, y, label='Ellipse: (x²/a²) + (y²/b²) = 1', color='blue')
plt.title('Graph of an Ellipse')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()

#Line Chart
x = [1, 2, 3, 4, 5]
y= [10, 5, 15, 25, 20]
plt.plot(x, y)
plt.title('Line Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

#Scatter Plot
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 25, 15, 25, 50])

plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

#Pie Chart
labels = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E', 'Category F']
sizes = [50, 25, 10, 10, 2.5, 2.5]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()

#Bar Chart
categories = ['A', 'B', 'C', 'D']
values = [25, 50, 10, 5]
plt.bar(categories, values)
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

#Bell Curve
mean = 0
standard_deviation = 1

#Define PDF function
def PDF(x):
    return (1.0 / (standard_deviation * np.sqrt(2 * np.pi))) * np.power(np.e, -0.5 * (((x - mean) / standard_deviation) ** 2))

#Common grid for plotting
x = np.linspace(mean - 4 * standard_deviation, mean + 4 * standard_deviation, 5000)
y = PDF(x)

#Plot Standard Normal PDF
plt.plot(x, y, color='blue', label='PDF')
plt.fill_between(x, y, where=(x <= -2.5) | (x >= 2.5), color='blue', alpha=0.5)

#Labels and annotations
plt.title('Standard Normal PDF')
plt.xlabel('z')
plt.ylabel('density')
plt.legend()
plt.grid(True)
plt.show()
