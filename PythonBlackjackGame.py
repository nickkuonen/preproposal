#Nick Kuonen - 2024
#Python Blackjack

import random

def deal():
    return random.randint(2, 11)

def score(cards):
    total = sum(cards)
    aces = cards.count(11)
    if total==21:
        print("BLACKJACK")
        return total       
    while total > 21 and aces > 0:
        total -= 10  
        aces -= 1  
    return total

def round(playerHand, dealerHand):
    print("Your Hand:", playerHand)
    print("Your Hand Value:", score(playerHand))
    print("Dealer's Hand:", dealerHand)
    print("Dealer's Hand Value:", score(dealerHand))

def blackjack():
    balance = 100
    while balance > 0:
        wager = int(input("Please, place your wager: "))
        balance -= wager
        dealerHand = [deal()]
        playerHand = [deal(), deal()]
        while True:
            round(playerHand,dealerHand)
            action = input("Do you want to hit, stand, or leave the table?: ")
            if action == "hit":
                playerHand.append(deal())
                if score(playerHand) <21:
                    continue
                break
            elif action == "stand":
                break
            elif action =="leave":
                balance += wager 
                print("Your total balance is now $", balance)
                return 
        winner(wager, balance, playerHand, dealerHand)

def winner(wager, balance, playerHand, dealerHand):
    while score(dealerHand) < 17:
        dealerHand.append(deal())
    round(playerHand, dealerHand)
    if score(playerHand) >21:
        print("You have busted and lost.")
    elif score(playerHand) > score(dealerHand):
        print("Congratulations, you have won.")
        balance += 2 * wager  
    elif score(dealerHand) >21:
        print("The dealer has busted, you have won.")
        balance += 2*wager  
    elif score(dealerHand) >score(playerHand):
        print("The dealer has won, you have lost.")
    elif score(playerHand) == score(dealerHand):
        print("It is a draw. No one has won.")
        balance += wager  
    print("Your total balance is now $",balance)
    if balance <=0:
        print("You lost all your money!")

print("You are starting off with $100 and going to play blackjack. Good Luck!")
blackjack()
