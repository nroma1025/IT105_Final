#works cited
    #https://pydealer.readthedocs.io/en/latest/usage.html#construct-a-deck
    #https://www.w3schools.com/python/python_dictionaries.asp
    #my bestest CS Friend

#To Do
    # - DONE - Describe rules of play
    # - DONE - make a cheat sheet for hands
    # make a program to count the user's hand
    # make a program to count the computer's hand
    # make copies of hands to separate play points from hand points!
    # go bool so that people can take consecutive turns if their partner has a go
    # - DONE - make a program to discard from the user and the computer to the crib
    # make a program to count points from the play
    # - DONE (-ISH?) - make a program to reshuffle and deal the deck
    #thoughts: have a list, append each time a card is played. compare ranks to detect for non-con series?
    #thoughts: have a whole separate module to check for scoring conditions?
    #thoughts: make a roll check to see if the computer will forget to count points based on difficulty
    #thoughts: how am i going to let the game know if someone can take more consecutive turns?
    # can i sum up the 'play' list? do they have a number value? can i see if it's possible to sum up a user's hand to see if its a 'go'?
    #Definite trouble areas: nonconsec-series, 'go's, determining whose turn
    # If i can find a way to get into pydealer and turn 'value' from str to int, this would be good
    # - DONE - Stage: Intro
    # - DONE - Stage: Deal
    # - DONE - Stage: Discard
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
playerScore = 0
comScore = 0
playerDealer = 3
while playerScore < 121 and comScore < 121:
    # Stage: Deal
    print('')
    print("Player deals first.")
    print('')
    #make sure you set up something like a modulo. odd numbers, player deals. even, computer deals. +=1 after every round
    deck.shuffle(2)
    playerHand = deck.deal(6)
    comHand = deck.deal(6)
    cribHand = []
    
    # Stage: Discard
    # Phase 1: Player discard first card
    discardBool = False
    while discardBool == False:
        for i in range(0,len(playerHand)):
            print(playerHand[i])
        print('')
        print("Type 'h' to bring up cheat sheet.")  
        print('')  
        discard1=(input("Choose a card, 1-6, to send the the crib."))
        if discard1 == 'h':
            ProjectHelperV1.CheatSheet()
        else:
            discard1 = int(discard1)
            if discard1 > 6 or discard1 < 1:
                print('')
                print('Try again.')
                print('')
            else:
                discardBool = True    
    discard1 = int(discard1 - 1)
    cribHand.append(playerHand[discard1])
    del playerHand[discard1]
    # Phase 2: player discard second card
    discardBool = False
    while discardBool == False:   
        for i in range(0,len(playerHand)):
            print(playerHand[i])
        print('')
        print("Type 'h' to bring up cheat sheet.")
        print('')
        discard1=(input("Choose a card, 1-5, to send the the crib."))
        if discard1 == 'h':
            ProjectHelperV1.CheatSheet()
        else:
            discard1 = int(discard1)
            if discard1 > 5 or discard1 < 1:
                print('')
                print('Try again.')
                print('')
            else:
                discardBool = True 
    discard1 = int(discard1 - 1)
    cribHand.append(playerHand[discard1])
    del playerHand[discard1]
    # Phase 3: Computer discards cards
    discard1 = int(random.randint(0,5))
    discardStr = comHand[discard1]
    cribHand.append(discardStr)
    del comHand[discard1]
    discard1 = int(random.randint(0,4))
    discardStr = comHand[discard1]
    cribHand.append(discardStr)
    del comHand[discard1]

    # Stage: Play
    # Phase 1: Determine who plays first
    communityCard = deck.deal(1)
    print('')
    print('Community Card: ' + str(communityCard))
    if (playerDealer % 2) == 1:
        print("You are the dealer, you play the first card.")
        print('')
        playerTurn = True 
    else:
        print("The computer is the dealer, it will play first.")
        print('')
        playerTurn = False  

    playList = []
    legalBool = False
    playSum = 0
    goPlayerBool = False
    goComBool = False
    # Phase 2: If someone has cards, play continues
    while len(playerHand) != 0 and len(comHand) != 0:
        #find a way to sum everything in the playList, empty it if it's >= 31
        # If it's the payer's turn, bool = true
        if (playerTurn == True) or (goComBool == True):
            #If they make a move that would make the play over 31, move is illegal
            legalBool = False
            #This loops player until they make a legal play
            #still need to make scoring choices!
            while legalBool == False:
                for i in range(0,len(playerHand)):
                    print(playerHand[i])
                print('')
                cardPlay = (input("Select a card to play, 1-" + str(len(playerHand)) + " or type 'go' if no legal."))
                if cardPlay == 'go':
                    print("You pass the turn.")
                    legalBool = True
                    playerTurn = False
                    goPlayerBool = True
                    break
                cardPlay = int(cardPlay)
                if cardPlay>(len(playerHand)) or cardPlay<1:
                    print('Try again.')
                    break
                cardPlay = int(cardPlay - 1)
                playList.append(playerHand[cardPlay])
                for i in range(0,len(playList)):
                    card = playList[i]
                    playSum = playSum + ProjectHelperV1.cribbageDict[card.value]
                #This is the actual test for a legal play
                if playSum > 31:
                    print('Play over 31, move not possible. Try again.')
                    #deletes player's illegal choice
                    del playList[-1]
                elif playSum <= 31:
                    print('Legal move ACCEPTED: ')
                    print('Play Total: ' + str(playSum))
                    #legal move accepted, card removed form hand, players turn ends
                    del playerHand[cardPlay]
                    cardPlay = 0
                    legalBool = True
                    playerTurn = False
                playSum = 0
        elif (playerTurn == False) or (goPlayerBool == True):
            legalBool = False
            turnCount = 0
            while legalBool == False and turnCount < 30:
                cardPlay = random.randrange(0,len(comHand))
                playList.append(comHand[cardPlay])
                for i in range(0,len(playList)):
                    card = playList[i]
                    playSum = playSum + ProjectHelperV1.cribbageDict[card.value]
                if playSum > 31:
                    del playList[-1]
                elif playSum <= 31:
                    print('Computer move ACCEPTED: ')
                    print('Play Total: ' + str(playSum))
                    del comHand[cardPlay]
                    cardPlay = 0
                    legalBool = True
                    playerTurn = True
                turnCount += 1
            if turnCount >= 30:
                print("Computer says, 'Go': ")
                playerTurn = True
                goComBool = True
                break
            playSum = 0
        elif goPlayerBool == True and goComBool == True:
            break

    
    for i in range(0, len(playList)):
        print(playList[i])
    
    playerScore = 122