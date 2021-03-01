##
# gamblegamblegamble.py
# GAmble gaMBle gaMBLe
from random import choice, shuffle


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

SUITS_DICT = {'s': '♤', 'h': '♡', 'c': '♧', 'd': '♢'}
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

    playing = (True if input(message.format(balance)).strip().lower()
               in AFFIRMATIVES else False)

    # Exit check
    if not playing:
        continue

    print('-'*(HISTORY_MAX+2))
    print('', ''.join(suit_history[-HISTORY_MAX:]))
    print('-'*(HISTORY_MAX+2))

    # Pick card
    suit_history.append(deck.pop())

    # Take the first character
    choice = input("Next suit? ").strip().lower()[0]

    print('-'*(HISTORY_MAX+2))
    print('', ''.join(suit_history[-HISTORY_MAX:]))
    print('-'*(HISTORY_MAX+2))

    # Compare
    if SUITS_DICT[choice] == suit_history[-1]:
        print('Correct!')
        balance *= 4

    else:
        print("Incorrect!")
        balance = 0

print("Your final balance is ${}.".format(balance))
