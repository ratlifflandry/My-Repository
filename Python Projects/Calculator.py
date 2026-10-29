from datascience import *
import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Math functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error"
    return a / b

def power(a, b):
    return math.pow(a, b)

def logarithm10(a):
    if a <= 0:
        return "Error"
    return math.log10(a)

def sine(a):
    return math.sin(math.radians(a))

def cosine(a):
    return math.cos(math.radians(a))

def tangent(a):
    return math.tan(math.radians(a))

def asin(a):
    if -1 <= a <= 1:
        return math.degrees(math.asin(a))
    return "Error"

def acos(a):
    if -1 <= a <= 1:
        return math.degrees(math.acos(a))
    return "Error"

def atan(a):
    return math.degrees(math.atan(a))

def factorial(a):
    return math.factorial(int(a))

def calculator():
    print("Scientific Calculator")
    print("Options:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Logarithm")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Arcsine")
    print("11. Arccosine")
    print("12. Arctangent")
    print("13. Factorial")
    print("14. Exit")

    while True:
        choice = input("\nChoose an operation (1-14): ")

        if choice == '1':
            print("Addition")
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(str(a) + " + " + str(b) + " = " + str(add(a, b)))

        elif choice == '2':
            print("Subtraction")
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(str(a) + " - " + str(b) + " = " + str(subtract(a, b)))

        elif choice == '3':
            print("Multiplication")
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(str(a) + " x " + str(b) + " = " + str(multiply(a, b)))

        elif choice == '4':
            print("Division")
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(str(a) + " / " + str(b) + " = " + str(divide(a, b)))

        elif choice == '5':
            print("Power")
            a = float(input("Enter the base: "))
            b = float(input("Enter the exponent: "))
            print(str(a) + " ^ " + str(b) + " = " + str(power(a, b)))

        elif choice == '6':
            print("Logarithm")
            a = float(input("Enter a number: "))
            print("log(" + str(a) + ") = " + str(logarithm10(a)))

        elif choice == '7':
            print("Sine")
            a = float(input("Enter angle in degrees: "))
            print("sin(" + str(a) + ") = " + str(sine(a)))

        elif choice == '8':
            print("Cosine")
            a = float(input("Enter angle in degrees: "))
            print("cos(" + str(a) + ") = " + str(cosine(a)))

        elif choice == '9':
            print("Tangent")
            a = float(input("Enter angle in degrees: "))
            print("tan(" + str(a) + ") = " + str(tangent(a)))

        elif choice == '10':
            print("Arcsine")
            a = float(input("Enter a value (between -1 and 1): "))
            print("arcsin(" + str(a) + ") = " + str(asin(a)))

        elif choice == '11':
            print("Arccosine")
            a = float(input("Enter a value (between -1 and 1): "))
            print("arccos(" + str(a) + ") = " + str(acos(a)))

        elif choice == '12':
            print("Arctangent")
            a = float(input("Enter a value: "))
            print("arctan(" + str(a) + ") = " + str(atan(a)))

        elif choice == '13':
            print("Factorial")
            a = float(input("Enter a number (non-negative): "))
            print(str(a) + "! = " + str(factorial(a)))

        elif choice == '14':
            print("Exiting Calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

calculator()