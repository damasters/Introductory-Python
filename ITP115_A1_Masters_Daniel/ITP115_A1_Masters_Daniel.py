"""
Multi line comment
Name: Daniel Masters
Email: damaster@usc.edu
Course: ITP 115
Description: Week 2
Creating a Madlibs Story using strings to input parts of speech as well as numerical values
"""

def main():
    properName= input("Enter an proper name: ")
    floatNumber= float(input("Enter a number with a decimal: "))
    adjective = input("Enter an adjective: ")
    intNumber= int(input("Enter a whole number: "))
    secondintNumber= int(input("Enter a second whole number: "))
    noun= input("Enter a noun: ")
    thirdintNumber= int(input("Enter a third whole number: "))
    verb= input("Enter a verb ending in -ing: ")
    bodypartNouns= input("Enter a body part noun: ")

    """ 
    This block of input takes parts of speech and numerical values from the user and defines it as a variable.
    Used int() in front of intNumber to signify casting which is needed to make sure the data type of the output is of an integer or float.
    By doing this we can now add let python add the numbers if needed.
    """

    print("As","\""+properName+"\"","continued running, the footsteps of the pursuer grew louder.")
    print("Panic began to settle in as","\""+properName+"\"","searched for ways to evade the pursuing foe.")
    print("A sign to the right of","\""+properName+"\"","read \"SAFETY\" followed by the distance of","\""+str(floatNumber)+"\"","miles.")
    print("After reading the sign","\""+properName+"\"","felt","\""+adjective+"\"","but disregarded such feelings to remain confident in completing the task at hand: win.")
    print("After","\""+str(intNumber)+"\"","minutes of running,","\""+properName+"\"","reached a","\""+str(secondintNumber)+"\"","foot tall","\""+noun+"\"","that blocked any possibilty of escape.")
    print("A dead end. \"This can't be! I have trained for","\""+str(thirdintNumber)+"\"","years only to fall short\"","\""+properName+"\"","proclaimed.")
    print("The","\""+verb+"\"","footsteps behind","\""+properName+"\"","came closer and closer until they suddenly stopped.")
    print("With a swift slap on the","\""+bodypartNouns+"\"","of","\""+properName+"\"","the pursuer yelled \"TAG YOU'RE IT\" and ran away laughing.")

    """
    These print statements utilize the input variables to make the story. Used "\""+ and +"\"" around all parts of speech.
    This separates the quotes used for the function of the print statement and the quotes used to go around each part of speech.
    The float number as well as the integer numbers needed to be casted back to string to avoid error.
    """

main()