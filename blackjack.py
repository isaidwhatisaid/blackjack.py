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

player_hand = []
dealer_hand = []

def new_card(hand):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)
    return card

def card_display(hand):
    print('\nYou have: ')
    for card in hand:
        print(card)

def deal(hand):
    new_card(hand)
    new_card(hand)

def score(hand):
    total = 0
    for card in hand:
        total += int(card.value())
    if total > 21:
        for card in hand:
            if int(card.value()) == 11:
                total -= 10
                return total
        print('Your total is ' + str(total) + '! BUST!')
        quit()
    return total

def score_display(hand):
    x = score(hand)
    print("Your current total is: " + str(x) + '\n')
    if x == 21:
        print('Blackjack! You win!\n')
        quit()

def dealer_display():
    print('Dealer has:')
    for card in dealer_hand:
        print(card)

def choose(hand):
    while True:
        choice = input('Hit or Stay: ')
        if choice == 's':
            total = score(hand)
            print('You chose to stay. Your total score is: ' + str(total) + '\n\n' + '-'*50 + '\n')
            return total
        elif choice == 'h':
            print('\n' + '-'*50 + '\n\nYou drew the ' + str(new_card(hand)) + '\nCurrent hand:')
            for i in hand:
                print(i)
            print('Your current total is: ' + str(score(hand)) + '\n')
            continue
        else:
            print('Enter valid input')
            continue

def dealer(hand):
    while True:
        total = 0
        for card in hand:
            total += int(card.value())
        if total > 21:
            dealer_display()
            print('Dealer busts with ' + str(total) + '!\n\nYou win!\n')
            quit()
        elif total < 17:
            dealer_display()
            print('Dealer hits\n\n' + '-'*50 + '\n')
            new_card(dealer_hand)
            continue
        else:
            dealer_display()
            print('Dealer stays\n\n' + '-'*50 + '\n')
            return total

def winner(p,d):
    print('Dealer\'s total is: ' + str(d) + '\n')
    if d >= p:
        print('You lose!\n')
    else:
        print('You win!\n')

def play():
    deal(dealer_hand)
    print('\nDealer has:\n' + str(dealer_hand[0]) + '\n?')
    deal(player_hand)
    card_display(player_hand)
    score_display(player_hand)
    winner(choose(player_hand),dealer(dealer_hand))

play()


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
