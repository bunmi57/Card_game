import random
from card_game import deck
from card_game.deck import Deck

'''
Contains Player class
* This class will be used to hold a player's current list of cards
* A player should be able to add or remove cards from their 'hand'(list of card objects)
* want the player to be able to add a single card or multiple cards to their list
* translating a Deck/Hand of cards with a top and bottom, to a python list


cards = ['A', 'B', 'C']  cards[0] = A, cards[-1] = 'C'
want to play cards from top of hand
* players class have a self.all_cards list
* A player plays a card from the top -  cards.pop(0) 
* player will add cards to the 'bottom' - cards.append()
*winning multiple rounds of war - player adding multiple cards uses extend
- original card - cards = ['B', 'C']
- new = ['x', 'z']   
- cards.extend(new) cards = ['B', 'C', 'X', 'Z']

'''

class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0) #removes card from the top of list

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            #a list of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            #a single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

'''
new_player = Player('Bunmi')
print(new_player) # Player Bunmi has 0 cards
new_deck = Deck()
mycard = new_deck.deal_one()
print(mycard) # Ace of clubs
new_player.add_cards(mycard)
print(new_player) #Player Bunmi has 1 cards
print(new_player.all_cards[0]) # Ace of clubs
new_player.add_cards([mycard,mycard,mycard, mycard])
print(new_player)
new_player.remove_one()
print(new_player)
'''
