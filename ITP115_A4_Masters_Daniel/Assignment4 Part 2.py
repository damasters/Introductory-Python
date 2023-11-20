"""
Multi line comment
Name: Daniel Masters, Email: damaster@usc.edu
ITP 115, Spring 2020
Assignment 4 Part 2
This program features 5 different cases that award points based on unique set of winning numbers. The program
randomly selects a case as well as rolls a twenty sided dice. If the number rolled, matches the case's winning
number, the player is awarded 50 points, if not, the user does not receive any points.
"""
def main():
    #necessary to define 'random'
    import random
    #all players begin with zero points
    totalPoints = 0
    #for loop used to loop the game 10 times
    for y in range(10):
        #list variable used to store all winning number ranges
        list = []
        #dice variable used for rolling of the 20-sided dice utilizing psuedo-random number generator
        dice = random.randrange(1, 21)
        #case variable used for determining which case will be used via psuedo-random number generator
        case = random.randrange(1, 6)
        #if and elif statements to represent each of the 5 possible cases
        if case == 1:
            #printed the statements that show user what case is being played for and the winning numbers
            print("\nYou are currently playing for CASE 1")
            print("You will win for the following numbers:")
            #the winning numbers are all even numbers from 2-20
            #for loop used to loop over the range of even numbers
            for x in range(2, 21, 2):
                #print statement prints the list of numbers that the user will win for
                print(x, end = " ")
                #.append adds the list of numbers in the range from 2-20 to the list variable
                #this list will uitilized later in the code to see if user won any points
                list.append(x)
            #print statement used to begin a new line
            print("\n")
        #case 2-5 follow same logic as case one but with different ranges
        elif case == 2:
            print("\nYou are currently playing for CASE 2")
            print("You will win for the following numbers:")
            #range is for any odd number between 1-20
            for x in range(1, 20, 2):
                print(x, end=" ")
                list.append(x)
            print("\n")
        elif case == 3:
            print("\nYou are currently playing for CASE 3")
            print("You will win for the following numbers:")
            #range is for any number between 5 and 10 including 10
            for x in range(5, 11):
                print(x, end=" ")
                list.append(x)
            print("\n")
        elif case == 4:
            print("\nYou are currently playing for CASE 4")
            print("You will win for the following numbers:")
            #range is for any even number between 10 and 20
            for x in range(10, 21, 2):
                print(x, end = " ")
                list.append(x)
            print("\n")
        elif case == 5:
            print("\nYou are currently playing for CASE 5")
            print("You will win for the following numbers:")
            #range is for any multiple of three from 3 to 20
            for x in range(3, 21, 3):
                print(x, end = " ")
                list.append(x)
            print("\n")
        #print statement to show dice is rolling
        print("Now rolling ...")
        #will print number that was rolled
        print("You rolled a "+str(dice)+"!")
        #if else statment used to show that if the dice rolled the number that is in the list than the
        # player won points, if not the player is awarded 0 points
        if dice in list:
            totalPoints = totalPoints + 50
            print("You won 50 points! :)")
        else:
            print("You didn't win :(")
    # each time the player matches the number rolled with a winning number they gain 50 points
    # this is done using the totalPoints variable
    # the total points are displayed at the end of the game
    print("\nYour total score is: "+str(totalPoints))
    print("Thanks for playing!")
main()
