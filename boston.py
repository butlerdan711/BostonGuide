'''
Name: Daniel Butler
Date: 11/17/21
Description: Use dictionaries and lists to manage data
'''

import csv
global phase
phase = 0 #this variable keeps track of where the program is currently in order to keep entername() working properly and allow it to return to proper function
global quit
global dict
quit = True #allows main function to continously run until quit()
columns = ['Short Name', 'Name', 'Category', 'URL', 'Lat', 'Lon', 'Color']
MENU = """
=====================================================================
1. Find an attraction by name       2. Find attractions by category
3. Add an attraction                4. Edit an attraction
5. Delete an attraction             6. Display all attractions
7. Quit
=====================================================================
"""
attractions = []
dict = {} #the dictionary which holds the attraction info
shortnames = dict.keys()


def openfile():
    global attractions
    global dict
    '''
    Read the data from the data file
    Add the dictionaries to the list (attractions)
    '''
    global csvfile
    with open('boston.csv', newline='') as csvfile: #This function reads file to a list and then attributes the list into dictionary of each attraction
        for line in csvfile:
            words = line.rstrip().split(",")
            attractions.append(words)
        for z in attractions:
            dict[z[0]] = z[1:]


def findbyname():
    '''Find an attraction by its short name'''
    global phase
    phase = 1
    name = entername()

    for d in dict:          #This for loop prints attraction info only if correct input
        if name == d:
            print(f"\nShort Name: {name}")
            print(f"{'Name':<10}: {dict[name][0]}")
            print(f"{'Category':<10}: {dict[name][1]}")
            print(f"{'URL':<10}: {dict[name][2]}")
            print(f"{'LAT':<10}: {dict[name][3]}")
            print(f"{'LON':<10}: {dict[name][4]}")
            print(f"{'Color':<10}: {dict[name][5]}")


def findbycat():
    '''
    Find attractions by category
    '''

    cat = input("What type of attractions do you like to visit: [E]vents, [S]hopping, [T]ourism, or [U]niversity ").lower()
    if cat in 'estu': #This if statement decides which intro to print based on input
        if cat == 'e':
            print(f"\nEvent attractions in Greater Boston:")
        elif cat == 's':
            print(f"\nShopping attractions in Greater Boston:")
        elif cat == 't':
            print(f"\nTourism attractions in Greater Boston:")
        elif cat == 'u':
            print(f"\nUniversity attractions in Greater Boston:")
        print(f"{'Name':<40}{'URL':<10}") #prints actual headers
    if cat == 'e': #this if statement and the following ones identify which type of attraction was selected and then prints each of that type
        for d in dict:
            if dict[d][1].lower() == "events":
                print(f"{dict[d][0]:<40}{dict[d][2]:<10}")
    elif cat == 's':
        for d in dict:
            if dict[d][1].lower() == "shopping":
                print(f"{dict[d][0]:<40}{dict[d][2]:<10}")
    elif cat == 't':
        for d in dict:
            if dict[d][1].lower() == "tourism":
                print(f"{dict[d][0]:<40}{dict[d][2]:<10}")
    elif cat == 'u':
        for d in dict:
            if dict[d][1].lower() == "university":
                print(f"{dict[d][0]:<40}{dict[d][2]:<10}")
    else:
        print("Invalid input! Please try again.")
        findbycat()


def allattractions():
    global columns
    '''List and display all attractions'''
    #This function sorts the dictionary by short name and then prints each in alphabetical order
    sorted_dict = sorted(dict.keys())
    print(f"{columns[1]:<40}{columns[2]:<20}{columns[3]:<70}{columns[6]:<40}")
    for key in sorted_dict:
        if dict[key][0] != "Name":
            print(f"{dict[key][0]:<40}{dict[key][1]:<20}{dict[key][2]:<70}{dict[key][5]:<40}")


def addattraction():
    '''Add a new attraction'''
    newsn = input(str("Enter short name of new attraction: "))
    if newsn.lower() in shortnames: #checks for existant attractions
        print("Attraction already exists. Please try again.")
        addattraction()
    else:                           #breaks down inputted attraction info in a list and appends to dictionary as well as writes to boston.csv
        stuff = input(str("Please enter new attraction info (Name,Category,URL,Lat,Lon,Color): "))
        stuff2 = stuff.split(',')
        with open("boston.csv", "w") as csvfile:
            dict[newsn.lower()] = stuff2
            for key in dict.keys():
                csvfile.write("%s,%s\n"%(key,",".join(dict[key])))
        print(f"You have added a new attraction for {newsn}")


def editattraction():
    '''Change the marker color of an attraction'''
    global phase
    global dict
    change = 0
    phase = 3
    colorName = input("Please enter the short name of the attractions: ").lower() #asks for name of attraction to edit

    while colorName.lower() not in dict.keys(): #checks for short name here for efficiency instead of entername()
        print(f"Attraction {colorName} is not found. Please try again.")
        colorName = input("Please enter the short name of the attractions: ").lower()

    selectColor = input("Please enter new color ([g]reen, [b]lue, [o]range) Press ENTER to keep current color: ") #asks for color
    while selectColor not in 'gbo': #this loop handles incorrect inputs
        print("Invalid input. Please try again.")
        selectColor = input("Please enter new color ([g]reen, [b]lue, [o]range) Press ENTER to keep current color: ")

    def colors(selectColor): #function to handle actually changing color info
        global change
        if selectColor.lower() in 'gbo':
            if selectColor.lower() == 'g' and colorName.lower() in dict.keys():
                dict[colorName][-1] = 'green'
                print(f"You have changed the color for {colorName} to green")
            elif selectColor.lower() == 'b' and colorName.lower() in dict.keys():
                dict[colorName][-1] = 'blue'
                print(f"You have changed the color for {colorName} to blue")
                change = 1
            elif selectColor.lower() == 'o' and colorName.lower() in dict.keys():
                dict[colorName][-1] = 'orange'
                print(f"You have changed the color for {colorName} to orange")
            elif selectColor.lower() == '':
                print(f"You have kept the color for {colorName} the same")
        elif selectColor.lower() not in 'gbo':
            print("Invalid input! Please try again.")

    colors(selectColor) #calls function to change color info using appropriate color


def deleteattraction():
    '''Delete an attraction'''
    global phase
    global delname
    phase = 2
    global attractions
    delname = entername()

    if delname in dict.keys():  #deletes row assuming it exists
        print(f"This attraction ({delname}) has been deleted")
        del dict[delname]


def quit():
    '''Quit the program and write the info back to the data file'''
    global quit
    global columns

    with open("boston.csv", "w") as csvfile: #Writes dictionary back to file overwriting original info
        for key in dict.keys():
            csvfile.write("%s,%s\n"%(key,",".join(dict[key])))

    print("Have a nice day!")
    quit = False #Exits program


def entername():
    '''Process user input for the short name of an attraction'''
    global phase
    name = input("Please enter the short name of the attraction: ").lower()
    ki = dict.keys()
    if name not in ki:
        print(f"Attraction {name} is not found. Please try again.")
        if phase == 1:
            findbyname()   # code to handle the situation where the short name is not found
        elif phase == 2:
            deleteattraction()
        elif phase == 3:
            editattraction()
    return name #returns name if it is in the keys


def main():
    openfile()

    option = ""
    while True:
        print(MENU)
        option = input("Please select an option: ")
        while option not in '1234567':
            print("Invalid input! An option must be a number beween 1 and 7")
            option = input("Please select an option: ")

        option = int(option)
        if option == 1:
            findbyname()
        elif option == 2:
            findbycat()
        elif option == 3:
            addattraction()
        elif option == 4:
            editattraction()
        elif option == 5:
            deleteattraction()
        elif option == 6:
            allattractions()
        else:
            quit()

            break


while quit: #keeps program running until quit() is invoked
    main()
