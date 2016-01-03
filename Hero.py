import Items

class Hero: 
	def __init__(self, **kwargs):
		self.name = kwargs.get('name', 'Hero')
		self.max_health = kwargs.get('max_health', 100)
		self.current_health = kwargs.get('current_health', 100)
		self.attack = kwargs.get('attack', 10)
		self.defence = kwargs.get('defence', 15)
		self.inventory = kwargs.get('inventory', {
				'gold' : 500,
				'items' : {
					'potions' : 5,
					'antidotes' : 1
				}
			})
		self.weapon = kwargs.get('weapon', 'sword')
		self.status = kwargs.get('status', None)



































