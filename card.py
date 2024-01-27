'''
Create a Card Class
Has 3 properties
1. understands the suit of the card - hearts, diamond, spade or club
2. understands the rank of the class
3. has integer value-  to compare one instance of the class to another
       e.g jack vs queen can use an integer value to determine which has a higher rank
'''
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks  = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten', 'Jack','Queen','King','Ace')
values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14
}
class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'








