"""
Multi line comment
Name: Daniel Masters
Email: damaster@usc.edu
Description: Week 3
Code for a Harry Potter Vending Machine that features four different items and gives customers appropriate amount of change
"""

def main():
#setting up the menu, allows for user to select one of the four options
    print("Select one of these four options")
    print("a) Butterbeer: 58 knuts")
    print("b) Quill: 10 knuts")
    print("c) The Daily Prophet: 7 knuts")
    print("d) Book of Spells: 400 knuts")
    selection = input("Please input the letter of your selection here: ")
#issue if statements for each of the four options, listing items and price for calculations after discount
    if selection== "a" or selection== "A":
        item= "Butterbeer"
        price= 58
    elif selection== "b" or selection== "B":
        item= "Quill"
        price= 10
    elif selection== "c" or selection== "C":
        item= "The Daily Prophet"
        price= 7
    elif selection== "d" or selection== "D":
        item= "Book of Spells"
        price= 400
#The else statement states that if they enter a letter that does match the above if statement options, they are automatically assigned option c.
    else:
        print("ERROR, your selection was invalid. You have been auto-assigned option c.")
        item= "The Daily Prophet"
        price= 7
#applying discount for customers that share their purchase on Instagram.
    instagram= input("Do you want to share this on Instagram: Yes or No? ")
    if instagram== "Yes" or instagram== "yes":
        discount= 5
        print("Thank you, you have received a 5 Knut discount on your purchase.")
    elif instagram== "No" or instagram== "no":
        discount= 0
#for those that do not enter "Yes", "yes", "No" or "no" they will not be given a discount.
    else:
        discount= 0
        print("Input invalid.")
#calculate the change for the purchase.
#casted each of the inputs as integers to enable addition subtraction, multiplicatio, division, etc.
    print("Input the number of each coin you would like to pay with:")
#ask customer how much of each coin they would like to pay with.
    inputgalleons= int(input("How many Galleons would you like to pay with? "))
    inputsickles= int(input("How many Sickles would you like to pay with? "))
    inputknuts= int(input("How many Knuts would you like to pay with? "))
#total amount of Knuts is the input function times their respective conversion factors
#this also must be casted as an integer
    totalknuts= int((inputgalleons * 493) + (inputsickles * 29) + inputknuts)
    change= int(totalknuts - price + discount)
#used integer division for galleons and sickles then modulus for the remainding galleons
#with the remaining amount, split it among the sickles and knuts by using integer division for sickles and modulus for knuts
    galleons= change // 493
    remaindergalleons= change % 493
    sickles= remaindergalleons // 29
    knuts= remaindergalleons % 29
#print statement tells customer what they are paying for as well the discount of knuts that has been applied to their account.
#converted the values to string statements and added quotations around them using the same format as last assignment.
    print("You paid with","\""+str(inputgalleons)+"\"","Galleons","\""+str(inputsickles)+"\"","Sickles and","\""+str(inputknuts)+"\"","Knuts for the item","\""+str(item)+"\"","with a price of","\""+str(price)+"\"","Knuts.")
    print("A discount of","\""+str(discount)+"\"","Knuts has been awarded to your account as well.")
#print statment tells customer their change given in galleons, sickles and knuts.
    print("Your change comes out to","\""+str(change)+"\"","Knuts which equates to","\""+str(galleons)+"\"","Galleon(s)","\""+str(sickles)+"\"","Sickle(s) and ","\""+str(knuts)+"\"","Knut(s). Thank you.")
main()
