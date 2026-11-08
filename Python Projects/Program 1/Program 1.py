#Program 1
from datascience import *
import numpy as np
import math, time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#Print Hello World
print("Hello World!")

#Variables
x = 1                                   #Integer
y = 3.14                                #Float
name = "Adam"                           #String
car = True                              #Boolean
my_list = [1, 2, 3]                     #List
my_dictionary = {1:'a', 2:'b', 3:'c'}   #Dictionary
my_complex = 1j + 1                     #Complex number

#Print Variables
print(x, y, name, car, my_list, my_dictionary, my_complex)

#F-Strings
first_name = "Landry"
last_name = "Ratliff"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, my name is {full_name}!")
print(f"Hello, my name is {full_name}!")

#Newline & Whitespace
print("Languages:\n\tPython\n\tC++\n\tJava")

#Draw a Square
for i in range(4):
    print("0" * 10)

#Draw a Triangle
for i in range(1, 6):
    x = " " * (5 - i) + "0" * i
    y = "0" * i
    print(x + y)

#Draw a Circle
r = 25

for y in range(-r, r + 1):
    for x in range(int(-r * 2.5), int(r * 2.5) + 1):
        d = math.sqrt((x/2.5)**2 + y**2)
        if d <= r:
            print("O", end="")
        else:
            print(" ", end="")
    print()

#Printing ASCII Code
code = []
for i in range(0, 256):
    code.append(chr(i))
print(code)

#Casting Variables
print(int(5.0))             #Integer
print(float(5))             #Float
print("Pi = " + str(3.14))  #String
print(bool(1))              #Boolean
print(chr(1))               #Character

#if statement
print("Guess what number I'm thinking of?")
a = int(input("Enter number: "))
if a == 1:
    print("You guessed correctly!")
elif a != 1:
    print("You guessed incorrectly!")

#Example of 'and' statement
age = 25
license = True

if age >= 16 and license:
    print("You are allowed to drive.")
else:
    print("You are not allowed to drive.")

#Example of 'or' statement
rainjacket = True
umbrella = False

if rainjacket or umbrella:
    print("You can go outside.")
else:
    print("You should stay inside.")

#Creating a list
numbers = [1,2,3,4,5,6,7,8,9, 10]
print(numbers)

#Creating a list
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "black", "white", "brown", "gray"]
print(colors)

#Count number of items in list
count = 0
for i in colors:
    count = count + 1

print("Number of items: " + str(count))

#print using array index
print(colors[4], colors[6], colors[7])

#Loop through colors
for color in colors:
    print(color)

#Add + Remove elements
colors.append("baby blue")
colors.remove("red")

#Creating a dictionary
person = {"name": "Landry", "age": 21, "birthday": "03/30/2004"}
print(person["name"])
print(person["age"])
print(person["birthday"])

#Add + Remove
person["city"] = "Mckinney, TX"
del person["age"]
print(person)

#For loop
for i in range(10):
    print(i)  #Outputs: 0 1 2 3 4 5 6 7 8 9

#For loop start/stop
for i in range(0, 101, 5):
    print(i) #Outputs: 0 5 10, . . ., 100

#While loop
count = 0
while count < 10:
    print(count) #Outputs: 0 1 2 3 4 5 6 7 8 9
    count = count + 1

#While loop choices
while True:
    choice = input("Choose between door 1, 2, or 3:")

    if choice == '1':
        print("You win a million dollars: $1,000,000")
        break

    elif choice == '2':
        print("You win a Ferrari LaFerrari!")
        break

    elif choice == '3':
        print("You died!")
        break

#If-else statement
x = 1
if x == 1:
    print("True")
else:
    print("False")

#Try-except block
try:
    x = 1 / 0
except:
    print("Error")

#Returns an integer between 1 and 10
random_integer = np.random.randint(0, 10)
print("Random Integer: " + str(random_integer))

# Returns a float between 0 and 10
random_float = np.random.uniform(0, 10)
print("Random Decimal: " + str(random_float))

#Returns a character A-Z
my_list = []

for i in range(65, 91):
    my_list.append(chr(i))

for i in range(97, 123):
    my_list.append(chr(i))

i = np.random.randint(0, 52)
print("Random Character: " + my_list[i])

#Returns an element from list
my_list = ['a', 'b', 'c', 1, 2, 3]
random_choice = np.random.choice(my_list)
print("Random Choice: " + str(random_choice))

#Mean, Max, Min, Median, Mode
my_list = np.array([1,2,3,4,5,6,7,8,9,10,5,5,5,5,5,3.14])

print(f"List: {my_list}")
print("Mean: " + str(np.mean(my_list)))                        #mean(average)
print("Median: " + str(np.median(my_list)))                    #median(middle)
print("Standard Deviation: " + str(np.std(my_list, ddof = 0))) #population standard deviation (ddof degrees of freedom)
print("Max: " + str(np.max(my_list)))                          #maximum
print("Min: " + str(np.min(my_list)))                          #minimum
print("Count: " + str(len(my_list)))                           #count

#Total, Count, Mean, Max, Min of dataset
count = 0
total = 0
x = my_list[0]
y = my_list[0]

for i in my_list:
    count = count + 1
    total = i + total

    if i > x:
        x = i

    if i < y:
        y = i

print("Total: " + str(total))
print("Count: " + str(count))
print("Mean: " + str(total/count))
print("Max: " + str(x))
print("Min: " + str(y))

#Sort List
sorted_list = sorted(my_list)
print("Sorted List: " + str(sorted_list))

#Copy list
copy_list = []

for i in range(0, count):
    copy_list.append(my_list[i])

print("Copy List: " + str(copy_list))

#Defining a function
def greet(name):
    return "Hello " + name + "!"

#Calling a function
print(greet("John")) # Outputs: Hello John!

#Define a class
class Person:
    #Constructor to initialize name + age
    def __init__(self, name, age):
        #Instance variable name + age
        self.name = name
        self.age = age

    #Method to greet name
    def greetname(self):
        return "Hello, my name is " + str(self.name) + "."

    #Method to greet age
    def greetage(self):
        return "I am " + str(self.age) + " years old."

#Creating an object
p0 = Person("John", 25)
print(p0.greetname())   #Outputs: Hello, my name is John.
print(p0.greetage())    #Outputs: I am 25 years old.

#Define a class Circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return math.pi * self.radius ** 2

    def Circumference(self):
        return 2 * math.pi * self.radius

#Circle Object
radius = 5
p1 = Circle(radius)
print("Radius = " + str(radius))
print("Area = " + str(p1.Area()))
print("Circumference = " + str(p1.Circumference()))

#Define a class Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Area(self):
        return self.length * self.width

    def Perimeter(self):
        return 2 * self.length + 2 * self.width

#Rectangle Object
length = 5
width = 5
p2 = Rectangle(length, width)
print("Length = " + str(length))
print("Width = " + str(width))
print("Area = " + str(p2.Area()))
print("Perimeter = " + str(p2.Perimeter()))
print(Rectangle(10, 5).Area())

#Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello World! 12345")

#Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  #Outputs: Hello, World!

#Counting letters in a string
text = "abcdefghijklmnopqrstuvwxyz"
count = text.count('a')
print("# of a = " + str(count))

#Pi Math - Approximate Pi using the Basel Formula
def PI():
    print("Enter a number to approximate PI:")
    print("Press q to quit.")

    while True:
        #Get user input
        number = input()

        #If the user types 'q', exit the loop
        if number == 'q':
            break

        #Initialize variables for summation
        x = 0
        y = 0

        #Start timing just before the math begins
        start = time.time()

        #Perform the Basel summation up to 'number' terms
        while x < int(number):
            x = x + 1
            y = y + 6 / (x ** 2)

        #Final approximation of pi from the summation
        answer = y ** 0.5

        #End timing after computation finishes
        end = time.time()

        #Print results
        print(answer)                         #Approximation of pi
        print(f"Time: {end - start:.6f}s")    #Time taken for calculation

#Run the program
PI()

#Timer
time_total = 0

x = 0
while x < 5:
    time_total = time_total + 1
    print(time_total)
    time.sleep(1)

    if time_total == 5:
        break