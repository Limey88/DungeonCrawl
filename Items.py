itemDict = {
	'potions' : {
		'name' : 'Potion',
		'plural_name' : 'Potions',
		'value' : 100,
		'effect' : "addHealth(100)",
	},
	'antidotes' : {
		'name' : 'Antidote',
		'plural_name' : 'Antidotes',
		'value' : 80,
		'effect' : "removeStatusEffect('Poisoned')",
	},
	'revives' : {
		'name' : 'Revive',
		'plural_name' : 'Revives',
		'value' : 300,
		'effect' : "removeStatusEffect('KO')",
	}
}

weaponDict = {
	'sword' : {
		'name' : 'Sword',
		'plural_name' : 'Swords',
		'custom name' : 'Excalibur',
		'attack' : 10,
		'value' : 200
	},
	'mace' : {
		'name' : 'Mace',
		'plural_name' : 'Maces',
		'custom name' : 'Morning Star',
		'attack' : 12,
		'value' : 200
	}
}

armourDict = {
	'helmet' : {
		'name' : 'Helmet',
		'plural_name' : 'Helmets',
		'defence' : 10,
		'value' : 200
	},
	'chest_plate' : {
		'name' : 'Chest Plate',
		'plural_name' : 'Chest Plates',
		'defence' : 15,
		'value' : 200
	}
}

keyItems = {
	'note_from_king' : {
		'for_sale' : False,
		'remove_on_use' : True
	}
}

catalogueDict = itemDict.copy()
catalogueDict.update(armourDict)
catalogueDict.update(weaponDict)
catalogueDict.update(keyItems)