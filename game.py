from card_game.card import Card
from card_game.deck import Deck
from card_game.player import Player
from card_game.card import Card

'''
Game logic

2 instances of player class, player 1 and player 2
instance of a new deck 
shuffle deck
split deck between player 1 and 2 
check if someone has lost - check for 0 cards 
while game_on = true
    each player draws a card 
    compare cards
    depending on who won - player wins both card and  add both cards to the bottom of the player's stack
    while at_war 
        player needs to draw 5 additional cards 
        compare
        player that won has the cards added 
        
    check if player has lost
    player also loses if they don't have at least 5 cards to play the war 

'''
# Game setup
player_one = Player('player1')
player_two = Player('player2')

new_deck = Deck()
new_deck.shuffle()

#split deck between player 1 and 2
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

round_num = 0
while game_on:
    round_num += 1
    print(f'Round {round_num}')
    if len(player_one.all_cards) == 0:  #Cards face down
        print('Player One, out of cards! Player Two Wins!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Play Two, out of cards!, Player One Wins!')
        game_on = False
        break

    #Start a new round
    player_one_cards = []  #current card in play
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards) #Player one gets all their card back
            player_one.add_cards(player_two_cards) #Player one adds the addition of player 2 cards
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards((player_two_cards))

            at_war = False
        else:
            print('WAR!')

            if len(player_one.all_cards) < 5:
                print('Player one unable to declare war')
                print('Player two wins!')
                game_on = False
                break

            if len(player_two.all_cards) < 5:
                print('Player two unable to declare war')
                print('Player one wins!')
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())  #remove 5 cards
                    player_two_cards.append(player_two.remove_one())



