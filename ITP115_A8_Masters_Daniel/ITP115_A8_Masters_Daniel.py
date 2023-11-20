"""
Multi line comment
Name: Daniel Masters, Email: damaster@usc.edu
ITP 115, Spring 2020
Assignment 8: This assignment directs coder to construct a looping game of tictactoe based on the user's decision to
keep playing or quit. Coder must use definition function blocks to code for different parts of the game. The end product
features a functional board that reflects each players move by displaying x's and o's over the numerical value
the user picked. At the end a winner is displayed and the user is asked whether or not they would like to play again.
"""
#import the file from directory
import TicTacToeHelper
#list of strings saved as board_list
board_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

#def function with parameters board_list and spot to determine whether or not the user's input is valid
def isValidMove(board_list, spot):
    #if the user's input is a number
    if spot.isdigit() == True:
        #then that number is then turned into an integer
        number = int(spot)
        #if the integer lies within the range, but is an 'x' or an 'o' then the boolean True is returned
        #else the boolean True is returned
        if number in range(0, 9):
            if board_list[number] == "x" or board_list[number] == "o":
                return False
            else:
                return True
    #if the user input is not a number then the boolean: False is returned
    return False

#updateBoard function is used to update the board with the index corresponding to the user's numerical choice
def updateBoard(board_list, spot, playerLetter):
    #reassigned the user's input to an integer
    reassignment = int(spot)
    #reassigning the user's input allows for indexing which replaces the number on the board with the player's letter
    board_list[reassignment] = playerLetter

#this function connects the other two functions together as well as incorporates a function from the tictactoehelper
def playGame():
    #the move counter begins at zero
    move_counter = 0
    #list of strings created
    board_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    #first player automatically uses letter 'o'
    playerLetter = "o"
    #while the move_counter is less than 8
    while move_counter <= 8:
        #the uglyboard is printed from the tictactoehelper
        TicTacToeHelper.printUglyBoard(board_list)
        #user inputs numerical value to represent the spot they want to pick
        spot = input("Player "+playerLetter+" pick a spot: ")
        #if the value they choose is not on the board, the value is examined in the isValidMove function
        #the isValidMove function dreturns the boolean: False. Thus this while loops is activated until the user chooses
        #an appropriate value
        while isValidMove(board_list, spot) == False:
            print("Invalid number, please input a number from 0 to 8. Make sure your input has not been entered already.")
            spot = input("Player "+playerLetter+" pick a spot: ")
        #call the updateBoard which updates the uglyboard with the player's letter
        updateBoard(board_list, spot, playerLetter)
        #if else statement switches the player's turns. If the playerLetter is 'o' the next turn will be 'x' and vice-versa
        if playerLetter == "o":
            playerLetter = "x"
        else:
            playerLetter = "o"
        #after each switch the move_counter goes up by one
        move_counter = move_counter + 1
        #utilizing the tictactoehelper, the winner is checked for via the checkForWinner function
        winner = TicTacToeHelper.checkForWinner(board_list, move_counter)
        #if else statements that code for each winner and scenario
        #if the winner is player x, the uglyboard is updated and print statements declare the end of the game as well
        #as the winner
        if winner == "x":
            TicTacToeHelper.printUglyBoard(board_list)
            print("\nGame over!")
            print('Player x is the winner!')
            #break statement to break the loop
            break
        # if the winner is player o, the uglyboard is updated and print statements declare the end of the game as well
        # as the winner
        elif winner == "o":
            TicTacToeHelper.printUglyBoard(board_list)
            print("\nGame over!")
            print('Player o is the winner!')
            # break statement to break the loop
            break
        # if there is no winner, the uglyboard is updated and print statements declare the end of the game as well
        # as there being a stalemate
        elif winner == "s":
            TicTacToeHelper.printUglyBoard(board_list)
            print("\nGame over!")
            print("Stalemate reached!")
            # break statement to break the loop
            break
        #else if there is no winner than the game will continue until there is one or there is a stalemate
        else:
            if winner == "n":
                continue

#the main function utilizes a while loop which allows the user to play the game as many times as they would like
#if they decide they would like to quit they can simply type 'n' when prompted
def main():
    print("Welcome to Tic Tac Toe!")
    #making the variable userInput not case-sensitive
    userInput = "y" or "Y"
    while userInput == "y" or userInput == "Y":
        #playGame function will start the actual game
        playGame()
        #input function for user to type either 'y' or 'n'
        userInput = input("Would you like to play another round? (y/n): ")
        #if user types 'n' or 'N' then the program ends with print statement saying goodbye
        if userInput == "n" or userInput == "N":
            print("Goodbye!")
            #program break after goodbye
            break
        #if the user types 'y' or 'Y' then the program continues with the loop
        elif userInput == "y" or userInput == "Y":
            continue
        #else if the types something other than 'y', 'Y', 'n' or 'N' than a print statement is displayed and the program
        #ends
        else:
            print("You did not input the appropriate letter. Program will now end. Goodbye!")

main()