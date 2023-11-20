"""
Multi line comment
Name: Daniel Masters, Email: damaster@usc.edu
ITP 115, Spring 2020
Assignment 7:
Rock, paper, scissors where the user is to choose from rock, paper or scissors and the computer is a random number
generator that selects its choice. The game that asks coder to create 6 different function blocks each of which
are responsible for different parts of the game. After coding for each block, the main function block is where the loop
is put together and incoprates all the different function blocks.
"""

#display menu function for displaying the rules of the game with the following print statements
def displayMenu():
    print("\nWelcome! Let's play rock, paper, scissors.")
    print("The rules of the game are:")
    print("\tRock smashes scissors")
    print("\tScissors cut paper")
    print("\tPaper covers rock")
    print("\tIf both the choices are the same, it's a tie")
    print("Please choose (0) for rock, (1) for paper or (2) for scissors.")

#this function gets gets a random inclusive integer from 0 to 2
def getComputerChoice():
    import random
    computerChoice = random.randint(0, 2)
    #returns the random integer
    return computerChoice

#this function gets the players choice, player must choose a number from 0 to 2
def getPlayerChoice():
    #input not casted as an int to allow for error checking
    playerChoice = input("> ")
    #string holds the different single values that the user can select
    string = "012"
    #if the user inputs a number or character not in the string than the program checks allows the user to re-enter
    #until they choose a correct one
    if playerChoice not in string:
        playerChoice = input("Your input is not valid, please enter a numerical value from the list above: ")
        while playerChoice not in string:
            playerChoice = input("Your input is not valid, please enter a numerical value from the list above: ")
    #returns a string that is either 0, 1 or 2
    return playerChoice

#playRound function operates based the random number from the computerChoice and the userinput from playerChoice
def playRound(computerChoice, playerChoice):
    #the case of rock smashes scissors and the computer wins
    if computerChoice == 0 and playerChoice == "2":
        return -1
    #the case of rock smashes scissors and the user wins
    elif computerChoice == 2 and playerChoice == "0":
        return 1
    #the case of scissors cut paper and computer wins
    elif computerChoice == 2 and playerChoice == "1":
        return -1
    # the case of scissors cut paper and user wins
    elif computerChoice == 1 and playerChoice == "2":
        return 1
    # the case of paper covers rock and comp wins
    elif computerChoice == 1 and playerChoice == "0":
        return -1
    # the case of paper covers rock and user wins
    elif computerChoice == 0 and playerChoice == "1":
        return 1
    # the case of both players choosing scissors, paper and rock
    elif computerChoice == 2 and playerChoice == "2":
        return 0
    elif computerChoice == 1 and playerChoice == "1":
        return 0
    elif computerChoice == 0 and playerChoice == "0":
        return 0

# continueGame function for after each round of rock, paper, scissors the user has the option of playing again or quiting
def continueGame():
    #user given two options to input either "y" or "n"
    userInput = input("Do you want to continue playing (y or n)? ").lower()
    #if the user inputs y it returns the boolean: True
    if userInput == "y":
        return True
    #if the user input n it returns the boolean: False
    elif userInput == "n":
        return False
    #if the user does not input "y" or "n" then there is error checking for that
    #allows for user to make 2 mistakes and still be able to input the correct value
    #after making a mistake on the third attempt the program ends.
    elif userInput != "y" or userInput != "n":
        userInput = input("Please select either 'y' or 'n' to continue: ").lower()
        if userInput == "y":
            return True
        elif userInput == "n":
            return False
        if userInput != "y" or userInput != "n":
            userInput = input("Please select either 'y' or 'n' to continue: ").lower()
            if userInput == "y":
                return True
            elif userInput == "n":
                return False
            else:
                print("Please read the instructions carefully. Program will now end.")

#the main function that combines all functions together
def main():
    #start out with the variables for the winner counters at 0 and the gameContinue at True to start the loop
    gameContinue = True
    userWinsCounter = 0
    compWinsCounter = 0
    drawsCounter = 0
    #while loop, loops as long as the gameContinue boolean returns True which is based on the user's choice
    while gameContinue == True:
        #menu is displayed showing the rules of the game
        displayMenu()
        #randomNum variable created to represent the computer's random number choice
        randomNum = getComputerChoice()
        #if and elif statments to match the numbers with their string equivalents
        #this was created for print statements that show what the computer selected
        if randomNum == 0:
            computerChoice = "rock"
        elif randomNum == 1:
            computerChoice = "paper"
        elif randomNum == 2:
            computerChoice = "scissors"
        #if elif statements to match the word sequivalent of the number
        #this was created for print statemtns that show what the user selected
        playerInput = getPlayerChoice()
        if playerInput == "0":
            playerChoice = "rock"
        elif playerInput == "1":
            playerChoice = "paper"
        elif playerInput == "2":
            playerChoice = "scissors"
        #print statements show what the user and computer chose
        print("\nYou chose", playerChoice+".")
        print("The computer chose", computerChoice+".")
        #variable play to represent the playRound with the parameters of randomNum and playerInput
        play = playRound(randomNum, playerInput)
        #if and elif statements for 1 for user win, -1 for computer win and 0 for tie which represent the winner in all
        # scenarios
        #if the user wins
        if play == 1:
            #if an elif statements based on the computer's choice in each scenario, since this is where the play
            #variable is equal to 0, all of these scenarios are win the user wins
            #print statements match the scenario and its display winner
            #the counter goes up by 1 evertime the user wins
            if randomNum == 2:
                print("Rock smashes scissors. You win!")
                userWinsCounter = userWinsCounter + 1
            elif randomNum == 1:
                print("Scissors cuts paper. You win!")
                userWinsCounter = userWinsCounter + 1
            elif randomNum == 0:
                print("Paper covers rock. You win!")
                userWinsCounter = userWinsCounter + 1
        #if the computer wins
        elif play == -1:
            #if and elif statements based on the computer's choice, since this is where the play variable is
            #equal to -1 that means the computer is the winner
            #print statements to show what happened and who won
            #counter for computer wins goes up by one each time
            if randomNum == 2:
                print("Scissors cuts paper. The computer wins!")
                compWinsCounter = compWinsCounter + 1
            elif randomNum == 1:
                print("Paper covers rock. The computer wins!")
                compWinsCounter = compWinsCounter + 1
            elif randomNum == 0:
                print("Rock smashes scissors. The computer wins!")
                compWinsCounter = compWinsCounter + 1
        #if there is a draw
        elif play == 0:
            #the draws counter goes up by one
            drawsCounter = drawsCounter + 1
            #print statement telling that the same item was chosen and there is a draw
            print("The same item was chosen. Draw!")
        #gameContinue referred to giving the user the option of playing again or quiting
        gameContinue = continueGame()
    #if the user decides they do not want to play anymore and the False boolean is returned, these print statements
    # are shown
    #the print statements show user the number of times the they won, the computer won and how many times they tied
    print("\nYou won", userWinsCounter,"game(s).")
    print("The computer won", compWinsCounter,"game(s).")
    print("You tied with the computer", drawsCounter,"time(s).")
    print("\nThanks for playing!")

main()