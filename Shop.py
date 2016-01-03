import Items

class Shop: 
	def __init__(self, **kwargs):
		self.name = kwargs.get('name', 'Merchant')
		self.items = kwargs.get('items', [
			'potions',
			'antidotes',
			'revives',
			'sword',
			'helmet'
		])




































