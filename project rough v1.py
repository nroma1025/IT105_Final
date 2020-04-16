#works cited
#https://pydealer.readthedocs.io/en/latest/usage.html#construct-a-deck

#To Do
# - DONE - Describe rules of play
# - DONE - make a cheat sheet for hands
# make a program to count the user's hand
# make a program to count the computer's hand
# make a program to discard from the user and the computer to the crib
# make a program to count points from the play
# - DONE (-ISH?) - make a program to reshuffle and deal the deck
#thoughts: have a list, append each time a card is played. compare ranks to detect for non-con series?
#thoughts: have a whole separate module to check for scoring conditions?
#thoughts: make a roll check to see if the computer will forget to count points based on difficulty
# - DONE - Stage: Intro
# - DONE - Stage: Deal
# Stage: Discard
# Stage: Play
# Stage: Hand
# Stage: Crib
# Stage: End Round


import pydealer
import ProjectHelperV1
import random

# Stage: Intro
introChoice = input("Welcome to Cribbage! Would you like a description of the rules? [y/n]")
while introChoice != 'y' and introChoice != 'n':
    print("Not today, ISIS. Try a valid input.")
    introChoice = input("Welcome to Cribbage! Would you like a description of the rules? [y/n]")
if introChoice == 'y':
    ProjectHelperV1.Instructions()
elif introChoice == 'n':
    print("You're ready to play!")

# Construct a Deck instance, with 52 cards.
deck = pydealer.Deck()
#initialize some variables
playerScore = 0
comScore = 0
playerDealer = 1
while playerScore < 121 and comScore < 121:
    # Stage: Deal
    print("Player deals first.")
    #make sure you set up something like a modulo. odd numbers, player deals. even, computer deals. +=1 after every round
    deck.shuffle(2)
    playerHand = deck.deal(6)
    comHand = deck.deal(6)
    cribHand = []
    
    # Stage: Discard
    # ATTN: Input cheat sheet option here somewhere
    discardBool = False
    while discardBool == False:
        for i in range(0,len(playerHand)):
            print(playerHand[i])
        discard1=int(input("Choose a card, 1-6, to send the the crib."))
        if discard1 > 6 or discard1 < 1:
            print('Try again.')
        else:
            discardBool = True    
    
    discard1 = int(discard1 - 1)
    cribHand.append(playerHand[discard1])
    del playerHand[discard1]

    discardBool = False
    while discardBool == False:   
        for i in range(0,len(playerHand)):
            print(playerHand[i])
        discard1=int(input("Choose a card, 1-5, to send the the crib."))
        if discard1 > 5 or discard1 < 1:
            print('Try again.')
        else:
            discardBool = True 
    # discardBool == False
    # discardStr = playerHand[discard1]
    # cribHand.append(discardStr)
    # playerHand.remove(discardStr)

    discard1 = int(discard1 - 1)
    cribHand.append(playerHand[discard1])
    del playerHand[discard1]
    
    # discard1 = int(random.randint(0,5))
    # discardStr = comHand[discard1]
    # cribHand.append(discardStr)
    # del comHand[discard1]
    # discard1 = int(random.randint(0,4))
    # discardStr = comHand[discard1]
    # cribHand.append(discardStr)
    # del comHand[discard1]

    print('')
    print("Your hand: ")
    for i in range(0,len(playerHand)):
        print(playerHand[i])
    print('')
    print("Computuer's hand: ")
    for i in range(0,len(comHand)):
        print(comHand[i])
    print('')
    print('Crib: ')
    for i in range(0,len(cribHand)):
        print(cribHand[i])
    comScore = 122