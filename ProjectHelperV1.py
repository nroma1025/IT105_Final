import random
import math
import pydealer

def CheatSheet():
    print('')
    playPoints = ['Pair-2', 'Three of a Kind-3', 'Four of a Kind-4', 'Nonconsecutive series-# cards in series', 'Sum to 15-2', 'Sum to 31-2', 'Last Card-1', 'Nobs-2']
    pointHand = ['Pair-2', 'Three of a Kind-6', 'Four of a Kind-12', 'Series-# cards in series', 'Sum to 15-2', 'Four card flush-4', 'Five card flush-5', 'Nibs-1']
    print("Points can be earned during play like so: ")
    print('')
    for i in range(0,len(playPoints)):
        print(playPoints[i])
    print('')
    print("Points can be earned in the hand and crib like so: ")
    print('')
    for i in range(0,len(pointHand)):
        print(pointHand[i])
    print('')
    return()
  
def Instructions():
    print("The objective of the game is to be the first to accrue 121 points")
    print("The dealer alternates between rounds. Each round, players will be dealt a six-card hand.")
    print("Players will discard two cards to 'The Crib'. The crib is an additional four-card hand for the dealer.")
    print("One card is dealt as a community card before play begins. Players discard before the community card is revealed.")
    print("Players will play cards, one at a time, during the 'play'. Points will be given during the play for the following: ")
    print('')
    continuePrompt = False
    while continuePrompt == False:    
        continuePrompt = input("Press 'y' to continue: ")
        if continuePrompt == 'y':
            continuePrompt = True
        else:
            continuePrompt = False
    playPoints = ['Pair-2', 'Three of a Kind-3', 'Four of a Kind-4', 'Nonconsecutive series-# cards in series', 'Sum to 15-2', 'Sum to 31-2', 'Last Card-1', 'Nobs-2']
    for i in range(0,len(playPoints)):
        print(playPoints[i])
    continuePrompt = False
    while continuePrompt == False:    
        continuePrompt = input("Press 'y' to continue: ")
        if continuePrompt == 'y':
            continuePrompt = True
        else:
            continuePrompt = False
    print('')
    print("As each player puts a card down, he/she adds his/her card's value to a running total. The total cannot go over 31.")
    print("If a player is unable to play a card without going over 31, they call 'Go'.")
    print("The other player will continue to play cards until they, too, are unable to stay under 31.")
    print("At this point, the players start a new total from 0 and play until all cards are played.")
    print("The play is done, and all points are added to the player's total. Next comes scoring the hand")
    print("Players will attempt to make the best 5-card hand with their hand and the community card.")
    print("The non-dealer scores his/her hand first. Points are awarded as follows: ")
    print('')
    continuePrompt = False
    while continuePrompt == False:    
        continuePrompt = input("Press 'y' to continue: ")
        if continuePrompt == 'y':
            continuePrompt = True
        else:
            continuePrompt = False
    pointHand = ['Pair-2', 'Three of a Kind-6', 'Four of a Kind-12', 'Series-# cards in series', 'Sum to 15-2', 'Four card flush-4', 'Five card flush-5', 'Nibs-1']
    for i in range(0,len(pointHand)):
        print(pointHand[i])
    continuePrompt = False
    while continuePrompt == False:    
        continuePrompt = input("Press 'y' to continue: ")
        if continuePrompt == 'y':
            continuePrompt = True
        else:
            continuePrompt = False
    print('')
    print("After the dealer counts his/her hand, he/she will count their crib as an additional hand.")
    print("After these three scoring phases, the deck will reshuffle and re-deal, and the dealer will switch.")
    print("Players can bring up the score cheat sheet with 'h' during a prompt.")
    print("Some notes: Nobs is when a jack is revealed as the community card. Points go to the dealer.")
    print("Nibs is when a jack in your hand is the same suit as the community card.")
    print("You cannot get points for summing to 31 AND getting the last card. 31 automatically implies a last card.")
    print("Series during play does not have to be consecutive. IE, 3-5-4 is a valid 3-card series.")
    print("Face cards are worth 10, Aces are worth 1.")
    print("Finally, you get points for each unique series. A hand of 3-3-4-5 is therefore 2 unique '3-4-5' series.")
    print("Now you're ready to play!")
    print('')

cribbageDict = {
    'Ace' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'Jack' : 10,
    'Queen' : 10,
    'King' : 10
}
rankDict = {
    'Ace' : 13,
    '2' : 1,
    '3' : 2,
    '4' : 3,
    '5' : 4,
    '6' : 5,
    '7' : 6,
    '8' : 7,
    '9' : 8,
    '10' : 9,
    'Jack' : 10,
    'Queen' : 11,
    'King' : 12
}
rankDict2 = {
    'Ace' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'Jack' : 11,
    'Queen' : 12,
    'King' : 13
}
suitDict = {
    "Spades": 4,
    "Hearts": 3,
    "Clubs": 2,
    "Diamonds": 1
}

def HandScore(hand, card):
    newPoints = 0
    deck = pydealer.Deck()
    handRank = deck.deal(0)
    handRankL = []
    for i in range (0, len(hand)):
        handRank.add(rankDict[hand[i].value])
        handRankL.append(handRank[i])
    handRankL.sort() 
    pointHand = deck.deal(0)
    pointHandL = []
    for i in range (0, len(hand)):
        pointHand.add(cribbageDict[hand[i].value])
        pointHandL.append(pointHand[i])
    pointHandL.sort() 
    sumH = 0
    #check for 15s
    for p in range (0,len(pointHandL)):
        if p <= 3:
            for i in range ((p+1),len(pointHandL)):
                if pointHandL[p]+pointHandL[i] == 15:
                    newPoints += 2
        if p <= 2:
            for i in range(p+2, len(pointHandL)):
                if pointHandL[p]+pointHandL[p+1]+pointHandL[i] == 15:
                    newPoints += 2
        if p <= 1:
            for i in range(p+3, len(pointHandL)):
                if pointHandL[p]+pointHandL[p+1]+pointHandL[p+2]+pointHandL[i] == 15:
                    newPoints += 2
        if p <= 0:
            for i in range(p+4, len(pointHandL)):
                if pointHandL[p]+pointHandL[p+1]+pointHandL[p+2]+pointHandL[p+3]+pointHandL[i] == 15:
                    newPoints += 2
    for i in range(0,len(pointHandL)):
        sumH = sumH + pointHandL[i]
    if sumH == 15:
        newPoints +=2
    return (int(newPoints))
    #check for series
    #3 series
    for i in range (0,3):
        if handRank[i+2] - handRank[i+1] == 1:
            if handRank[i+1] - handRank[i] == 1:
                newPoints += 3
    for i in range (0,2):
        if handRank[i] == handRank[i+1]:
            if handRank[i+3] - handRank[i+2] == 1:
                if handRank[i+2] - handRank[i+1] ==1:
                    newPoints += 3
        if handRank[i+1] == rankHand[i+2]:
            if handRank[i+1] - handRank[i] == 1:
                if rankHand[i+3] - rankHand[i+2] == 1:
                    newPoints += 3
        if handRank[i+2] == rankHand[i+3]:
            if handRank[i+2] - handRank[i+1] == 1:
                if handRank[i+1] - rankHand[i] == 1:
                    newPoints += 3
    #series of 4
    for i in range (0,1):
        if handRank[i+3] - handRank[i+2] == 1:
            if handRank[i+2] - handRank[i+1] == 1:
                if handRank[i+1] - handRank[i] == 1:
                    newPoints -= 2
    for i in range (0,1):
        if handRank[i] == handRank[i+1]:
            if handRank[i+4] - handRank[1+3] == 1:
                if handRank[i+3] - handRank[i+2] == 1:
                    if handRank[i+2] - handRank[i+1] ==1:
                        newPoints += 4
        if handRank[i+1] == rankHand[i+2]:
            if handRank[i+1] - handRank[i] == 1:
                if handRank[i+4] - handRank[i+3] == 1:
                    if rankHand[i+3] - rankHand[i+2] == 1:
                        newPoints += 4
        if handRank[i+2] == rankHand[i+3]:
            if handRank[i+2] - handRank[i+1] == 1:
                if handRank[i+1] - rankHand[i] == 1:
                    if handRank[i+4] - handRank[i+3] == 1:
                        newPoints += 4
        if handRank[i+3] == handRank[i+4]:
            if handRank[i+3] - rankHand[i+2] == 1:
                if handRank[i+2] - handRank[i+1] == 1:
                    if handRank[i+1] - handRank[i] == 1:
                        newPoints +=4
    #series of 5
    if handRank[5] - handRank[4] == 1:
        if handRank[4] - rankHand[3] == 1:    
            if handRank[3] - rankHand[2] == 1:
                if handRank[2] - handRank[1] == 1:
                    if handRank[1] - handRank[0] == 1:
                        newPoints -= 3
    #check for 4 card flush
    handSuit = deck.deal(0)
    for i in range(0,6):
        handSuit.add(suitDict[hand[i].suit])
    handSuit.sort()
    for i in range(0,2):
        if handSuit[i] == handSuit[i+1]:
            if handSuit[i+1] == handSuit[i+2]:
                if handSuit[i+2] == handSuit[i+3]:
                    newPoints += 4
    #check for 5 card flush
    if handSuit[0] == handSuit[1]:
        if handSuit[1] == handSuit[2]:
            if handSuit[2] == handSuit[3]:
                if handSuit[3] == handSuit[4]:
                    newPoints += 1
    #check for pairs
    for i in range (0,4):
        if handRank[i] == handRank[i+1]:
            newPoints += 2
    #check for trips
    for i in range (0,3):
        if handRank[i] == handRank[i+1] and handRank[i+1] == handRank[i+2]:
            newPoints += 2
    #check for quads
    for i in range(0,2):
        if handRank[i] == handRank[i+1] and handRank[i+1] == handRank[i+2] and handRank[i+2] == handRank[i+3]:
            newPoints += 2
    #check for nibs
    for i in range (0,5):
        if hand[i].value == "Jack" and suitDict[hand[i].suit] == suitDict[card.suit]:
            newPoints += 1


def Series3(aList):
        newPoints = 0
        newList = aList[-3:]
        newList.sort()
        if int(rankDict[newList[-1].value]) - int(rankDict[newList[-2].value]) == 1:
            if int(rankDict[newList[-2].value]) - int(rankDict[newList[-3].value]) == 1:
                print('')
                print('Series of 3: 3 pts')
                print('')
                newPoints+=3
        return newPoints
def Series4(aList):
    newPoints = 0
    newList = aList[-4:]
    newList.sort()
    seriesBool = False
    if int(rankDict[newList[-1].value]) - int(rankDict[newList[-2].value]) == 1:
        if int(rankDict[newList[-2].value]) - int(rankDict[newList[-3].value]) == 1:
            if int(rankDict[newList[-3].value]) - int(rankDict[newList[-4].value]) == 1:
                print('')
                print('Series of 4: 4 pts')
                print('')
                newPoints+=4
                seriesBool = True
    if seriesBool == False:
        if int(rankDict[newList[-1].value]) - int(rankDict[newList[-2].value]) == 1:
            if int(rankDict[newList[-2].value]) - int(rankDict[newList[-3].value]) == 1:
                print('')
                print('Series of 3: 3 pts')
                print('')
                newPoints+=3
    return newPoints
def Series5(aList):
    newPoints = 0
    newList = aList[-5:]
    newList.sort()
    seriesBool = False
    if int(rankDict[newList[-1].value]) - int(rankDict[newList[-2].value]) == 1:
        if int(rankDict[newList[-2].value]) - int(rankDict[newList[-3].value]) == 1:
            if int(rankDict[newList[-3].value]) - int(rankDict[newList[-4].value]) == 1:
                if int(rankDict[newList[-4].value]) - int(rankDict[newList[-5].value]) == 1:
                    print('')
                    print('Series of 5: 5 pts')
                    print('')
                    newPoints+=5
                    seriesBool = True
    if seriesBool == False:
        if int(rankDict[newList[-1].value]) - int(rankDict[newList[-2].value]) == 1:
            if int(rankDict[newList[-2].value]) - int(rankDict[newList[-3].value]) == 1:
                if int(rankDict[newList[-3].value]) - int(rankDict[newList[-4].value]) == 1:
                    print('')
                    print('Series of 4: 4 pts')
                    print('')
                    newPoints+=4
                    seriesBool = True
    if seriesBool == False:
        if int(rankDict[newList[-1].value]) - int(rankDict[newList[-2].value]) == 1:
            if int(rankDict[newList[-2].value]) - int(rankDict[newList[-3].value]) == 1:
                print('')
                print('Series of 3: 3 pts')
                print('')
                newPoints+=3
    return newPoints

def PlayScore(aList):
    points = 0
    #Check for 15's
    psum = 0
    for i in range (0, len(aList)):
        psum = psum + int(cribbageDict[aList[i].value])
    if psum == 15:
        points =+ 2
        print('')
        print('15: 2 pts')
        print('')
    #check for series
    if len(aList) == 3:
        points += Series3(aList)
    if len(aList) == 4:
        points += Series4(aList)
    if len(aList) == 5:
        points += Series5(aList)    
    #Check for pairs
    if len(aList) >= 2:
        card1 = aList[-1]
        card2 = aList[-2]
        if card1.value == card2.value:
            points += 2
            print('')
            print('Pair: 2 pts')
            print('')
    #Check for trips
    if len(aList) >= 3:
        card1 = aList[-1]
        card2 = aList[-2]
        card3 = aList[-3]
        if card1.value == card2.value and card1.value == card3.value:
            points += 3
            print('')
            print('3 of a Kind: 3 pts')
            print('')
    #Check for quads
    if len(aList) >= 4:
        card1 = aList[-1]
        card2 = aList[-2]
        card3 = aList[-3]
        card4 = aList[-4]
        if card1.value == card2.value and card1.value == card3.value and card1.value == card4.value:
            points += 4
            print('')
            print('4 of a Kind: 4 pts')
            print('')
    #check for 31
    psum = 0
    for i in range (0, len(aList)):
        psum = psum + int(cribbageDict[aList[i].value])
    if psum == 31:
        points =+ 2
        print('')
        print('31: 2 pts')
        print('')   
    return(points)