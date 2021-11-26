'''A simulation of an adaptation of the card game Go Fish.'''
from go_fish_functions import *
from stats import stats
import json

#Initialise record file. To be used if no record file exists already.
first_record = {"Player1": 0, "Player2": 0, "Draws": 0}

counter = 0

while counter < 100:
    #Deck is created and shuffled. Hands are dealt to players.
    game_deck = deck.create_deck()
    deck.shuffle_deck(game_deck)
    player1_cards = deck.deal_hand(game_deck, 7)
    player2_cards = deck.deal_hand(game_deck, 7)

    #Original cards dealt to players.
    # print(f'Player1 original hand: {player1_cards}\n')
    # print(f'Player2 original hand: {player2_cards}\n')

    #Inital pairs before players start.
    player1_pairs = initial_pairs(player1_cards)
    player2_pairs = initial_pairs(player2_cards)

    player_1_asked = []
    player_2_asked = []

    #Loop of game. Players taking turns based on rules.
    while len(game_deck) > 0 and len(player1_cards) > 0 and len(player2_cards) > 0:

        #player1 turn.
        player1_turn = turn(player1_cards, player2_cards, player1_pairs, game_deck, player_1_asked)

        #player2 turn.
        player2_turn = turn(player2_cards, player1_cards, player2_pairs, game_deck, player_2_asked)

    #Players pairs.
    # print(f'Player1 pairs: {player1_pairs}\n')
    # print(f'Player2 pairs: {player2_pairs}\n')

    #Player cards at the end of the game.
    # print(f'Player1 cards left: {player1_cards}\n')
    # print(f'Player2 cards left: {player2_cards}\n')

    #Cards remaining in deck.
    # print(f'Deck remaining: {len(game_deck)}\n')

    #Outcome of the game.
    if len(player1_pairs) > len(player2_pairs):
        # print(f'Player1 wins!')
        first_record["Player1"]+=1
    elif len(player2_pairs) > len(player1_pairs):
        # print(f'Player2 wins!')
        first_record["Player2"]+=1
    else:
        # print(f"It's a draw!")
        first_record["Draws"]+=1

    # print(f'Total Card Count: {len(player1_cards + player2_cards + player1_pairs + player2_pairs + game_deck)}')

    #Stats function
    stats(player1_pairs, player2_pairs, first_record)

    counter +=1

#New Stats
filename = 'stats.json'
with open(filename) as f:
    new_record = json.load(f)

print(f"New Record: {new_record}")