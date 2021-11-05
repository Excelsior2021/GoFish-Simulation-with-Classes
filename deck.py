from random import shuffle, choice

class Deck():
    '''A model of a deck of cards and functions.'''
    def __init__(self):
        self.non_num_cards = ['ace', 'jack', 'queen', 'king']
        self.suits = ['clubs', 'diamonds', 'hearts', 'spades']

    def create_deck(self):
        '''Creates a full deck of cards.'''
        deck = []
        i = 0
        for x in range(2, 11):
            for y in self.suits:
                deck.append(f'{x} of {y.title()}')
        for x in self.non_num_cards:
            if x != 'ace':
                for y in self.suits:
                    deck.append(f'{x.title()} of {y.title()}')
        for x in self.suits:
            deck.insert(i, f'{self.non_num_cards[0].title()} of {x.title()}')
            i= i+1
        return deck
        
    def shuffle_deck(self, deck):
        '''Shuffles a deck of cards.'''
        shuffle(deck)
        return deck

    def deal_top_card(self, deck):
        '''Deals the top card of a deck.'''
        card = deck[0]
        deck.remove(card)
        return card

    def get_random_card(self, deck):
        '''Chooses a random card from the deck.'''
        card = choice(deck)
        deck.remove(card)
        return card

    def deal_hand(self, deck, hand_size):
        '''Returns a set of cards from a deck. Amount based on hand size.'''
        hand = []
        while len(hand) < int(hand_size):
            pick = choice(self.shuffle_deck(deck))
            hand.append(pick)
            deck.remove(pick)
        return hand

    def deal_hands(self, hand_size, num_hands=1):
        '''Returns sets of cards from a deck based on hand size.'''
        i = 0
        while i < num_hands:
            self.hands.append(self.deal_deck, hand_size)
            i += 1
        return self.hands