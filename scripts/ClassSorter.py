#Use random module to randomly print names
import random

#The class list 
classNames = ["Ella", "Ethan", "David", "Cole", "Stella", "Revathi", "Benton", "Brigid",
"John", "Taylor", "Andres", "Diego", "Max", "Reed", "Emma", "Jacquelyn", "Eleanore"]

#Ask user how big the groups will be
groupSize = int(input("How big are the groups going to be? "))

#Team ordering, starts with team 1
teamNumber = 1

#While there are still people left in the original list
while len(classNames) > 0:
    #Start a new string for the team with the team number and a hyphen
    newTeam = str(teamNumber) + " - "

    #This will cycle through a for loop to get the amount of people per group
    for num in range(groupSize):
        #Randomly pick a name from the list
        name = random.choice(classNames)

        #Add that name to the variable for this team
        newTeam += name + " "

        #Remove that name from the list
        classNames.remove(name)

        #If the list is 0, exit the loop
        if len(classNames) == 0:
            break

    #Print that team
    print(newTeam)

    #Add a number to the team numbers
    teamNumber += 1
        
