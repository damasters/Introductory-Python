"""
Multi line comment
Name: Daniel Masters, Email: damaster@usc.edu
ITP 115, Spring 2020
Assignment 9:
In the EPA mileage calculator assignment, the coder is to get the user input for the year that they would like to view
vehicle information for. Vehicle information is done through a read and write process that acquires the
min and max city MPG of all vehicles excluding vans, minivans or trucks.
"""
#all work is done in the main function
def main():
    #print statment to match the ample output
    print("Welcome to EPA Mileage Calculator")
    #ask user for input on the year they would like to view data for
    yearInput = input("What year would you like to view data for? (2008 or 2009): ")
    #if user inputs 2008, the 2008 file will be opened
    if yearInput == "2008":
        fileIn = open("epaVehicleData2008.csv", "r")
    #if userinputs 2009, the 2009 file will be opened
    elif yearInput == "2009":
        fileIn = open("epaVehicleData2009.csv", "r")
    #if the user does not input either of these they will be prompted to try again
    #user must enter a valid year after they making a mistake, if not the program will end
    else:
        print("*Invalid input, please try again!")
        yearInput = input("What year would you like to view data for? (2008 or 2009): ")
        if yearInput == "2008":
            fileIn = open("epaVehicleData2008.csv", "r")
        elif yearInput == "2009":
            fileIn = open("epaVehicleData2009.csv", "r")
        else:
            print("*Invalid input, please re-read directions and retry. Program will now end.")
            return
    #prompts the user too enter a filename of their liking. This saves their results to that filename
    saveResults = input("Enter the filename to save results to: ")
    #print statements to match the sample output. The program ends after this and all the information that the user
    #wanted is now being processed and saved with the code below
    print("Operation Success! Mileage data has been saved to "+saveResults)
    print("Thanks, and have a great day!")
    #made variable openList to begin the creation of a list
    openList = []
    #headerLine was created to skip the header of when reading the CSV file
    headerLine = fileIn.readline()
    #for loop create to iterate over the fileIn varaibale which is either for the 2008 or 2009 information
    for line in fileIn:
        #strip() strips the data of unnecessary indentation
        line = line.strip()
        #split() breaks down the large string into smaller strings using a comma
        dataList = line.split(",")
        #filters if the data does not carry the substring "van" or "trucks" then adds that information to openList
        if dataList[0] not in "van" or dataList[0] not in "trucks":
            openList.append(dataList)
        #initialize the min and max variables
        #make max equivalent to an unachievably high number
        #make min equivalent to an unachievably low number
        listMin = 100
        listMax = 0
        #loop through openList and find the city MPG
        for item in openList:
            #the MPG is found in the list at the 8th index
            mpg = dataList[8]  # was openList[8], program would not run
            #casted the MPG as an int to be able to compare it to the listMax ints
            intMpg = int(mpg)
            #if the mpg found at the index are greater than the listMax number than that number becomes the new listmax
            if intMpg > listMax:
                listMax = intMpg
            #if the mpg found at the index is less than the listMin, than it becomes the new listMin
            if intMpg < listMin:
                listMin = intMpg
        #maxMpg and minMpg list variables are constructed
        maxMpgList = []
        minMpgList = []
        #loops over the datalist
        for item in dataList:
            #at the datalist index 8, the number is saved as variable mpg
            mpg = dataList[8]  # was openList[8], program woud not run
            #mpg is then casted as an int
            intMpg = int(mpg)
            #if the int is equal to the listMax then append that value to the max list
            if intMpg == listMax:
                maxMpgList.append(item)
            #if the int is equal to the listMin then append that value to the min list
            if intMpg == listMin:
                minMpgList.append(item)
    #close the file
    fileIn.close()
    # open the write file with the saveResults variable as the fileOut variable
    fileOut = open(saveResults,"w")
    #print statements match the format given in the sample output
    #follow up each of these statements with a file = fileOut statement
    print("EPA City MPG Calculator "+yearInput, file = fileOut)
    print("---------------------------------", file = fileOut)
    #get the maximum mileage from the listMax variable which represent the largest value out of all the data
    print("Maximum Mileage (city): "+str(listMax), file = fileOut)
    #gets the information of the car(s) that produces the greatest mpg
    print("\t"+str(maxMpgList), file = fileOut)
    #gets the minimum mileage from the listMin variable which represents the smallest value out of all the data
    print("Minimum Mileage (city): "+str(listMin), file = fileOut)
    #gets the information of the car(s) that produces the smallest mpg
    print("\t"+str(minMpgList), file = fileOut)
    #close the write file
    fileOut.close()
#call main
main()


