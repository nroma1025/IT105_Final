#works cited
    #https://pydealer.readthedocs.io/en/latest/usage.html#construct-a-deck
    #https://www.w3schools.com/python/python_dictionaries.asp
    #my bestest CS Friend

#To Do
    # - DONE - Describe rules of play
    # - DONE - make a cheat sheet for hands
    # make a program to count the user's hand
    # make a program to count the computer's hand
    # - DONE - make copies of hands to separate play points from hand points!
    # - DONE - go bool so that people can take consecutive turns if their partner has a go
    # - DONE - make a program to discard from the user and the computer to the crib
    # - DONE - make a program to count points from the play
    # - DONE (-ISH?) - make a program to reshuffle and deal the deck
    #Definite trouble areas: nonconsec-series, 'go's, determining whose turn
    # - DONE - Stage: Intro
    # - DONE - Stage: Deal
    # - DONE - Stage: Discard
    # - DONE - Stage: Play
    # Stage: Hand
    # Stage: Crib
    # Stage: End Round

import pydealer
import ProjectHelperV1 as helper
import random

# Stage: Intro
introChoice = input("Welcome to Cribbage! Would you like a description of the rules? [y/n]")
while introChoice != 'y' and introChoice != 'n':
    print("Not today, ISIS. Try a valid input.")
    introChoice = input("Welcome to Cribbage! Would you like a description of the rules? [y/n]")
if introChoice == 'y':
    helper.Instructions()
elif introChoice == 'n':
    print("You're ready to play!")

playerScore = 0
comScore = 0
playerDealer = 3
#change these back to 121 after test!
while playerScore < 4 and comScore < 4:
    # Stage: Deal
    deck = pydealer.Deck()
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
            helper.CheatSheet()
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
            helper.CheatSheet()
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
    communityStack = deck.deal(1)
    communityCard = communityStack[0]
    playerHand2 = playerHand
    comHand2 = comHand
    print('')
    print('Community Card: ' + str(communityCard))
    if (playerDealer % 2) == 1:
        print("You are the dealer, you play the first card.")
        print('')
        playerTurn = True
        if communityCard.value == 'Jack':
            print("Two points to dealer for Nobs!")
            playerScore += 2
        didPlayerDeal = True 
    else:
        print("The computer is the dealer, it will play first.")
        print('')
        if communityCard.value == 'Jack':
            print("Two points to computer for Nobs!")
            comScore += 2
        playerTurn = False
        didPlayerDeal = False  

    playList = []
    legalBool = False
    playSum = 0
    goPlayerBool = False
    goComBool = False
    playNextBool = False
    # Phase 2: If someone has cards, play continues
    while len(playerHand) != 0 and len(comHand) != 0:
        # If it's the payer's turn, bool = true
        if (playerTurn == True) or (goComBool == True) or playNextBool == True:
            #If they make a move that would make the play over 31, move is illegal
            legalBool = False
            #This loops player until they make a legal play
            while legalBool == False:
                print('Player turn.')
                for i in range(0,len(playerHand)):
                    print(playerHand[i])
                print('')
                if len(playerHand) == 0:
                    goPlayerBool = True
                    legalBool = True
                    playerTurn = False
                    pass
                cardPlay = (input("Select a card to play, 1-" + str(len(playerHand)) + " or type 'go' if no legal."))
                if cardPlay == 'go':
                    print("You pass the turn.")
                    legalBool = True
                    playerTurn = False
                    goPlayerBool = True
                    if goComBool == True:
                        print('')
                        print('You get a point for the go.')
                        print('')
                        playerScore += 1
                    else:
                        playNextBool = False
                    break
                cardPlay = int(cardPlay)
                if cardPlay>(len(playerHand)) or cardPlay<1:
                    print('Try again.')
                    pass
                cardPlay = int(cardPlay - 1)
                playList.append(playerHand[cardPlay])
                for i in range(0,len(playList)):
                    card = playList[i]
                    playSum = playSum + helper.cribbageDict[card.value]
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
                    playerScore += helper.PlayScore(playList)
                    print("Earned Points: " + str(playerScore))
                playSum = 0
        elif (playerTurn == False) or (goPlayerBool == True):
            legalBool = False
            turnCount = 0
            while legalBool == False and turnCount < 30:
                if len(comHand) == 0:
                    goComBool = True
                    legalBool = True
                    playerTurn = True
                    pass
                cardPlay = random.randrange(0,len(comHand))
                playList.append(comHand[cardPlay])
                for i in range(0,len(playList)):
                    card = playList[i]
                    playSum = playSum + helper.cribbageDict[card.value]
                if playSum > 31:
                    del playList[-1]
                elif playSum <= 31:
                    print("Computer plays " + str(comHand[cardPlay].value))
                    print('Computer move ACCEPTED: ')
                    print('Play Total: ' + str(playSum))
                    del comHand[cardPlay]
                    cardPlay = 0
                    legalBool = True
                    playerTurn = True
                    comScore += helper.PlayScore(playList)
                    print('')
                    print("Computer Points: " + str(playerScore))
                turnCount += 1
            if turnCount >= 30:
                print("Computer says, 'Go': ")
                playerTurn = True
                goComBool = True
                if goPlayerBool == True:
                        print('')
                        print('Computer gets a point for the go.')
                        print('')
                        playerScore += 1
                else:
                    playNextBool = True
            playSum = 0
        if goPlayerBool == True and goComBool == True:
            print("Play reset. Play total = 0")
            playList.clear()
            communityStack.empty()
            deck.empty()
            pass
        playerDealer += 1
    # Stage: Hand Scoring
    playerHand2.append(communityCard)
    comHand2.append(communityCard)

    print("")
    print("TEST: DISPLAYING HANDS")
    print(playerHand2)
    print(comHand2)
    print("")
    if didPlayerDeal == True:
        print('')
        print("Computer hand is calculated first.")
        

    if didPlayerDeal == False: