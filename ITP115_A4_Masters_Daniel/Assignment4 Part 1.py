"""
Multi line comment
Name: Daniel Masters, Email: damaster@usc.edu
ITP 115, Spring 2020
Assignment 4 Part 1
User inputs any sentence they would like and the program returns how many of each letter in the alphabet
was used as well as any special characters (ie numbers, punctuation, etc EXCEPT spaces).
"""

def main():
        #made input variable for user to input their sentence
        userInput = input("Please enter a sentence: ")
        #created two sequence variables "alphabetWithSpace" and "alphabetWithOutSpace"
        alphabetWithSpace = "abcdefghijklmnopqrstuvwxyz "
        alphabetWithOutSpace = "abcdefghijklmnopqrstuvwxyz"
        #print statement indicates the breakdown of the characters used in the sentence
        print("\nHere is the character distribution:")
        #definition function used to set up function block using replacable variables: sentence and alphabet
        def char_counter(sentence, alphabet):
            #counter begins at 0
            counter = 0
            #for loop utilizes x in analyzing the sentence sequence which will be made into lower case form
            for x in sentence.lower():
                #when x is equal to the alphabet the counter increases by one
                if x == alphabet:
                    counter = counter + 1
            #return statement used to end the function block
            return counter
        #definition fuction block used to represent the special character cases, opposite of char_counter
        #now counts characters that are not found in the alphabet
        def special_counter(sentence, alphabet):
            #counter begins at 0
            counter = 0
            for y in sentence.lower():
                #cannot use != in this case and instead use 'not in' operator
                if y not in alphabet:
                    #for the letters that are not in the alphabet the counter increases by 1
                    counter = counter + 1
            return counter
        #introduced new variable asterisk
        asterisk = ""
        #saved results to variable 'special_count' to set up if statement
        special_count= special_counter(userInput, alphabetWithSpace)
        # if statement used to show that if there are no special characters, program displays "NONE"
        if special_count == 0:
            print("\nSpecial Characters: NONE")
        # else the number of users input will be represented by asterisks
        else:
            #for loop goes over the range from 0 and the amount of characters from the usersinput that are not equal
            # to a space or the alphabet. This is done by going over the special_counter function block
            for z in range(0, special_count):
                # asterisk amount calculated after for loop
                asterisk += "*"
            print("\nSpecial characters: "+asterisk)
        #varaible z goes over the alphabetWithoutSpace sequence utilizing the char_counter function block with the variables userInput and z
        #if statement shows that if the asteriskCount equals to 0 then "NONE" is printed next to the corresponding letter
        #otherwise the else statement takes all values greater than zero and distributes the appropriate amount of
        #asterisks to each letter of the usersinput
        for a in alphabetWithOutSpace:
            asteriskCount = char_counter(userInput, a)
            if asteriskCount == 0:
                print(a + ": " + "NONE")
            else:
                asteriskTwo = ""
                for b in range(0, asteriskCount):
                    asteriskTwo += "*"
                print(a + ": " + asteriskTwo)

main()







