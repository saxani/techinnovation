#Simple version of blackjack
import random

#Open the cards file
cards = open('cards.txt', 'r')
cardsString = cards.read();
cardsList = cardsString.split('\n')

playAgain = "y"

#Can keep playing
while playAgain == "y":

    #New list that can be deleted after game and starts over
    handList = [] + cardsList

    #User/dealer hand lists and points
    userHand = []
    dealerHand = []
    userPoints = 0
    dealerPoints = 0

    #Starting cards for user
    card1 = random.choice(handList)
    handList.remove(card1)
    userHand.append(card1)
    card2 = random.choice(handList)
    handList.remove(card2)
    userHand.append(card2)

    #Starting card for dealer
    card3 = random.choice(handList)
    dealerHand.append(card3)
    handList.remove(card3)


    #Just to repeat this code easier I made it a function
    def pointTracker(card, points):
        if card[0] == "A":
            points += 11
        elif card[0] == "1" or card[0].isalpha():
            points += 10
        else:
            points += int(card[0])

        return points


    #For each card user has off start add point total
    for card in userHand:
        userPoints = pointTracker(card, userPoints)

    #For one card dealer has, add point total
    dealerPoints = pointTracker(card3, dealerPoints)

    #Let user know what they can see
    print("Your hand is", userHand)
    print("You hand is worth", userPoints)
    print("Dealer card is", dealerHand)

    #As long as user doesn't go over 21, can keep playing
    while userPoints < 21:
        move = input("(h)it or (s)tay ")

        #If user wants hit, draws new card, removes from list, adds points
        if move == "h":
            newCard = random.choice(handList)
            userHand.append(newCard)
            handList.remove(newCard)
            userPoints = pointTracker(newCard, userPoints)
            print("Your hand is", userHand)
            print("You hand is worth", userPoints)

        #If wants to stay, leaves loop
        elif move == "s":
            break

        #Just incase user types something else
        else:
            print('Not valid input')

    #Loses if they go over 21
    if userPoints > 21:
        print("You lose!")
    #Wins if they get exactly 21
    elif userPoints == 21:
        print("You win!")

    #Else have dealer draw as long as they're less than 17
    else:
        while dealerPoints < 17:
            newCard = random.choice(handList)
            dealerHand.append(newCard)
            handList.remove(newCard)
            dealerPoints = pointTracker(newCard, dealerPoints)

        #Print scores
        print("Your score:", userPoints)
        print("Dealer score:", dealerPoints)
        print()
        
        #Figure out who wins
        if dealerPoints > userPoints and dealerPoints < 22:
            print("Dealer wins")
        else:
            print("You win")

    #Prompt to play again
    playAgain = input("Type 'y' to play again ")           





    
