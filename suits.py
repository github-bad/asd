##
# suits.py
# GAmble gaMBle gaMBLe
# Dago

from random import choice, shuffle

def suits(partial_history)
    # Take the first character
    choice = input("Next suit? ").strip().lower()[0]

    print('-'*(len(partial_history)+2))
    print('', ''.join(partial_history))
    print('-'*(len(partial_history)+2))

    # Compare
    if SUITS_DICT[choice] == partial_history[-1]:
        print('Correct!')
        multiplier = 4

    else:
        print("Incorrect!")
        multiplier = 0

    return multiplier
# Dict will be used to convert user input into symbol
SUITS_DICT = {'s': '♤', 'h': '♡', 'c': '♧', 'd': '♢'}
