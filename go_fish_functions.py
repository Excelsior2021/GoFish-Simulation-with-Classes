from card import Card
from deck import Deck

from random import choice

card = Card()
deck = Deck()

def initial_pairs(hand):
    '''Returns a list of pairs of values.'''
    pairs = []
    for cardx in hand:
        for cardy in hand:
            if card.get_value(cardx) == card.get_value(cardy) and card.get_suit(cardx) != card.get_suit(cardy) and cardx not in pairs and cardy not in pairs:
                pairs.append(cardx)
                pairs.append(cardy)
    for cardz in pairs:
        hand.remove(cardz)
    return pairs

def pairs(hand, pairs):
    '''Returns a list of pairs of values.'''
    for cardx in hand:
        for cardy in hand:
            if card.get_value(cardx) == card.get_value(cardy) and card.get_suit(cardx) != card.get_suit(cardy) and cardx not in pairs and cardy not in pairs:
                pairs.append(cardx)
                pairs.append(cardy)
    for cardz in pairs:
        if cardz in hand:
            hand.remove(cardz)

def ask_value(asker_hand, askee_hand, asker_pairs):
    '''Player asks for a value of a card they have in their hand.'''
    if len(asker_hand) > 0 and len(askee_hand) > 0:
        pick = choice(asker_hand)
        value = card.get_value(pick)
        for card_1 in askee_hand:
            if value == card.get_value(card_1):
                asker_pairs.append(pick)
                asker_pairs.append(card_1)
                asker_hand.remove(pick)
                askee_hand.remove(card_1)
                return True

def deal_card(asker_hand, asker_pairs, game_deck):
    '''Deals top card from the deck and compares value with player ask or with another value in player hand. 
        If no matches, card added to player hand.'''
    if len(game_deck) > 0:
        pick = deck.deal_top_card(game_deck)
        value = card.get_value(pick)
        if len(asker_hand) > 0:
            player_ask = choice(asker_hand)
            if value == card.get_value(player_ask):
                asker_pairs.append(pick)
                asker_pairs.append(player_ask)
                asker_hand.remove(player_ask)
                return True
            elif value != card.get_value(player_ask):
                for card_1 in asker_hand:
                    if value == card.get_value(card_1):
                        asker_pairs.append(pick)
                        asker_pairs.append(card_1)
                        asker_hand.remove(card_1)
                        break
                    else:
                        asker_hand.append(pick)
                        break
        else:
            asker_hand.append(pick)

def again(asker_hand, askee_hand, asker_pairs):
    '''Calls ask_value if player is to play again.'''
    if ask_value or deal_card:
        ask_value(asker_hand, askee_hand, asker_pairs)