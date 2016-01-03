#Imports
import Items
import Hero
import Monster
import Shop
import Level
import math
import random


#Global variables
gameOver = 'N'
healingItems = Items.itemDict
weaponItems = Items.weaponDict
catalogue = Items.catalogueDict

#Global Lists
responses = [
	"Not really sure what you mean by that",
	"Is... that even a thing?",
	"Now you're being stupid",
	"...",
	"We only speak English in these parts"
]

#Main object instances
mainChar = Hero.Hero()
shopOne = Shop.Shop()
enemey = Monster.Monster()

#Class variable
playerGold = mainChar.inventory['gold']
playerItems = mainChar.inventory['items']




def checkItems() :
	print("Your bag contains:")
	for item, amount in playerItems.items():
		print( str(amount) + "x " + catalogue[item]['name'])

def checkGold() :
	print("Your have {} Gold".format(playerGold))


def sellValue(item, amount = 1) :
	#finds the sell value of the items and returns a value relivant to the amount sold
	return int( ( (item['value']) / 5) * int(amount) )

def buyTotal(item, amount = 1) :
	#finds the sell value of the items and returns a value relivant to the amount sold
	return int( item['value'] * int(amount) )

def sell() :
	global playerGold
	#Function global variables
	mainCharItems = playerItems
	amountToSell = 1

	#displays all items in the command line
	for item, amount in mainCharItems.items() : 
		print( str(amount) + "x " + catalogue[item]['name'] + ": " + str( int( catalogue[item]['value'] * 0.2) ) ) 
	
	#Choose what item to sell
	itemToSell = input("What item do you want to sell? ")



	#Gets the items inforamtion from the catalogue
	if itemToSell != 'leave' : 
		try : 
			#Sees if item is in the catalogue to be sold
			catalogueTarget = catalogue[itemToSell]

			#Cheack to see how many the player actually has
			try : 
				amountAvailabel = mainCharItems[itemToSell]

				#If more than one can be sold, change that global variables amount
				if amountAvailabel > 1 :
					try : 
						amountToSell = int(input("How many do you want to sell? ") )
					except ValueError: 
						print("I need a number...")
						sell()

				#If player has requires amount to sell
				if amountToSell <= amountAvailabel :
					#relay information to player on items sold and the amount
					print("Sold {} {} for {}".format(amountToSell, itemToSell, sellValue(catalogue[itemToSell], amountToSell)) )

					#add gold based on a % of the cost of purchase
					playerGold += sellValue(catalogue[itemToSell], amountToSell)

					#reduce item value by set amount
					mainCharItems[itemToSell] -= amountToSell

					#if all items removed, pop item off player invetory dict
					if amountToSell == amountAvailabel :
						mainCharItems.pop(itemToSell)

					print("You now have {} Gold".format(playerGold) )
				else : 
					#Thrown if iplayer does not have enough to sell
					print("You don't have that many to sell")
			except KeyError: 
				print("You don't own that item, yet")

		except KeyError: 
			print("That isn't a real item, I'm afraid")

		sell()
	else : 
		print("Be seeing you again real soon.")



def buy() :
	global playerGold
	global playerItems
#Function import
	for item in shopOne.items:
		try : 
			print(catalogue[item]['name'] + ": " + str(catalogue[item]['value'] ) )
		except KeyError : 
			print('{}... what kind of item is that?'.format(item) )
	itemToBuy = input("What do you want to buy? ")
	if itemToBuy != 'leave' :
		try :
			if catalogue[itemToBuy] : 
				print("it does exsist")
				#Check if how many the player wants
				try : 
					amountToBuy = int(input("How many you want?"))
					#Check if they have enough gold
					if playerGold >= buyTotal(catalogue[itemToBuy]) :
						#add items to the players inventory
						#checkif player has items already
						if playerItems[itemToBuy] > 0 :
							playerItems[itemToBuy] += amountToBuy

						else : 
							playerItems[itemToBuy] = amountToBuy
						#if not, add new key/value pair to list
						#else, add item quantity to current item

						#take gold from player
						playerGold -= buyTotal(catalogue[itemToBuy], amountToBuy)

					else :
						print("Not enough cash for that, friend")
						buy()

					catalogue[itemToBuy]

				except ValueError : 
					print("That ain't a number, friend")
					buy()

			else : 
				print("We don't stock that, buddy")

		except KeyError: 
			print("We don't stock that item")
			buy()
	else : 
		print("Be seeing you again real soon.")


def randomResponse() : 
	randomIndex = math.floor( (random.random() ) * len(responses) ) 

	randomResponse = responses[randomIndex]

	print(randomResponse)


options = {

	'buy' : buy,
	'sell' : sell,
	'items' : checkItems,
	'gold' : checkGold,

}


def game() :
	global gameOver
	# print("Welcome to Dungeon Crawler.")
	# playerName = input("What should we call you? ")

	# mainChar.name = playerName

	# print("Welcome {}. Are you ready for an adventure?".format(mainChar.name))

	while gameOver == 'N' :

		try :
			func = input("What you wanting to do? ")
			if func == 'leave' :
				input
				gameOver = 'Y'
				break
			else :
				options[func]()

		except KeyError :
			randomResponse()

game()

if gameOver == 'Y' : 
	print("And the hero was never seen again...")
else : 
	print("So he went home...")






































