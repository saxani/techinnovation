#Shaun Axani
#02/01/2017
#CSCI-UA.0002-011
#Assignment #2, Problem 1

#Greeting before input
print("Hello! Let's split your bill.")
print()


#Get variables for getting 3 meals
mealOne = float(input('How much was meal #1? (enter as a number without dollar \
signs or commas): '))

mealTwo = float(input('How much was meal #2? (enter as a number without dollar \
signs or commas): '))

mealThree = float(input('How much was meal #3? (enter as a number without dollar \
signs or commas): '))

#Get Tip Amount variable
tipPercent = float(input('How much tip percentage would you like to leave? (enter number without percentage \
sign): '))

print('Thank!')
print()
print('-' * 32)
print ()

#Variable for tax percent
taxPercent = 8.875

#Total before tax/tip cost
#Getting this to figure out percentage of final price for each person
totalMealRaw = mealOne + mealTwo + mealThree

#Each meal percentage of total bill to use later to divide up the total
mealOnePercent = mealOne/totalMealRaw
mealTwoPercent = mealTwo/totalMealRaw
mealThreePercent = mealThree/totalMealRaw

#Calculate tip
tipAmount = totalMealRaw * (tipPercent/100)

#Calculate tax
taxAmount = totalMealRaw * (taxPercent/100)

#Total including tax and tip
total = totalMealRaw + tipAmount + taxAmount

#Meal one total owing, formatted to two decimal places
mealOneTotalAmount = format(total * mealOnePercent, '.2f')

#Meal one total owing, formatted to two decimal places
mealTwoTotalAmount = format(total * mealTwoPercent, '.2f')

#Meal one total owing, formatted to two decimal places
mealThreeTotalAmount = format(total * mealThreePercent, '.2f')

########OUTPUT########
'''I don't care if they nest formatting or do it earlier and make new variables'''

print(format('The total tip is', '26'), '$', format(tipAmount, '>5.2f'), sep='')
print(format('The total tax is', '26'), '$', format(taxAmount, '>5.2f'), sep='')
print(format('The total bill is', '26'), '$', format(total, '>5.2f'), sep='')
print(format('Person one should pay', '26'), '$', format(mealOneTotalAmount, '>5'), sep='')
print(format('Person two should pay', '26'), '$', format(mealTwoTotalAmount, '>5'), sep='')
print(format('Person three should pay', '26'), '$', format(mealThreeTotalAmount, '>5'), sep='')





