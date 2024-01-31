import random

from card_game import card


'''
Deck class
* instantiate a new deck
    * create all 52 card objects
    * hold as a list of card objects
* shuffle a deck through a method call
    *random library shuffle() function
* deal cards from the deck object

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks  = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten', 'Jack','Queen','King','Ace')  
'''

class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in card.suits:
            for rank in card.ranks:
                # create the card object
                created_card = card.Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    #grabs a card from the deck
    def deal_one(self):
        return self.all_cards.pop()




