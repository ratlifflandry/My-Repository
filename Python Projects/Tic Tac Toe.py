from datascience import *
import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#Introduction
print("Welcome to Tic Tac Toe!")

#Grid Function
def grid(TicTacToe):
    print(f" {TicTacToe[1]} | {TicTacToe[2]} | {TicTacToe[3]} ")
    print("---|---|---")
    print(f" {TicTacToe[4]} | {TicTacToe[5]} | {TicTacToe[6]} ")
    print("---|---|---")
    print(f" {TicTacToe[7]} | {TicTacToe[8]} | {TicTacToe[9]} ")

#Creating TicTacToe Dictionary
TicTacToe = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}
grid(TicTacToe)

#Current Player X or O
player = "X"
error = False

#Checks if input is valid
while error == False:
    player = input("Enter X or O:")

    if player == "X" or player == "O":
        print("It's your turn " + str(player))
        error = True
    else:
        print("Error! Try Again!")
        error = False

#Win for X's
win1 = False
#Win for O's
win2 = False

#Checks for double plays
Array = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False}

#While Loop
count = 0
while Array != {1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True}:

    #Checks if input is valid
    error = False

    while error == False:
        Number = input("Enter a number between 1-9:")

        try:
            if int(Number) in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                error = True
            elif int(Number) not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print("Invalid Input! Try Again!")
                error = False
        except:
            print("Invalid Input! Try Again!")

    #Checks if player tried to double play
    if Array[int(Number)] == True:
        if player == "X":
            player = "O" #Flips player back
            TicTacToe[int(Number)] = "O"
            print("Invalid Play! Try Again!")
        elif player == "O":
            player = "X" #Flips player back
            TicTacToe[int(Number)] = "X"
            print("Invalid Play! Try Again!")

    TicTacToe[int(Number)] = player #Updates grid
    grid(TicTacToe)  #Displays the updated board

    if Number == '1':
        Array[1] = True
        if player == "X":
            TicTacToe[1] = "X"
            print(TicTacToe)
        elif player == "O":
            TicTacToe[1] = "O"
            print(TicTacToe)

    elif Number == '2':
        Array[2] = True
        if player == "X":
            TicTacToe[2] = "X"
            print(TicTacToe)
        elif player == "O":
            TicTacToe[2] = "O"
            print(TicTacToe)

    elif Number == '3':
        Array[3] = True
        if player == "X":
            TicTacToe[3] = "X"
            print(TicTacToe)
        elif player == "O":
            TicTacToe[3] = "O"
            print(TicTacToe)

    elif Number == '4':
        Array[4] = True
        if player == "X":
            TicTacToe[4] = "X"
            print(TicTacToe)
        elif player == "O":
            TicTacToe[4] = "O"
            print(TicTacToe)

    elif Number == '5':
        Array[5] = True
        if player == "X":
            TicTacToe[5] = "X"
            print(TicTacToe)
        elif player == "O":
            TicTacToe[5] = "O"
            print(TicTacToe)

    elif Number == '6':
        Array[6] = True
        if player == "X":
            TicTacToe[6] = "X"
            print(TicTacToe)
        elif player == "O":
            TicTacToe[6] = "O"
            print(TicTacToe)

    elif Number == '7':
        Array[7] = True
        if player == "X":
            TicTacToe[7] = "X"
            print(TicTacToe)
        elif player == "O":
            TicTacToe[7] = "O"
            print(TicTacToe)

    elif Number == '8':
        Array[8] = True
        if player == "X":
            TicTacToe[8] = "X"
            print(TicTacToe)
        elif player == "O":
            TicTacToe[8] = "O"
            print(TicTacToe)

    elif Number == '9':
        Array[9] = True
        if player == "X":
            TicTacToe[9] = "X"
            print(TicTacToe)
        elif player == "O":
            TicTacToe[9] = "O"
            print(TicTacToe)

    #Logic for X wins
    if TicTacToe[1] == "X" and TicTacToe[2] == "X" and TicTacToe[3] == "X":
        win1 = True

    if TicTacToe[4] == "X" and TicTacToe[5] == "X" and TicTacToe[6] == "X":
        win1 = True

    if TicTacToe[7] == "X" and TicTacToe[8] == "X" and TicTacToe[9] == "X":
        win1 = True

    if TicTacToe[1] == "X" and TicTacToe[4] == "X" and TicTacToe[7] == "X":
        win1 = True

    if TicTacToe[2] == "X" and TicTacToe[5] == "X" and TicTacToe[8] == "X":
        win1 = True

    if TicTacToe[3] == "X" and TicTacToe[6] == "X" and TicTacToe[9] == "X":
        win1 = True

    if TicTacToe[1] == "X" and TicTacToe[5] == "X" and TicTacToe[9] == "X":
        win1 = True

    if TicTacToe[3] == "X" and TicTacToe[5] == "X" and TicTacToe[7] == "X":
        win1 = True

    #If X's wins
    if win1 == True:
        print("You win X's!")
        break

    #Logic for O wins
    if TicTacToe[1] == "O" and TicTacToe[2] == "O" and TicTacToe[3] == "O":
        win2 = True

    if TicTacToe[4] == "O" and TicTacToe[5] == "O" and TicTacToe[6] == "O":
        win2 = True

    if TicTacToe[7] == "O" and TicTacToe[8] == "O" and TicTacToe[9] == "O":
        win2 = True

    if TicTacToe[1] == "O" and TicTacToe[4] == "O" and TicTacToe[7] == "O":
        win2 = True

    if TicTacToe[2] == "O" and TicTacToe[5] == "O" and TicTacToe[8] == "O":
        win2 = True

    if TicTacToe[3] == "O" and TicTacToe[6] == "O" and TicTacToe[9] == "O":
        win2 = True

    if TicTacToe[1] == "O" and TicTacToe[5] == "O" and TicTacToe[9] == "O":
        win2 = True

    if TicTacToe[3] == "O" and TicTacToe[5] == "O" and TicTacToe[7] == "O":
        win2 = True

    #If O's win
    if win2 == True:
        print("You win O's!")
        break

    #Current player switch statement
    if player == "X":
        player = "O"
        Grid = "O"
        print("It's your turn " + str(player))
    else:
        player = "X"
        Grid = "X"
        print("It's your turn " + str(player))

    #Check if tie
    if Array == {1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True}:
        print("It's a tie!")