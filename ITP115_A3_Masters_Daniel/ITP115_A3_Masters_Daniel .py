"""
Daniel Masters, damaster@usc.edu
ITP 115, Spring 2020
Assignment 3
Description:
Asking for users to list input values by utilizing while loops. With the while loops, if statements are used to interpret
the largest number, smallest number and average number of the user's input.
"""
def main():
    #When the user types "Y" or "y" the intial print statement will reappear and the user will then be able to type in
    #a new set of values for their second list of numbers
    secondInput= "Y" or "Y".lower()
    while secondInput== "Y" or "Y".lower():
        #print statement that gives the user directions
        print("Input an integer greater than or equal to 0 (-1 to quit): ")
        # started with inner while loop which accounts for all input integers from user
        #defining each variable that will be used in both while loops
        userInput= -2
        maxNum= 0
        minNum= ""
        sumNum= 0
        counter= 0
        #if userinput does not equal to -1 than the program will continue to run
        while userInput != -1:
            userInput = int(input("> "))
            #if user input is less than negative one than the program will ask the user to input a valid number
            while userInput < -1:
                print("Please input valid value greater than or equal to zero.")
                userInput = int(input("> "))
            if userInput != -1:
                #maximum input is achieved when the user inputs the greatest integer value
                if userInput > maxNum:
                    maxNum= userInput
                #minimum input is achieved when the user inputs the smallest integer value
                if minNum == "":
                    minNum= userInput
                #else something that is not equal to ""
                else:
                    #if statement within the else statement shows that if the userInput is smaller than minNum, it
                    #become the new minimum number
                    if userInput < minNum:
                        minNum= userInput
                #sumNum varaible is the all number(s) added together that to calculate min, max and avg
                #counter variable counts the input variables
                sumNum += userInput
                counter += 1
        #print statements to show the max, min and avg
        #the avg was calculated using the variables sumNum and counter
        print("The largest number is",maxNum)
        print("The smallest number is",minNum)
        print("The average number is",sumNum/counter)
        #second set of numbers will be calculated depending on users answer
        secondInput= input("Would you like to enter another set of numbers? (y/n): ")
        #if user inputs "Y" or "y" then the program will let user enter integer values once again
        #if user inputs "N" or "n" then the program will end
        if secondInput== "Y" or secondInput== "Y".lower():
            pass
        elif secondInput== "N" or secondInput== "N".lower():
            print("Goodbye!")
            break
main()