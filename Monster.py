class Monster: 
	def __init__(self, **kwargs) : 
		self.level = kwargs.get('level', 3)
		self.attack = kwargs.get('attack', 3)
		self.defence = kwargs.get('defence', 3)