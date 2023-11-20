"""
Multi line comment
Name: Daniel Masters, Email: damaster@usc.edu
ITP 115, Spring 2020
Assignment 6
Writing code for an airline that allows the user to be assigned a seat, look at the seating chart as well as print
out there boarding pass. System uses definition blocks, lists and loops to achieve a smooth interaction with the user as
well as catch any of their errors.
"""

def main():
    #empty list
    seats = []
    #total number of seats variable
    TOTAL_SEATS = 10
    #number of filled seats variable set to begin at zero
    numFilledSeats = 0
    #initialize seat map to "Empty" for empty seats
    for x in range(10):
        seats.append("Empty")
    #first definition block for assigning user's seat
    def assignSeat():
        #input variable for user's name
        userName = input("Please input your full name: ")
        numFilledSeats = 0
        #this gives a range to each "empty" in the list, numbering each one from 0-9
        rangeOfLenSeats = range(len(seats))
        #for loop, going over range of each empty in the list
        #if at the index of the range there is the word "Empty" that spot will be filled with the user's name
        for x in rangeOfLenSeats:
            if seats[x] == "Empty":
                seats[x] = userName
                #if the userName fills a spot than the numFilledSeats variable increases by 1
                numFilledSeats = numFilledSeats + 1
                #print statement to show that the action has been completed
                print("You have been assigned a seat!\n")
                break
        #If the numFilledSeats variable remains at 0 than that means all spots have been accounted for
        if numFilledSeats == 0:
            #thus print statement shows tells user to wait for the next flight
            print("No seating available, the next flight leaves in 3 hours.\n")
    #2nd definition block for printing the seat map
    def printSeatMap():
        #print statements to match the format of the output in directions
        print("***************************************")
        #created variable to show the range of total seats from 0-9
        rangeOfTotSeats = range(TOTAL_SEATS)
        #for loop goes over the range from 0-9
        for x in rangeOfTotSeats:
            #if in the seats list there is an index that says empty
            #print statement shows the seat number is empty
            #must cast to a string and add one to the variable x in order to be show the correctly numbered list
            if seats[x] == "Empty":
                print("\tSeat #"+str(x+1)+":\tEmpty")
            #else in that seats list index there is a name
            #then print the seat number as well as the name
            else:
                print("\tSeat #"+str(x+1)+":\t"+seats[x])
        print("***************************************\n")
    #definition block for printing the boarding pass
    def printBoardingPass():
        #print statements to show the user options to select from
        print("Please select a method to print your boarding pass.")
        print("Type '1' to get Boarding Pass by seat number.")
        print("Type '2' to get Boarding Pass by name.")
        #input statement for user to select one of two options
        userBpOption = input("> ")
        #string as the options that the if statements can draw from without having casting the input as an int
        #this sets up error checking for characters that are not numbers
        initialString = "12"
        #while loop used for error checking and will loop until the user types 1 or 2
        while userBpOption not in initialString:
            userBpOption = input("Input invalid, please enter either '1' or '2' based on the menu above: ")
        #if the user types one they will be prompted to enter a seat number
        if userBpOption == "1":
            seatNumber = input("Please enter your seat number: ")
            #if the user types a character that int in the alphabet they will be given the chance(s) to type a numeric value
            while seatNumber.isdigit() == False:
                seatNumber = input("Please enter the numeric value for your seat number: ")
            #when the user types a digit, code will see if the seat number they typed is in the string list 1-10
            #if it is not, a print statement will prompt the user that their input is invalid and suggest that the user
            #check the seating map to get the correct information
            #if the user inputs a number in the string the boarding pass will be printed out showing the seat number
            #and name of passenger
            if seatNumber.isdigit() == True:
                string = "12345678910"
                if seatNumber not in string:
                    print("The seat number you entered does not exist, check the seating map and try again.\n")
                if seatNumber in string:
                    print("\n======= BOARDING PASS =======")
                    print("\tSeat #: " + seatNumber)
                    print("\tPassenger Name: " + seats[int(seatNumber) - 1])
                    print("===============================\n")
        #if the user selects option number 2, they are prompted to input their name
        elif userBpOption == "2":
            passengerName = input("Please enter your full name: ")
            #variable used to put the passengers name in lowercase which will make it easier to match their name to the one
            #in the seats list
            passengerNameLower = passengerName.lower()
            #variable to hold the range of seats
            rangeOfLenSeats = range(len(seats))
            #filled seats variable begins at zero
            filledSeat = 0
            #for loop goes over the range of seats with all names/ "empty" in it
            for x in rangeOfLenSeats:
                #made names in the list lowercase to match with lowercase passenger names
                lowerCaseListName = seats[x].lower()
                #if the passengername in lower case form matches the lowercase passenger name than the filled seat
                #variable increase by one
                if passengerNameLower == lowerCaseListName:
                    filledSeat = x+1
                    #print statement includes the seat number which is the filled seat variable and the passengers name
                    print("\n======= BOARDING PASS =======")
                    print("\tSeat #: "+str(filledSeat))
                    print("\tPassenger Name: "+seats[int(filledSeat)-1])
                    print("=============================\n")
                    break
            #if the filled seat variable remains at 0 then that means the passenger was not on the list
            #print statement informs the user that this is the case
            if filledSeat == 0:
                print("No passenger with the name ""\""+passengerName+"\" was found.\n")
    #Formatting the loops/ combining all the def blocks
    #print statements to show the menu and the choices the user will choose from
    print(" 1: Assign Seat")
    print(" 2: Print Seat Map")
    print(" 3: Print Boarding Pass")
    print("-1: Quit")
    print("Please select a numerical value from the list above: ")
    #variable to input the user's choice
    userInput = input("\n> ")
    #string variable for the user's potential numbers
    menuString = "123"
    #if the user inputs numbers, negative numbers are returned as false in the .isdigit() function
    if userInput.isdigit() == True:
        #if the numbers are not in the string then it loop until user gives a value that is found in the string
        while userInput not in menuString:
            print("Please select an appropriate numerical value from the list above: ")
            userInput = input("\n> ")
            #if user opts to leave program than after only inputting incorrect values, the program allows for it
            if userInput == "-1":
                print("Thank you! Have a nice day!")
                # return function to end execution of function
                return
        #while the userInput is found in the string
        while userInput in menuString:
            #if the userInput is equal to 1
            if userInput == "1":
                #than do the assign seat definition function
                assignSeat()
                #after that is complete display the menu again
                print(" 1: Assign Seat")
                print(" 2: Print Seat Map")
                print(" 3: Print Boarding Pass")
                print("-1: Quit")
                print("Please select a numerical value from the list above: ")
                userInput = input("\n> ")
            #elif statement for if the user inputs the number 2
            elif userInput == "2":
                #sends to the printSeatMap def block
                printSeatMap()
                #menu displayed
                print(" 1: Assign Seat")
                print(" 2: Print Seat Map")
                print(" 3: Print Boarding Pass")
                print("-1: Quit")
                print("Please select a numerical value from the list above: ")
                userInput = input("\n> ")
            #elif statement for if the user inputs the number 3
            elif userInput == "3":
                #send to the printBoardingPass def block
                printBoardingPass()
                #print statments displayed after complete
                print(" 1: Assign Seat")
                print(" 2: Print Seat Map")
                print(" 3: Print Boarding Pass")
                print("-1: Quit")
                print("Please select a numerical value from the list above: ")
                userInput = input("\n> ")
        #else for when the user completes a task(s) but either wants to quit or makes a mistake
        else:
            #if the userInput is -1 then the program ends
            if userInput == "-1":
                print("Thank you! Have a nice day!")
                # return function to end execution of function
                return
            #if it is not -1, than program loops until an appropriate value is selected
            while userInput != "-1":
                print("Please select an appropriate numerical value from the list above: ")
                userInput = input("\n> ")
                #goes through the same exact menu loop as above
                while userInput in menuString:
                    if userInput == "1":
                        assignSeat()
                        print(" 1: Assign Seat")
                        print(" 2: Print Seat Map")
                        print(" 3: Print Boarding Pass")
                        print("-1: Quit")
                        print("Please select a numerical value from the list above: ")
                        userInput = input("\n> ")
                    elif userInput == "2":
                        printSeatMap()
                        print(" 1: Assign Seat")
                        print(" 2: Print Seat Map")
                        print(" 3: Print Boarding Pass")
                        print("-1: Quit")
                        print("Please select a numerical value from the list above: ")
                        userInput = input("\n> ")
                    elif userInput == "3":
                        printBoardingPass()
                        print(" 1: Assign Seat")
                        print(" 2: Print Seat Map")
                        print(" 3: Print Boarding Pass")
                        print("-1: Quit")
                        print("Please select a numerical value from the list above: ")
                        userInput = input("\n> ")
            #if user wants to quit after this while loop they have the option to
            if userInput == "-1":
                print("Thank you! Have a nice day!")
                #return function to end execution of function
                return
    #to account for when the user does not type a positive number
    elif userInput.isdigit() == False:
        #if the user opts to quit at the start
        if userInput == "-1":
            #program ending print statement
            print("Thank you! Have a nice day!")
            #return function to end execution of function
            return
        #when the user types characters that are not numbers at the very beginning than the program ends and tells
        #user to carefully read the instructions before attempting begin the program again
        else:
            print("Your input is invalid. Please restart the program and follow the menu options carefully.")
main()