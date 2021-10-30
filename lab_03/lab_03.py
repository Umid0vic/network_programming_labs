# Network programming lab 3 - Python: Classes
# created by Osman Said 2021-10-27


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
		values = [ 'Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
			'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']			]

		suits = ['Spades','Hearts','Diamons','Clubs']
		
		value = values[self.getValue() + 1]
		suit  = suits[self.getSuit() + 1]
		return '{} of {}'.format(value, suit)

class CardDeck:
	def __init__(self):
		pass
	
	def shuffle(self):
		pass
	
	def getCard(self):
		pass
	
	def size(self):
		pass
	
	def reset(self):
		pass
