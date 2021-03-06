#works cited
    ##### CITATION 1 #####
    # PyDealer: Playing Card Package. c2015 [cited 2020 APR 21]. 
    # This is an open-source library that took all of the legwork out of creating
    # a functional deck of cards. This was invaluable.
    # Available from: https://pydealer.readthedocs.io/en/latest/usage.html#construct-a-deck
    ##### CITATION 2 #####
    # Python Dictionaries. c2020 [cited 2020 APR 21].
    # I looked up dictionaries, their relevance to my project, and how to use them.
    # Available from: https://www.w3schools.com/python/python_dictionaries.asp
    ##### CITATION 3 #####
    # O'Shea, Ryan P, Stevens Institute of Technology '20. 2020 APR 18. 
    # Assistance given to the author, verbal discussion.  
    # Mr. O'Shea assisted me in the use of dictionaries to use for
    # comparing items within stacks to each other. Using the dictionaries,
    # i was able to construct the flow of logic for scoring hands and plays.
    # Mr. O'Shea was also instrumental in helping to troubleshoot runtime errors.
    # Toms River, NJ.

#To Do
    # - DONE - Describe rules of play
    # - DONE - make a cheat sheet for hands
    # - DONE - make a program to count the user's hand
    # - DONE - make a program to count the computer's hand
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
    # - DONE - Stage: Hand
    # - DONE - Stage: Crib
    # - DONE - Stage: End Round

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
playerDealer = 2
print('')
print("Player deals first.")
print('')
while playerScore < 30 and comScore < 30:
    # Stage: Deal
    playerDealer += 1
    deck = pydealer.Deck()
    deck.shuffle(2)
    playerHand = deck.deal(6)
    comHand = deck.deal(6)
    cribHand = deck.deal(0)
    
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
    cribHand.add(playerHand[discard1])
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
    cribHand.add(playerHand[discard1])
    del playerHand[discard1]

    # Phase 3: Computer discards cards
    discard1 = int(random.randint(0,5))
    #discardStr = comHand[discard1]
    cribHand.add(comHand[discard1])
    del comHand[discard1]
    discard1 = int(random.randint(0,4))
    #discardStr = comHand[discard1]
    cribHand.add(comHand[discard1])
    del comHand[discard1]

    # Stage: Play
    # Phase 1: Determine who plays first
    communityStack = deck.deal(1)
    communityCard = communityStack[0]
    playerHand2 = deck.deal(0)
    comHand2 = deck.deal(0)
    for i in range(0,4):
        playerHand2.add(playerHand[i])
        comHand2.add(comHand[i])
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

    playList = deck.deal(0)
    legalBool = False
    playSum = 0
    goPlayerBool = False
    goComBool = False
    playNextBool = False
    # Phase 2: If someone has cards, play continues
    while len(playerHand) != 0 and len(comHand) != 0:
        # If it's the payer's turn, bool = true
        if ((playerTurn == True) or (goComBool == True) or playNextBool==True) and goPlayerBool != True:
            legalBool = False
            #This loops player until they make a legal play
            while legalBool == False:
                playNextBool = False
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
                        playNextBool = True
                    break
                cardPlay = int(cardPlay)
                if cardPlay>(len(playerHand)) or cardPlay<1:
                    print('Try again.')
                    pass
                cardPlay = int(cardPlay - 1)
                playList.add(playerHand[cardPlay])
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
                    print('')
                    print("Player Points: " + str(playerScore))
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
                playList.add(comHand[cardPlay])
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
                    print("Computer Points: " + str(comScore))
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
                        playNextBool = True
                else:
                    playNextBool = False
            playSum = 0
        if goPlayerBool == True and goComBool == True:
            print("Play reset. Play total = 0")
            goPlayerBool = False
            goComBool = False
            playList.empty()
            pass
    if playerTurn == True:
        print("Computer gets points for Last Card.")
        comScore += 1
    elif playerTurn == False:
        print("Player gets points for Last Card")
        playerScore += 1

    # Stage: Hand Scoring and Crib Scoring
    playerHand2.add(communityCard)
    comHand2.add(communityCard)
    cribHand.add(communityCard)

    if didPlayerDeal == True:
        print('')
        print("Computer hand is calculated first.")
        comScore += helper.HandScore(comHand2, communityCard)
        print("Computer hand worth " + str(helper.HandScore(comHand2, communityCard)))
        print("Computer Score: " + str(comScore))
        print('')
        print("Calculating Player Hand...")
        playerScore += helper.HandScore(playerHand2, communityCard)
        print("Player hand worth " + str(helper.HandScore(playerHand2, communityCard)))
        print("Player score: " + str(playerScore))
        print('')
        print("Calculating Player Crib...")
        playerScore += helper.HandScore(playerHand2, communityCard)
        print('Crib worth ' + str(helper.HandScore(playerHand2, communityCard)))
        print("Player score: " + str(playerScore))
    if didPlayerDeal == False:
        print('')
        print("Player hand is calculated first.")
        playerScore += helper.HandScore(playerHand2, communityCard)
        print("Player hand worth " + str(helper.HandScore(playerHand2, communityCard)))
        print("Player score: " + str(playerScore))
        print('')
        print("Calculating Computer Hand...")
        comScore += helper.HandScore(comHand2, communityCard)
        print("Computer hand worth " + str(helper.HandScore(comHand2, communityCard)))
        print("Computer Score: " + str(comScore))
        print('')
        print("Calculating Computer Crib...")
        comScore += helper.HandScore(comHand2, communityCard)
        print('Crib worth ' + str(helper.HandScore(comHand2, communityCard)))
        print("Computer score: " + str(comScore))

    print('')
    print("NEXT ROUND")
    print('')
    communityStack.empty()
    deck.empty()
if playerScore > comScore:
    print("Congrats! You Won!")
elif comScore > playerScore:
    print("Sorry, computer won.")