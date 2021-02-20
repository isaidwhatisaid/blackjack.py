import random

# Build the deck

suits = ['h','d','c','s']
values = ['2','3','4','5','6','7','8','9','10','j','q','k','a']
deck = []

class Card:

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        if self.name.endswith('h'):
            display = self.name.replace('h', '\u2665').upper()
        elif self.name.endswith('d'):
            display = self.name.replace('d', '\u2666').upper()
        elif self.name.endswith('c'):
            display = self.name.replace('c', '\u2663').upper()
        elif self.name.endswith('s'):
            display = self.name.replace('s', '\u2660').upper()
        return display
    
    def value(self):
        if self.name.startswith('j') or self.name.startswith('q') or self.name.startswith('k') or self.name.startswith('1'):
            x = 10
        elif self.name.startswith('a'):
            x = 11
        else:
            x = self.name[0]
        return x

for suit in suits:
    for value in values:
        card = Card(value+suit)
        deck.append(card)


# Functions to play the game

hand = []

def new_card(deck, hand):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)
    return card

def card_display(hand):
    for i in hand:
        print(i)

def deal():
    new_card(deck,hand)
    new_card(deck,hand)
    card_display(hand)

def score(hand):
    total = 0
    for card in hand:
        total += int(card.value())
    if total > 21:
        print('Your total is ' + str(total) + '! BUST!')
        quit()
    return total

def score_display(hand):
    print("Your current total is: " + str(score(hand)))

def choose():
    while True:
        choice = input('Hit or Stay: ')
        if choice == 's':
            print('You chose to stay. Your total score was: ' + str(score(hand)))
            break
        elif choice == 'h':
            print('You drew a ' + str(new_card(deck,hand)))
            for i in hand:
                print(i)
            print('Your current total is: ' + str(score(hand)))
            continue
        else:
            print('Enter valid input')
            continue

deal()
score_display(hand)
choose()





# for suit in suits:
#     for value in values:
#         card_value = None
#         if value == 'J' or 'Q' or 'K':
#             card_value = 10
#         elif value == 'A':
#             card_value = (1,11)
#         else: card_value = value
#         card_value_display = str(value)+suits[suit]
#         if value == 10:
#            card_string = '-'*8+'\n' + ('|'+' '*2 + card_value_display +' |'+'\n') + ('|'+' '*6+'|'+'\n')*3 + '-'*8
#            print(card_string)
#         else: 
#             card_string = '-'*8+'\n' + ('|'+' '*3 + card_value_display + ' |'+'\n') + ('|'+' '*6+'|'+'\n')*3 + '-'*8
#             print(card_string)






# print(card_frame)