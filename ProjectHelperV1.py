import random

def CheatSheet():
    playPoints = ['Pair-2', 'Three of a Kind-3', 'Four of a Kind-4', 'Nonconsecutive series-# cards in series', 'Sum to 15-2', 'Sum to 31-2', 'Last Card-1', 'Nobs-2']
    handPoints = ['Pair-2', 'Three of a Kind-6', 'Four of a Kind-12', 'Series-# cards in series', 'Sum to 15-2', 'Four card flush-4', 'Five card flush-5', 'Nibs-1']
    print("Points can be earned during play like so: ")
    for i in range(0,len(playPoints)):
        print(playPoints[i])
    print("Points can be earned in the hand and crib like so: ")
    for i in range(0,len(handPoints)):
        print(handPoints[i])
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