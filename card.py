class Card():
    '''A model of a playing card and card functions.'''
    def __init__(self):
        self.non_num_cards = ['ace', 'jack', 'queen', 'king']
        self.suits = ['clubs', 'diamonds', 'hearts', 'spades']

    def choose_suit(self, deck, suit=None):
        '''Returns a list of cards specified by suit.
        if no suit is provided, the full deck is returned.'''
        list = []
        if suit:
            suit.lower()
            for x in deck:
                if suit.title() in x:
                    list.append(x)
        else:
            return deck
        return list

    def get_suit(self, card):
        '''Returns the suit of a the card.'''
        card = card.lower()
        for x in self.suits:
            if x in card:
                return x.title()

    def get_value(self, card):
        '''Returns the value of a card.'''
        for x in range(2,11):
            if str(x) in card:
                return x
        for x in self.non_num_cards:
            if x.title() in card:
                return x.title()

    def same_value(self, card1, card2, card3=None, card4=None):
        '''Returns True if up to four cards have the same value. 
            At least two cards need to be passed into the function.'''
        if card3 and card4:
            return self.get_value(card1) == self.get_value(card2) == self.get_value(card3) == self.get_value(card4)
        elif card3:
            return self.get_value(card1) == self.get_value(card2) == self.get_value(card3)
        else:
            return self.get_value(card1) == self.get_value(card2)

    def same_suit(self, card1, card2, card3=None, card4=None):
        '''Returns True if at least four cards have the same suit. 
            At least two cards need to be passed into the function.'''
        if card3 and card4:
            return self.get_suit(card1) == self.get_suit(card2) == self.get_suit(card3) == self.get_suit(card4)
        elif card3:
            return self.get_suit(card1) == self.get_suit(card2) == self.get_suit(card3)
        else:
            return self.get_suit(card1) == self.get_suit(card2)