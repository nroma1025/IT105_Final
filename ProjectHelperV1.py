import random
import math

def CheatSheet():
    print('')
    playPoints = ['Pair-2', 'Three of a Kind-3', 'Four of a Kind-4', 'Nonconsecutive series-# cards in series', 'Sum to 15-2', 'Sum to 31-2', 'Last Card-1', 'Nobs-2']
    handPoints = ['Pair-2', 'Three of a Kind-6', 'Four of a Kind-12', 'Series-# cards in series', 'Sum to 15-2', 'Four card flush-4', 'Five card flush-5', 'Nibs-1']
    print("Points can be earned during play like so: ")
    print('')
    for i in range(0,len(playPoints)):
        print(playPoints[i])
    print('')
    print("Points can be earned in the hand and crib like so: ")
    print('')
    for i in range(0,len(handPoints)):
        print(handPoints[i])
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
    handPoints = ['Pair-2', 'Three of a Kind-6', 'Four of a Kind-12', 'Series-# cards in series', 'Sum to 15-2', 'Four card flush-4', 'Five card flush-5', 'Nibs-1']
    for i in range(0,len(handPoints)):
        print(handPoints[i])
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
#test for discard phase
# print('')
# print("Your hand: ")
# for i in range(0,len(playerHand)):
#     print(playerHand[i])
# print('')
# print("Computuer's hand: ")
# for i in range(0,len(comHand)):
#     print(comHand[i])
# print('')
# print('Crib: ')
# for i in range(0,len(cribHand)):
#     print(cribHand[i])

#Some random example code for accessing dicts
# print(playerHand.get(1))
# discardBool = False
# for i in range(0,len(playerHand)):
#     #print(playerHand[i])
#     card = playerHand[i]
#     cardVal = ProjectHelperV1.cribbageDict[card.value]
#     print(cardVal)

# comScore = 122


def HandScore(hand, card):
    newPoints = 0
    rankHand1 = []
    rankHand2 = []
    for i in range (0, len(rankHand1)):
        rankHand1[i] = rankDict[hand[i].value]
        rankHand2[i] = rankDict2[hand[i].value]
    rankHand1.sort()
    rankHand2.sort()
    pointHand = hand
    sumH = 0
    for i in range (0,len(pointHand)):
        pointHand[i] = cribbageDict[hand[i].value]
    #check for 15s
    for p in range (0,4):
        if p <= 3:
            for i in range ((p+1),5):
                if pointHand[p]+pointHand[i] == 15:
                    newPoints += 2
        if p <= 2:
            for i in range(p+2, 5):
                if pointHand[p]+pointHand[p+1]+pointHand[i] == 15:
                    newPoints += 2
        if p <= 1:
            for i in range(p+3, 5):
                if pointHand[p]+pointHand[p+1]+pointHand[p+2]+pointHand[i] == 15:
                    newPoints += 2
        if p <= 0:
            for i in range(p+4, 5):
                if pointHand[p]+pointHand[p+1]+pointHand[p+2]+pointHand[p+3]+pointHand[i] == 15:
                    newPoints += 2
    for i in range(0,5):
        sumH = sumH + pointHand[i]
    if sumH == 15:
        newPoints +=2
    return (int(newPoints))
    #check for series
    #3 series
    for i in range (0,3):
        if rankHand1[i+2] - rankHand1[i+1] == 1:
            if rankHand1[i+1] - rankHand1[i] == 1:
                newPoints += 3
    for i in range (0,2):
        if rankHand1[i] == rankHand1[i+1]:
            if rankHand1[i+3] - rankHand1[i+2] == 1:
                if rankHand1[i+2] - rankHand1[i+1] ==1:
                    newPoints += 3
        if rankHand1[i+1] == rankHand[i+2]:
            if rankHand1[i+1] - rankHand1[i] == 1:
                if rankHand[i+3] - rankHand[i+2] == 1:
                    newPoints += 3
        if rankHand1[i+2] == rankHand[i+3]:
            if rankHand1[i+2] - rankHand1[i+1] == 1:
                if rankHand1[i+1] - rankHand[i] == 1:
                    newPoints += 3
    #series of 4
    for i in range (0,1):
        if rankHand1[i+3] - rankHand1[i+2] == 1:
            if rankHand1[i+2] - rankHand1[i+1] == 1:
                if rankHand1[i+1] - rankHand1[i] == 1:
                    newPoints -= 2
    for i in range (0,1):
        if rankHand1[i] == rankHand1[i+1]:
            if rankHand1[i+4] - rankHand1[1+3] == 1:
                if rankHand1[i+3] - rankHand1[i+2] == 1:
                    if rankHand1[i+2] - rankHand1[i+1] ==1:
                        newPoints += 4
        if rankHand1[i+1] == rankHand[i+2]:
            if rankHand1[i+1] - rankHand1[i] == 1:
                if rankHand1[i+4] - rankHand1[i+3] == 1:
                    if rankHand[i+3] - rankHand[i+2] == 1:
                        newPoints += 4
        if rankHand1[i+2] == rankHand[i+3]:
            if rankHand1[i+2] - rankHand1[i+1] == 1:
                if rankHand1[i+1] - rankHand[i] == 1:
                    if rankHand1[i+4] - rankHand1[i+3] == 1:
                        newPoints += 4
        if rankHand1[i+3] == rankHand1[i+4]:
            if rankHand1[i+3] - rankHand[i+2] == 1:
                if rankHand1[i+2] - rankHand1[i+1] == 1:
                    if rankHand1[i+1] - rankHand1[i] == 1:
                        newPoints +=4
    #series of 5
    if rankHand1[5] - rankHand1[4] == 1:
        if rankHand1[4] - rankHand[3] == 1:    
            if rankHand1[3] - rankHand[2] == 1:
                if rankHand1[2] - rankHand1[1] == 1:
                    if rankHand1[1] - rankHand1[0] == 1:
                        newPoints -= 3
    #check for 4 card flush
    suitHand = []
    for i in range(0,6):
        suitHand[i] = suitDict[hand[i].suit]
    suitHand.sort()
    for i in range(0,2):
        if suitHand[i] == suitHand[i+1]:
            if suitHand[i+1] == suitHand[i+2]:
                if suitHand[i+2] == suitHand[i+3]:
                    newPoints += 4
    #check for 5 card flush
    if suitHand[0] == suitHand[1]:
        if suitHand[1] == suitHand[2]:
            if suitHand[2] == suitHand[3]:
                if suitHand[3] == suitHand[4]:
                    newPoints += 1
    #check for pairs
    for i in range (0,4):
        if rankHand1[i] == rankHand1[i+1]:
            newPoints += 2
    #check for trips
    for i in range (0,3):
        if rankHand1[i] == rankHand1[i+1] and rankHand1[i+1] == rankHand1[i+2]:
            newPoints += 2
    #check for quads
    for i in range(0,2):
        if rankHand1[i] == rankHand1[i+1] and rankHand1[i+1] == rankHand1[i+2] and rankHand1[i+2] == rankHand1[i+3]:
            newPoints += 2
    #check for nibs
    for i in range (0,6):
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