# Network programming lab 3 - Python: Classes
# created by Osman Said 2021-10-27

import random 


class Card:
	def __init__(self, suit, value):
		assert 1 <= suit <= 4 and 1 <= value <= 13
		self._suit = suit
		self._value = value
	
	def getValue(self):
		return self._value
	
	def getSuit(self):
		return self._suit
	
	def __str__(self):
		values = [ 
			'Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 
			'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King'
		]

		suits = ['Spades','Hearts','Diamons','Clubs']
		
		value = values[self.getValue() - 1]
		suit  = suits[self.getSuit() - 1]
		return '{} of {}'.format(value, suit)

class CardDeck:
	def __init__(self):
		self.reset()
	
	def shuffle(self):
		random.shuffle(self.cardDeck)
	
	def getCard(self):
		return self.cardDeck.pop()
	
	def size(self):
		return len(self.cardDeck)
	
	def reset(self):
		self.cardDeck = []
		suits = [1, 2, 3, 4]
		values = [*range(1, 14)]  #a list of numbers between 1 and 14. 14 not included
		for s in suits:
			for v in values:
				self.cardDeck.append(Card(s, v))

# testing code
deck = CardDeck()
deck.shuffle()
cardNum = 0
while deck.size() > 0:
	cardNum += 1
	card = deck.getCard()
	print("{}: Card {} has value {}".format(cardNum, card, card.getValue()))