##
# gamblegamble.py
# GAmble gaMBle

from random import choice, shuffle
from colours import *
from suits import *

# Set up cards
def setup_cards(): 
    SUITS = ['♤', '♡', '♧', '♢']
    CARDS_PER_SUIT = 13
    deck = []

    for card in range(CARDS_PER_SUIT):
        for suit in SUITS:
            deck.append(suit)

    shuffle(deck)
    
    return deck

deck = setup_cards()

BLACK_SUITS = ['♤', '♧']  # Else theyre red
suit_history = []
HISTORY_MAX = 6


# "yes" responses. Lowercase
AFFIRMATIVES = ['y', 'ye', 'yes', 'yeah', 'sure', 'r', 'b', '']

message = "Would you like to gamble? You current balance is ${}. "

# Fill history
for i in range(0, HISTORY_MAX):
    # Pick card
    suit_history.append(deck.pop())
    
# Set up loop
balance = 100
playing = True

while playing and balance > 0:
    if len(deck) <= 0:
        deck = setup_cards()
    
    playing = True if input(message.format(balance)).strip().lower() in AFFIRMATIVES else False
    
    if not playing:
        continue

    print('-'*(HISTORY_MAX+2))
    print('',''.join(suit_history[-HISTORY_MAX:]))
    print('-'*(HISTORY_MAX+2))
    
    # Pick card
    suit_history.append(deck.pop())

    # Take the first character.
    # r if red, b if black
    choice = input("Red or Black? ").strip().lower()[0]

    print('-'*8)
    print('',''.join(suit_history[-HISTORY_MAX:]))
    print('-'*8)

    if choice == 'b' and suit_history[-1] in BLACK_SUITS:
        print('Correct!')
        balance *= 2

    elif choice == 'r' and suit_history[-1] not in BLACK_SUITS:
        print('Correct!')
        balance *= 2
        
    else:
        print("Incorrect!")
        balance = 0

print("Your final balance is ${}.".format(balance))
