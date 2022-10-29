import sys
import os
import textwrap
import time
from random import randint


#### Class for Character Setups ####
class Character:
	# Instantiates each character with personality traits
	def __init__(self, name, health, lives, gender, inventory):
		self.name = name
		self.health = int(health)
		self.lives = int(lives)
		self.gender = gender
		self.inventory = {}
	
	# Gives pronouns for character based on gender: he, she, hers, his etc...	
	def pronouns(self):
		if 'male' in self.gender:
			nouns = {
				'mine': 'he',
				'them': 'him',
				'their': 'his',
				'asshole': 'bastard'
			}
		if 'female' in self.gender:
			nouns = {
				'mine': 'she',
				'them': 'her',
				'their': 'her',
				'asshole': 'bitch'
			}
		return nouns
		
#### Items to find within the game and add to player inventory ####		
inventoryitems = {
	'Peanuts': 5, 
	'Magic Axe': randint(50,100), 
	'Tiny Fists': randint(0,25),
	'Sword': randint(15,30),
	'Ghost Farts': randint(0,5),
	'Breadstick': 5,
	'Key': 1,
	'Bolt Cutters': randint(25,40),
	'Candle': 5,
	'Newspaper': 1,
	'Necklace': 1,
	'Nipple Warmers': 1,
	}

#### Menu Screens ####		
def help():
	print("-" * 26)
	print("Welcome to the Help Menu")
	print("-" * 26)
	print("\n")
	print(textwrap.fill(f"Tip: You can interact with most items in the room, take a moment to carefully read what is in each room and see if it provides you additional clues.", width=75))
	print("\n")
	print("\n* Type 'inventory' to see what is in your inventory")
	print("* Type 'clues' to see clues about the current room")
	print("* Type 'back' to re read the room description")
	print("* Type 'quit' to exit the game")
	return getcmd(cmdlist)

def continuegame():
	print("-" * 8)
	print("WOULD YOU LIKE TO CONTINUE?")
	print("-" * 8)
	answer = getcmd(cmdlist)

	if "y" in answer and player.lives > 1:
		print("-" * 8)
		print("\nThe game will continue")
		player.lives = player.lives - 1
		player.health = 100
		kingsguard.health = 150
		print(f"You have {player.lives} lives remaining\n")
		print("-" * 8)
		print(input("Press Enter to Continue"))
		ballroom()
	elif "n" in answer:
		ending = "You little pussy...\nGame Over!"
		for letters in ending:
			sys.stdout.write(letters)
			sys.stdout.flush()
			time.sleep(0.075)
		exit(1)
	elif player.lives == 1:
		ending = "\nWell atleast you tried...\nGame over homie!\n"
		for letters in ending:
			sys.stdout.write(letters)
			sys.stdout.flush()
			time.sleep(0.075)
		exit(1)
	else:
		print("\nI dont understand, please type yes or no\n")
		continuegame()

def continuegame2():
	print("-" * 8)
	print("WOULD YOU LIKE TO CONTINUE?")
	print("-" * 8)
	answer = getcmd(cmdlist)

	if "y" in answer and player.lives > 1:
		print("-" * 8)
		print("\nThe game will continue")
		player.lives = player.lives - 1
		player.health = 100
		kingsguard.health = 150
		print(f"You have {player.lives} lives remaining\n")
		print("-" * 8)
		print(input("Press Enter to Continue"))
		bedroom()
	elif "n" in answer:
		ending = "You little pussy...\nGame Over!"
		for letters in ending:
			sys.stdout.write(letters)
			sys.stdout.flush()
			time.sleep(0.075)
		exit(1)
	elif player.lives == 1:
		ending = "\nWell atleast you tried...\nGame over homie!\n"
		for letters in ending:
			sys.stdout.write(letters)
			sys.stdout.flush()
			time.sleep(0.075)
		exit(1)
	else:
		print("\nI dont understand, please type yes or no\n")
		continuegame2()		

def inventory():
	print('-' * 15)
	print("INVENTORY ITEMS")
	print('-' * 15)
	print("")
	print("You currently have:")
	print(f"Health: {player.health}")
	print(f"Lives: {player.lives}")
	print("")
	print("Hint: to use an item in your inventory type its name")
	print("")
	for item in player.inventory:
		print("*", "".join(item))
	return getcmd(cmdlist)	
	
#### Command List for Player Input ####
def getcmd(cmdlist):
	cmd = input("> ")
	cmd = cmd.lower()
	# Checks player input to see if this matches a current request or
	# give options for help/inventory
	if cmd in cmdlist:
		return cmd
	# Gives player option to visit help menu
	elif cmd == 'help':
		return help()
	# Gives player option to view inventory
	elif cmd == 'inventory':
		return inventory()
	elif cmd == 'quit':
		ending = "\nYou little pussy...\nGame Over!"
		for letters in ending:
			sys.stdout.write(letters)
			sys.stdout.flush()
			time.sleep(0.075)
		exit(1)
	else:
		return cmd
	
#### Rooms within the Game ####		
def startentryhall():
	os.system('cls')
	print('-' *25)
	print(textwrap.fill(f"""Welcome to the Entry Hall""", width=75))
	print('-' *25)
	print(textwrap.fill(f"""You look around and notice the door you entered through is now locked shut, theres no going back now. Thats ok because you brought a bag of peanuts with you in case you get hungry, or you know use them as a deadly weapon or something. To your left there is a staircase leading down to the Dungeon, in front of you is a Hallway leading to what looks some other rooms.""", width=75))
	print("\n")
	
	playerchoice = getcmd(cmdlist)
	while playerchoice != cmdlist:
		if 'clue' in playerchoice:
			print("")
			print("Clues:")
			print(textwrap.fill(f"Looking around the room a little more carefully you notice a letter pinned to the door which reads: \"Claire, you will never believe what I found in the Kitchen it\"... well that suspicious, this person never finished their letter, hmm odd...", width=75))
			playerchoice = getcmd(cmdlist)
		elif "peanut" in playerchoice:
			print("You eat a peanut, hmm nutritious!")
			playerchoice = getcmd(cmdlist)
		elif 'dungeon' in playerchoice or 'stair' in playerchoice:
			dungeon()
			break
		elif 'hall' in playerchoice:
			hallway()
			break
		elif 'back' in playerchoice:
			startentryhall()
		else:
			print("")
			print(textwrap.fill(f"Im unsure what {playerchoice} means, please think of something useful to ask {player.name}. Remember if you need help you can always type 'help'.", width=75))
			playerchoice = getcmd(cmdlist)

def entryhall():
	print('-' *25)
	print(textwrap.fill(f"""Welcome to the Entry Room""", width=75))
	print('-' *25)
	print(textwrap.fill(f"""You are at the entrance to the Castle, the main door is locked. To your left there is a staircase leading down to the Dungeon, in front of you is a Hallway leading to what looks some other rooms.""", width=75))
	print("\n")
	
	playerchoice = getcmd(cmdlist)
	while playerchoice != cmdlist:
		if 'clues' in playerchoice:
			print("")
			print("Clues:")
			print(textwrap.fill(f"Looking around the room a little more carefully you notice a letter pinned to the door which reads: \"Claire, you will never believe what I found in the Kitchen it\". Well that suspicious, this person never finished their letter, hmm odd...", width=75))
			print(input("\nPress Enter to Continue"))
			playerchoice = getcmd(cmdlist)
		elif 'peanut' in playerchoice:
			print("You eat a peanut, hmm nutritious!")
			playerchoice = getcmd(cmdlist)
		elif 'dungeon' in playerchoice or 'stair' in playerchoice:
			dungeon()
			break
		elif 'hall' in playerchoice:
			hallway()
			break
		elif 'back' in playerchoice:
			startentryhall()
		else:
			print("")
			print(textwrap.fill(f"Im unsure what {playerchoice} means, please think of something useful to ask {player.name}. Remember if you need help you can always type 'help'.", width=75))
			playerchoice = getcmd(cmdlist)

def tower():
	pass

def dungeon():
	print('-' *22)
	print(textwrap.fill(f"""Welcome to the Dungeon""", width=75))
	print('-' *22)
	print(textwrap.fill(f"""After climbing down the creeky stairs into the dungeon you look for a light switch, its spooky and dark in here. You can hear a noise of footsteps quickly darting across the back of the room. You throw one of your peanuts hoping to scare off whatever else is in the room with you... but all you hear is the sound of your peanut bouncing along the dusty floor. Well shit, I dont like the look of this...""", width=75))
	print(input("\nPress Enter to Continue"))
	print(textwrap.fill(f"""This room seems to be filled with old torture devices and weapons. There is a staircase which leads back to the Entry Hall, a few old buckets that looked like they were used as toilets and a cage in the back corner""", width=75))
	print("\n")
	
	playerchoice = getcmd(cmdlist)
	while playerchoice != cmdlist:
		if 'clue' in playerchoice or 'weapon' in playerchoice:
			print("")
			print("Clues:")
			print(textwrap.fill(f"Maybe one of these weapons will be of some use {player.name}, there is a few old swords, a rusty pipe, and there seems to be a freshly baked breadstick here.", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'peanuts' in playerchoice:
			print("You eat a peanut, hmm nutritious!")
			playerchoice = getcmd(cmdlist)
		elif 'entrance' in playerchoice or 'entry' in playerchoice:
			entryhall()
			break
		elif 'sword' in playerchoice or 'pipe' in playerchoice:
			print("\n")
			print(textwrap.fill(f"The {playerchoice} falls apart in your hands due to its old age and is useless to you now.", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'bread' in playerchoice:
			player.inventory['Breadstick'] = inventoryitems['Breadstick']
			print("\n")
			print(textwrap.fill(f"Mmm that is a tasty Breadstick {player.name}. Ever had a Big Kahuna Breadstick? If you like breadsticks give em a try sometime. I cant usually get them myself because my partner is gluten intollerant, which pretty much makes me gluten intollerant. But I do love the taste of a good Breadstick. Mm-mmmmm, do you know what they call a Quarter Pounder with Cheese in France? A Royal with Cheese, its because of the metric system.", width=75))
			print(input("\nPress Enter to Continue"))
			print("\n* You have added a Breadstick to your inventory *")
			playerchoice = getcmd(cmdlist)
		elif 'bucket' in playerchoice or 'toilet' in playerchoice:
			print(textwrap.fill(f"You need to take a shit {player.name}? I donk this bucket is a very sanity item to add to your inventory, keep looking...", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'cage' in playerchoice:
			print("\n")
			print(textwrap.fill(f"{player.name} comes in like a wrecking ball, left {player.pronouns()['them']} crouching in a blaze and fall!... Ok get off the cage now {player.name} this is no time for singing in your underwear!", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'back' in playerchoice:
			dungeon()
		else:
			print("")
			print(textwrap.fill(f"Im unsure what {playerchoice} means, please think of something useful to ask {player.name}. Remember if you need help you can always type 'help'.", width=75))
			playerchoice = getcmd(cmdlist)

def kingsroom():
	#player.inventory['Necklace'] = inventoryitems['Necklace']
	#player.inventory['Bolt Cutters'] = inventoryitems['Bolt Cutters']
	#player.inventory['Nipple Warmers'] = inventoryitems['Nipple Warmers']
	print('-' *29)
	print(textwrap.fill(f"""Welcome to the The Kings Room""", width=75))
	print('-' *29)
	print(textwrap.fill(f"""You made it! It looks like this is the last room You can go back into the ballroom through the doors or you may search for a way out. It appears this room is just as boring as the Maids Bedroom, some paintings on the wall, a bookcase, a large locked chest on the floor and a little bed, for a little King I suppose.""", width=75))
	print("\n")
	
	playerchoice = getcmd(cmdlist)
	while playerchoice != cmdlist:
		if 'clues' in playerchoice:
			print("")
			print("Clues:")
			print(textwrap.fill(f"The paintings on the wall appear to be of lush environments from around the nearby forest and animals. The book case has a suspiciously large frame around the sides and top. The chest on the floor looks like it has a large lock on it. The bed looks like it would fit someone the size of bowling ball, well Im exaggerating but its super tiny for kings bed!", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'ball' in playerchoice:
			ballroom()		
		elif 'paint' in playerchoice:
			print("")
			print(textwrap.fill(f"You approach the paintings, they look very pretty. Oh who cares where the hell is the exit in this place?", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'chest' in playerchoice or 'lock' in playerchoice:
			print("")
			print(textwrap.fill(f"You inspect the chest of draws, the lock appears to be damaged, there does not seem to be a way of opening this easily!", width=75))
			playerchoice = getcmd(cmdlist)
			if 'Bolt Cutters' in player.inventory and 'bolt' in playerchoice:
				print("")
				print(textwrap.fill(f"You pry open the chest and Hazar! You find the Diamond Encrusted Gold Plated Nipple Warmers!", width=75))
				player.inventory['Nipple Warmers'] = inventoryitems['Nipple Warmers']
				print(input("\nPress Enter to Continue"))
				print("\n* You have added the Nipple Warmers to your inventory *")
				playerchoice = getcmd(cmdlist)
		elif 'bed' in playerchoice:
			print("")
			print(textwrap.fill(f"You squeeze onto the bed and pretend to be the King for moment, very nice {player.name}, but you need to get out of here!", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'book' in playerchoice:
			print("")
			print(textwrap.fill(f"You inspect the book case, literature, mathematics, physics, what is this guy a genius or something? I see nothing in here thats actually interesting. Well actually theres also a bible, a dictionary, some old business paperwork", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'literature' in playerchoice:
			print("")
			print(textwrap.fill(f"You take a moment to read some literature, nice but useless for you right now!", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'math' in playerchoice:
			print("")
			print(textwrap.fill(f"These maths books like like hes been building some interesting things. There is some drawings of some machinery that looks like it rotates a hidden wall or something like that", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'physic' in playerchoice:
			print("")
			print(textwrap.fill(f"...'The young Isaac Newton is sitting in his garden when an apple falls on his head and, in a stroke of brilliant insight, he suddenly comes up with his theory of gravity'...", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'dictionary' in playerchoice:
			print("")
			print(textwrap.fill(f"...'Apple: the round fruit of a tree of the rose family, which typically has thin green or red skin and crisp flesh.'... Right well this is boring...", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'business' in playerchoice:
			print("")
			print(textwrap.fill(f"...'A business rule is a rule that defines or constrains some aspect of business and always resolves to either true or false. ... Business rules can apply to people'... Yeah, nah...", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'bible' in playerchoice:
			print("")
			print(textwrap.fill(f"This bible is empty.. after flipping a few pages there seems to be a hole in the centre, its shaped like a Cross that you would find on a necklace.. ok then?", width=75))
			playerchoice = getcmd(cmdlist)
			if 'Necklace' in player.inventory and 'necklace' in playerchoice:
				if 'Nipple Warmers' in player.inventory:
					print("")
					print(textwrap.fill(f"You pull out the Crummy Cats Necklace you had from within your pocket... and slowly place it into the hollowed out bible like Indian Jones in the Temples of Doom.", width=75))
					print("")
					print(input("\nPress Enter to Continue"))
					print("")
					print(textwrap.fill(f"The walls start to shake as the old and creeky Book Case starts to open slowly, rotating around on its axis to reveal a secret passage and a bright light... ITS OUTSIDE!", width=75))
					print("")
					print(input("\nPress Enter to Continue"))
					print("")
					congrats = f"Congratulations {player.name}! You escaped The Castle of Deaths Honor!\nYou even managed to find the Diamond Encrusted Gold Plated Nipple Warmers!\nYou saved the day!!"
					for letters in congrats:
						sys.stdout.write(letters)
						sys.stdout.flush()
						time.sleep(0.075)
					exit(1)
				else:
					print("")
					print(textwrap.fill(f"You pull out the Crummy Cats Necklace you had from within your pocket... and slowly place it into the hollowed out bible like Indian Jones in the Temples of Doom.", width=75))
					print("")
					print(input("\nPress Enter to Continue"))
					print("")
					print(textwrap.fill(f"The walls start to shake as the old and creeky Book Case starts to open slowly, rotating around on its axis to reveal a secret passage and a bright light... ITS OUTSIDE!", width=75))
					print("")
					print(input("\nPress Enter to Continue"))
					print("")
					congrats = f"Congratulations {player.name}! You escaped The Castle of Deaths Honor!\nUnforunately you did not find the Diamond Encrusted Gold Plated Nipple Warmers!\nMaybe next time!"
					for letters in congrats:
						sys.stdout.write(letters)
						sys.stdout.flush()
						time.sleep(0.075)
					exit(1)
			else:
				print("")
				print(textwrap.fill(f"It seems you do not have the necklace in your inventory {player.name}! You must go find it if you wish to place it inside this bible.", width=75))
				playerchoice = getcmd(cmdlist)
		else:
			print("")
			print(textwrap.fill(f"Im unsure what {playerchoice} means, please think of something useful to ask {player.name}. Remember if you need help you can always type 'help'.", width=75))
			playerchoice = getcmd(cmdlist)
	
def ballroom():	
	#player.inventory['Candle'] = inventoryitems['Candle']
	#player.inventory['Magic Axe'] = inventoryitems['Magic Axe']
	if 'Candle' not in player.inventory:
		print('-' *8)
		print(textwrap.fill(f"""Ballroom""", width=75))
		print('-' *8)
		print(textwrap.fill(f"""Its completely pitch black in here, you cant see a thing! You may as well come back later if you can find a flashlight or something to help you see.""", width=75))
		print("\n")
		
		playerchoice = getcmd(cmdlist)
		while playerchoice != cmdlist:
			if 'back' in playerchoice or 'hall' in playerchoice:
				hallway()
				break
			elif 'clues' in playerchoice:
				print("")
				print("Clues:")
				print(textwrap.fill(f"You will need a light to see in this room. I suggest you go back to the hallway and search elsewhere", width=75))
				playerchoice = getcmd(cmdlist)
			else:
				print("")
				print(textwrap.fill(f"Im unsure what {playerchoice} means, please think of something useful to ask {player.name}. Remember if you need help you can always type 'help'.", width=75))
				playerchoice = getcmd(cmdlist)
	else:
		print('-' *8)
		print(textwrap.fill(f"""Ballroom""", width=75))
		print('-' *8)
		print(textwrap.fill(f"""This is a very large room its a bit difficult to see in this light but at least you have a candle to help you navigate. It looks like people used to dance and party here what a bunch of animals, definitely my kind of people! There is a giant chandelier suspended from the ceiling. The way you came in leads to the hallway, and at the end of the room there seems to be 2 large doors leading to another room.""", width=75))
		print("\n")
		
		playerchoice = getcmd(cmdlist)
		while playerchoice != cmdlist:
			if 'clues' in playerchoice:
				print("")
				print("Clues:")
				print(textwrap.fill(f"The chandelier on the ceiling is very ornate and looks like it is covered in diamonds, what a spectacle! It is also suspended by ropes attached to hooks on the sides of each room. The room looks to be still in quite good condition considering what probably used to go on in here. The two large doors at the back of the room looks like it has a large shadow covering the entrance... spooky!", width=75))
				playerchoice = getcmd(cmdlist)
			elif 'hall' in playerchoice:
				hallway()
				break
			elif 'back' in playerchoice:
				ballroom()
			elif 'chand' in playerchoice:
				print("")
				print(textwrap.fill(f"Well thats a pretty Chandelier, maybe if you could get it down we could steal some of those diamonds, I always wanted a diamond tooth!", width=75))
				playerchoice = getcmd(cmdlist)
			elif 'rope' in playerchoice or 'hook' in playerchoice:
				print("")
				print(textwrap.fill(f"It looks like these are pretty heavy duty ropes. I would say if you could burn these then you could bring that chandelier down.", width=75))
				playerchoice = getcmd(cmdlist)
			elif 'burn' in playerchoice:
				print("")
				print(textwrap.fill(f"Using all your skill as a slightly psychotic pyromaniac you set fire to the ropes, HOooraH! lets burn this shit to the ground!", width=75))
				print(input("\nPress Enter to Continue"))
				print("")
				print(textwrap.fill(f"The Chandelier wobbles and then you hear the ropes snap! CRRRAAASHHHHH!! The Chandelier flies from the ceiling and smashes into the ground into 1000 pieces. Oh shit, fake diamonds, you cheap son of a bitch! You notice the diamonds fly to the corner of the room where you see something metal just behind one of the pillars", width=75))
				playerchoice = getcmd(cmdlist)
			elif 'door' in playerchoice or 'shadow' in playerchoice or 'king' in playerchoice:
				if not kingsguard.health <= 0:
					print("")
					print(textwrap.fill(f"You approach the large doors, which seems to lead into the Kings Bedroom. As you reach for the door handles the shadow appears before you!", width=75))
					print(input("\nPress Enter to Continue"))
					kingsguardbattle()
					break
				else:
					kingsroom()
					break
			elif 'hall' in playerchoice:
				print("")
				print(textwrap.fill(f"  ", width=75))
				playerchoice = getcmd(cmdlist)
			elif 'diamonds' in playerchoice:
				print("")
				print(textwrap.fill(f"Aww look at the pretty diamonds...useless to you however", width=75))
				playerchoice = getcmd(cmdlist)
			elif 'dance' in playerchoice:
				print("")
				print(textwrap.fill(f"You quickly look around, ok no one is watching, you pop out a quick irish dance and get on with it.", width=75))
				playerchoice = getcmd(cmdlist)
			elif 'metal' in playerchoice or 'pillar' in playerchoice:
				print("")
				print(textwrap.fill(f"You walk over to the pillar to find a pair of Bolt Cutters sitting against the pillar. What a strange place for bolt cutters! Its not like you are gardening and need to cut open a fence or something... or do you?", width=75))
				player.inventory['Bolt Cutters'] = inventoryitems['Bolt Cutters']
				print(input("\nPress Enter to Continue"))
				print("\n* You have added Bolt Cutters to your inventory *")
				playerchoice = getcmd(cmdlist)
			elif 'peanut' in playerchoice:
				print("\n")
				print(textwrap.fill(f"You flick a scrumptious peanut into the air and catch it with your teeth, you do a little bow as if a crowd of peasants were applauding you, thank you, thank you!", width=75))
				playerchoice = getcmd(cmdlist)
			else:
				print("")
				print(textwrap.fill(f"Im unsure what {playerchoice} means, please think of something useful to ask {player.name}. Remember if you need help you can always type 'help'.", width=75))
				playerchoice = getcmd(cmdlist)
			
def hallway():
	print('-' *7)
	print(textwrap.fill(f"""Hallway""", width=75))
	print('-' *7)
	print(textwrap.fill(f"""Between the Entrance Hall and the Kitchen at the end of the long hall way with a beautiful red floral carpet lining the cold ground beneath you. There are many old paintings on the walls as well a few large statues which seem to be guarding the entrances to the other rooms. The other rooms are a Ballroom to your left further up the Hall and a Bedroom to your right.""", width=75))
	print("\n")
	
	playerchoice = getcmd(cmdlist)
	while playerchoice != cmdlist:
		if 'clues' in playerchoice:
			print("")
			print("Clues:")
			print(textwrap.fill(f"These paintings are of what looks like family members and seem to be staring at you, a bit eery to say the least. There is one painting which seems to be a little different - it has a winding path through a forest with a beam of light in the distance. The statues look like something from the Terracotta Army, some of them have their arms crossed, another which looks like he is about to unsheathe a sword, another one menacingly holding a glowing axe. The a flickering of light coming from the kitchen down the hall as if someone was there recently. You can hear the echos of your footsteps in the large Ballroom which looks like it would have been an impressive place for parties.", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'carpet' in playerchoice:
			print("\n")
			print(textwrap.fill(f"You moon walk across the carpet like Michael Jackson and grab your crotch, 'Woo!!'", 75))
			playerchoice = getcmd(cmdlist)
		elif 'paint' in playerchoice or 'forest' in playerchoice:
			print("\n")
			print(textwrap.fill(f"You take a closer look at the painting of the forest and notice there is a small hole in the bottom of the frame about the size of a fingernail. If only you had something this small that could fit into it...", 75))
			playerchoice = getcmd(cmdlist)
			if 'peanut' in playerchoice:
				print("\n")
				print(textwrap.fill(f"Taking a peanut out of the bag you eat one, yum!! Then you take another out of the bag and place it into the small hole in the frame of the Hansel and Grettle painting... you hear a 'click' sound. The painting swings open to reveal a box...", 75))
				playerchoice = getcmd(cmdlist)
				if 'box' in playerchoice:
					print("\n")
					print(textwrap.fill(f"Opening the box reveals a Key! Well done {player.name}, this may come in use later!", 75))
					player.inventory['Key'] = inventoryitems['Key']
					print(input("\nPress Enter to Continue"))
					print("\n* You have added a Key to your inventory *")
					playerchoice = getcmd(cmdlist)
				else: 
					print("\n")
					print("Who likes surprises anyway right? You walk back into the Hallway")
					playerchoice = getcmd(cmdlist)
			else:
				print("\n")
				print(textwrap.fill(f"Even though this is the only painting with a small hole, what use could it be, right? You walk back into the Hallway", 75))
				playerchoice = getcmd(cmdlist)
		elif 'peanut' in playerchoice:
			print("\n")
			print("You eat a peanut, hmm nutritious!")
			playerchoice = getcmd(cmdlist)
		elif 'sword' in playerchoice:
			print("")
			print(textwrap.fill(f"You pull on the sword as hard as you can, however it feels like the hammer of Thor... It appears as if the sword is apart of the statue, this you will not be able to take this with you.", 75))
			playerchoice = getcmd(cmdlist)
		elif 'entrance' in playerchoice or 'entry' in playerchoice:
			entryhall()
			break
		elif 'kitchen' in playerchoice:
			kitchen()
			break
		elif 'back' in playerchoice:
			hallway()
		elif 'axe' in playerchoice:
			if 'Bolt Cutters' in player.inventory:
				print(textwrap.fill(f"Good thinking using those Bolt Cutters {player.name}! The Magic Axe is yours!", 75))
				print(input("\nPress Enter to Continue"))
				player.inventory['Magic Axe'] = inventoryitems['Magic Axe']
				print("\n* You have added the Magic Axe to your inventory *")
			else:
				print("")
				print(textwrap.fill(f"Now this looks like an impressive Axe! However it seems as if its attached to the guards hand with a chain, if you had an item that could break the chain then this could come in handy...", 75))
			playerchoice = getcmd(cmdlist)
		elif 'statue' in playerchoice:
			print(textwrap.fill(f"Impressive statue right {player.name}? It looks as if it was hand crafted by a blind Slovakian mushroom hunter.", 75))
			playerchoice = getcmd(cmdlist)
		elif 'ball' in playerchoice:
			ballroom()
			break
		elif 'bed' in playerchoice:
			if 'Key' in player.inventory:
				print("")
				print(textwrap.fill(f"Ah the key fits! Well done {player.name}. You slightly open the door and peer inside, it looks safe enough and you enter the room.", 75))
				print(input("\nPress Enter to Continue"))
				bedroom()
				break
			else:
				print("")
				print(textwrap.fill(f"The door is locked! It looks like you need a key to enter this room {player.name}.", 75))
			playerchoice = getcmd(cmdlist)
		else:
			print("")
			print(textwrap.fill(f"Im unsure what {playerchoice} means, please think of something useful to ask {player.name}. Remember if you need help you can always type 'help'.", width=75))
			playerchoice = getcmd(cmdlist)
	
def bedroom():
		print('-' *7)
		print(textwrap.fill(f"""Bedroom""", width=75))
		print('-' *7)
		print(textwrap.fill(f"""Welcome to the Maids Bedroom. The room smells like shes been smoking crack in here. I bet you could find some interesting goodies in here! Her windows are boarded up with timber, she has a chest of drawers facing her bed and some dirty laundry on the floor.""", width=75))
		
		playerchoice = getcmd(cmdlist)
		while playerchoice != cmdlist:
			if 'clues' in playerchoice:
				print("")
				print("Clues:")
				print(textwrap.fill(f"You notice on the chest of drawers a jewelery box, there is a pile of laundry on the floor. There is also some paintings around the room which could be family members. There is also a letter on the chest of drawers.", 75))
				playerchoice = getcmd(cmdlist)
			elif 'back' in playerchoice:
				bedroom()
			elif 'bed' in playerchoice:
				print("")
				print(textwrap.fill(f"You roll around on the bed like a child, good times {player.name}!", 75))
				playerchoice = getcmd(cmdlist)
			elif 'peanut' in playerchoice:
				print("")
				print(textwrap.fill(f"You throw a penut into the air to catch it with your teeth... whoosh it disappears!! Creepy!", 75))
				playerchoice = getcmd(cmdlist)
			elif 'window' in playerchoice:
				print("")
				print(textwrap.fill(f"Even if you could jump out the window {player.name} now is not the time to be contemplating suicide, we have a mission to complete!", width=75))
				playerchoice = getcmd(cmdlist)
			elif 'draw' in playerchoice or 'chest' in playerchoice:
				print("")
				print(textwrap.fill(f"You open the chest of drawers, they are empty... I suppose she just leaves her clothes on the floor, dirty bitch.", width=75))
				playerchoice = getcmd(cmdlist)
			elif 'laundry' in playerchoice:
				print("")
				print(textwrap.fill(f"You search in her laundry and find her underwear and give it a sniff. {player.name}, as much as you might want to keep those for later its unsanitary, put them back...", width=75))
				playerchoice = getcmd(cmdlist)
			elif 'letter' in playerchoice:
				print("")
				print(textwrap.fill(f"You open the letter to reveal... its her kinky lover from Castle Jack, 3 miles from here. It seems these two have had a thing going on for awhile now, super juicy info but lets keep searching for something useful!", width=75))
				playerchoice = getcmd(cmdlist)
			elif 'paint' in playerchoice:
				print("")
				print(textwrap.fill(f"You inquisitively inspect the paintings on the wall like you are some professional connoisseur, thumb and finger on your chin, head tilted sideways you reach out to the painting to straighten it and accidentally knock it onto the ground and destroy it. Bad {player.name}, Bad!", width=75))
				playerchoice = getcmd(cmdlist)
			elif 'jewel' in playerchoice:
				if not ghost.health == 0:
					print("\n")
					print(textwrap.fill(f"You reach out to the jewelery box and just as you are about to reach it, a huge Whoosh blasts you off your feet, {ghost.name} appears from the jewelery box and challenges you to a dice battle! If you beat him then you may take the contents of the jewelery box!", width=75))
					print(input("\nPress Enter to Continue"))
					print("\n")
					dicebattle(ghost)
					break
				else:
					print("\n")
					print(textwrap.fill(f"You open the box... and you find a shitty old necklace that looks like it belongs to a cat, seriously some ghost was guarding this? Whatever, probably a good idea to hold onto it anyway."))
					player.inventory['Necklace'] = inventoryitems['Necklace']
					print(input("\nPress Enter to Continue"))
					print("\n* You have added the Necklace to your inventory *")
				playerchoice = getcmd(cmdlist)
			elif 'back' in playerchoice:
				bedroom()
			elif 'hall' in playerchoice:
				hallway()
				break
			else:
				print("")
				print(textwrap.fill(f"Im unsure what {playerchoice} means, please think of something useful to ask {player.name}. Remember if you need help you can always type 'help'.", width=75))
				playerchoice = getcmd(cmdlist)
				
def kitchen():
	print('-' *7)
	print(textwrap.fill(f"""Kitchen""", width=75))
	print('-' *7)
	print(textwrap.fill(f"""At the end of the Hallway you find yourself in the Maids Kitchen. Theres cobwebs between the walls and discarded bones and rotten food left on the Kitchen Island in the centre of the room. There is dirty pots and pans left lying around on the stovetop. The door leads back into the Hallway""", width=75))
	print("\n")
	
	playerchoice = getcmd(cmdlist)
	while playerchoice != cmdlist:
		if 'clues' in playerchoice:
			print("")
			print("Clues:")
			print(textwrap.fill(f"This room is a complete mess! It reminds me of your bedroom {player.name}! At least someone left a candle in here otherwise you probably would tripped over and broke your face. There is some weird kitchen utensils in here - not the usual type. A bunch of newspapers sitting on the corner of the bench, the windows seem to be covered in grease and you cannot see outside. There is also a sealed cardboard box on the ground labelled 'DO NOT TOUCH', how very odd.", width=75))
			playerchoice = getcmd(cmdlist)
		if 'back' in playerchoice:
			kitchen()
		elif 'box' in playerchoice or 'card' in playerchoice:
			print("")
			print(textwrap.fill(f"You open the cardboard box and find a bunch of nude magazines inside, it seems like this maid was one kinky bitch! Oh wait this is addressed to the king, the guy needs to get a girlfriend seriously.", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'utensil' in playerchoice:
			print("")
			print(textwrap.fill(f"These utensils look like they belong in the garden, what were these people doing? These bones don't even look like they belong to animals... There's a chainsaw, a industrial can opener, for you know those giant cans of beans you find like - no where, and a weird looking vice.", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'chainsaw' in playerchoice:
			print("")
			print(textwrap.fill(f"Put the chainsaw down {player.name}... it has no benzin and what do you think this is, Friday the 13th?", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'industrial' in playerchoice or 'opener' in playerchoice:
			print("")
			print(textwrap.fill(f"Hmm a can opener, which seems to be broken, useless...", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'vice' in playerchoice:
			print("")
			print(textwrap.fill(f"You put a peanut in the vice and crush it... hmm satisfying!", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'news' in playerchoice:
			print("")
			print(textwrap.fill(f"You clear some dust off the table and sit down to read the newspaper, the front page reads 'Get your ass back to work {player.name}! This aint no time to be reading the damn newspaper'. Interesting article, I think this might be good to hold onto, you never know when you need a good newspaper in an abondon Castle", width=75))
			player.inventory['Newspaper'] = inventoryitems['Newspaper']
			print(input("\nPress Enter to Continue"))
			print("\n* You have added the Newspaper to your inventory *")
			playerchoice = getcmd(cmdlist)
		elif 'window' in playerchoice or 'grease' in playerchoice:
			print("")
			print(textwrap.fill(f"You draw a smiley face in window with the grease, so cute.", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'candle' in playerchoice:
			print("")
			print(textwrap.fill(f"You pick up the candle, now that was probably the smartest thing you have done today {player.name}! This will help to see in the dark", width=75))
			player.inventory['Candle'] = inventoryitems['Candle']
			print(input("\nPress Enter to Continue"))
			print("\n* You have added the Candle to your inventory *")
			playerchoice = getcmd(cmdlist)
		elif 'bones' in playerchoice:
			print("")
			print(textwrap.fill(f"Ah disgusting {player.name}, what are you going to do with some old bones, pick your teeth?", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'food' in playerchoice:
			print("")
			print(textwrap.fill(f"You really want to eat that dont you {player.name}, you digust me! Eat your penuts if you are that damn hungry.", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'peanut' in playerchoice:
			print("")
			print(textwrap.fill(f"Hmm yum, peanuts, the cornerstone of a nutritious breakfast!", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'pot' in playerchoice or 'pan' in playerchoice:
			print("")
			print(textwrap.fill(f"You whip out the spoons from the draw and start banging on the pots and pans like a drum set, you are a damn Rockstar {player.name}! Now lets keep looking...", width=75))
			playerchoice = getcmd(cmdlist)
		elif 'door' in playerchoice or 'hall' in playerchoice:
			hallway()
			break
		else:
			print("")
			print(textwrap.fill(f"Im unsure what {playerchoice} means, please think of something useful to ask {player.name}. Remember if you need help you can always type 'help'.", width=75))
			playerchoice = getcmd(cmdlist)
	
### Battle Scenes ###	
def dicebattle(enemy):
# dice battle enables the player to roll 2 times to win
	print(textwrap.fill(f"""You are to roll the dice twice, if you roll a 3 or 6 you will 
	defeat {enemy.name}""", width=75))
	
	roll = input("\nPress Enter to roll the dice:")
	dice = randint(1,6)
	guess = 0
	
	while dice != 6 and dice != 3 and guess < 1:
		print(f"You rolled {dice}, one last try!:")
		guess += 1
		roll = input("Press Enter to roll the dice:")
		dice = randint(1,6)
	if dice == 3 or dice == 6:
		print(f"You rolled {dice}")
		print("You win! You are free to take what you like from the jewelery box!")
		ghost.health = 0
		print(input("\nPress Enter to Continue"))
		bedroom()
	else:
		print(f"You rolled {dice}")
		print("You lose")
		continuegame2()
		
def battlemode(enemy, selectedweapon):
	os.system('cls')
	# Convert dictionary to list for selectedweapon: [0] weapon name, [1] weapon damage
	playerweapon = selectedweapon[0]
	playerdamage = selectedweapon[1]
	# Assign from inventoryitems dictionary the value of weapon to variable enemydamage
	# Works only if enemy has 1 item in inventory
	for k, v in enemy.inventory.items():
		enemyweapon, enemydamage = k, v
	# Fight loop based on weapon selected 	
	while enemy.health > 0:
		print(f"\n{enemy.name} swings at you with his {list(enemy.inventory)[0]}")
		player.health = player.health - enemydamage
		print(f"{player.name} has been struck with {enemy.name}'s {list(enemy.inventory)[0]} leaving: {player.health} health remaining")

		if player.health <= 0:
			print(f"\n{enemy.name} strikes you hard with his {list(enemy.inventory)[0]}!")
			print("You're head was squished like a lemon! Maybe try using a weapon next time\n")
			continuegame() # change this later
		elif enemy.health <= 0:
			print(f"Congratulations {player.name}! You have defeated {enemy.name}!")
			kingsroom()
			break
		else:
			print(f"\n{player.name} fights back with {player.pronouns()['their']} {playerweapon}!")
			enemy.health = enemy.health - playerdamage
			print(f"{enemy.name} has:",enemy.health, "health remaining")
			print(input("\nPress Enter to Continue!"))
			
	win = f"Congratulations {player.name}! You have defeated {enemy.name}!"
	for letters in win:
		sys.stdout.write(letters)
		sys.stdout.flush()
		time.sleep(0.075)
	print(input("\nPress Enter to Continue!"))
	kingsroom()
			
def kingsguardbattle():
	enemy = kingsguard
	print(textwrap.fill(f"""You encounter {enemy.name}, {enemy.pronouns()['mine']} is 8 feet tall and {enemy.pronouns()['mine']} is holding {enemy.pronouns()['their']} {list(enemy.inventory)[0]}!\n\nYou must prepare to fight {enemy.pronouns()['them']}. Your health is {player.health}, but {enemy.name} has {enemy.health} health as {enemy.pronouns()['mine']} has heavy armour. Hopefully you have a weapon in your inventory otherwise you can take a chance to fight {enemy.pronouns()['them']} with your fists. Be aware once you begin the fight you cannot run away, so choose carefully!""", width=75, replace_whitespace=False))
	print("\n")
	print(textwrap.fill(f"\nDo you wish to fight or run? If you have a weapon in your inventory type in the name of the item instead.", 75))
	
	cmdlist = ['fight', 'run']
	playerchoice = getcmd(cmdlist)
	
	if 'fight' in playerchoice or 'fist' in playerchoice:
		key, value = 'Tiny Fists', inventoryitems['Tiny Fists']
		selectedweapon = key, value
		print("\n")
		print(textwrap.fill(f"You are a brave soul {player.name}! Personally I would have picked a weapon, but you know, knock yourself out :D", width=75, replace_whitespace=False))
		print(input("\nPress Enter to Continue"))
		battlemode(kingsguard, selectedweapon)
	elif 'Magic Axe' in player.inventory and 'axe' in playerchoice:
		key, value = 'Magic Axe', inventoryitems['Magic Axe']
		selectedweapon = key, value
		print("\n")
		print(textwrap.fill(f"Ah the Magic Axe! Wise Choice {player.name}! May the luck of the gods be on your side", width=75, replace_whitespace=False))
		print(input("\nPress Enter to Continue"))
		battlemode(kingsguard, selectedweapon)
	elif 'Peanuts' in player.inventory and 'peanut' in playerchoice:
		key, value = 'Peanuts', inventoryitems['Peanuts']
		selectedweapon = key, value
		print("\n")
		print(textwrap.fill(f"Peanuts... really? Great choice you nut-job...", width=75, replace_whitespace=False))
		print(input("\nPress Enter to Continue"))
		battlemode(kingsguard, selectedweapon)
	elif 'Breadstick' in player.inventory and 'bread' in playerchoice:
		key, value = 'Breadstick', inventoryitems['Breadstick']
		selectedweapon = key, value
		print("\n")
		print(textwrap.fill(f"A Breadstick... really? Your going to bash him to death with a hardened flour stick nice one {player.name}...", width=75, replace_whitespace=False))
		print(input("\nPress Enter to Continue"))
		battlemode(kingsguard, selectedweapon)
	elif 'Key' in player.inventory and 'key' in playerchoice:
		key, value = 'Key', inventoryitems['Key']
		selectedweapon = key, value
		print("\n")
		print(textwrap.fill(f"I see, you are oldschool {player.name}. Bustin out the keys between the finger tips I see, go all ninja on his ass...", width=75, replace_whitespace=False))
		print(input("\nPress Enter to Continue"))
		battlemode(kingsguard, selectedweapon)
	elif 'Bolt Cutters' in player.inventory and 'bolt' in playerchoice:
		key, value = 'Bolt Cutters', inventoryitems['Bolt Cutters']
		selectedweapon = key, value
		print("\n")
		print(textwrap.fill(f"Formidable option, probably not the best thing to use but you could give it a try!", width=75, replace_whitespace=False))
		print(input("\nPress Enter to Continue"))
		battlemode(kingsguard, selectedweapon)
	elif 'Candle' in player.inventory and 'candle' in playerchoice:
		key, value = 'Candle', inventoryitems['Candle']
		selectedweapon = key, value
		print("\n")
		print(textwrap.fill(f"Yeah right, good luck with your Candle hot shot!", width=75, replace_whitespace=False))
		print(input("\nPress Enter to Continue"))
		battlemode(kingsguard, selectedweapon)
	elif 'Newspaper' in player.inventory and 'news' in playerchoice:
		key, value = 'Newspaper', inventoryitems['Newspaper']
		selectedweapon = key, value
		print("\n")
		print(textwrap.fill(f"Yes mum, get him with your rolled up newspaper! What is this Red Neck town?", width=75, replace_whitespace=False))
		print(input("\nPress Enter to Continue"))
		battlemode(kingsguard, selectedweapon)
	elif 'Necklace' in player.inventory and 'necklace' in playerchoice:
		key, value = 'Necklace', inventoryitems['Necklace']
		selectedweapon = key, value
		print("\n")
		print(textwrap.fill(f"Swing it baby! I think you have better chance just hanging yourself now with that necklace... but oh well luck!", width=75, replace_whitespace=False))
		print(input("\nPress Enter to Continue"))
		battlemode(kingsguard, selectedweapon)
	elif 'run' in playerchoice:
		ballroom()
	else:
		print(f"\n{playerchoice} is not an option... try something else!")
		print(input("\nPress Enter to Continue"))
		kingsguardbattle()

#### Game Start  ####
def introduction():
	os.system('cls')
	print(textwrap.fill(f"""Welcome {player.name}. You have arrived at King Sexy Pants Castle of Deaths Honour, a mouthful I know - he is an extravagant King who is well known in the land for his assorted range of sexy pants. As well as being known for his attire it has been rumoured his Castle is filled with death traps, so beware! I trust you brought a spare pare of underwear.
	""", width=75))
	print('\n')
	print(input("Press Enter to Continue"))
	print(textwrap.fill(f"""Your mission, if you choose to accept it is to find and steal King Sexy Pants' most precious and elusive possession - The Diamond Encrusted Gold Plated Nipple Warmers, these fetch for atleast $30 each on ebay... And make it out alive ofcourse!
	""", width=75))
	print('\n')
	print(input("Press Enter to Continue"))
	print(textwrap.fill(f"""You start the game with 3 lives and 100 health so be careful as you go through the game otherwise if you run out of lives you will have to restart the game from the beginning, losing any items you have collected along the way.
	""", width=75))
	print('\n')
	print(input("Press Enter to Continue"))
	print(textwrap.fill(f"""If you need help just type the words 'help'. You can type the words 'clues' to look around the room for clues. You can also view your inventory by typing the word 'inventory' - which will show you all the items you have collected so far. If you see an item in the room you think may be of use later you can attempt to collect it or use it by typing its name. Okay, enough jibber jabber, lets get exploring! 
	""", width=75))
	print('\n')
	print(input("Press Enter to Continue"))
	journeyintro = f"Good luck on your journey {player.name}!....."
	for letters in journeyintro:
			sys.stdout.write(letters)
			sys.stdout.flush()
			time.sleep(0.1)
	startentryhall()
	
if __name__ == "__main__":
	cmdlist = []
	os.system('cls')
	# Welcome Screen: Input player name & gender

	print("Welcome to the Castle of Deaths Honour, what may be your name?")
	player_name = input("> ")
	print(f"Hi {player_name}, and what is that thing between your legs, are you a male or a female?")
	player_gender = getcmd(cmdlist)
	while player_gender != 'male' and player_gender != 'female':
		print(f"\You are not a {player_gender} {player_name}, please type either male or female")
		player_gender = getcmd(cmdlist)
		
	# Test Character
	#player_name = 'Mr Doug' ###
	#player_gender = 'male'	###	 
	# Character Setups
	player = Character(player_name, 100, 3, player_gender, None)
	player.inventory['Tiny Fists'] = inventoryitems['Tiny Fists']
	player.inventory['Peanuts'] = inventoryitems['Peanuts']
	kingsguard = Character("The Kings Guard", 150, 1, 'male', None)
	kingsguard.inventory['Sword'] = inventoryitems['Sword']
	ghost = Character("The Ghost of King Sexy Pants", 100, 1, 'male', None)
	ghost.inventory['Ghost Farts'] = inventoryitems['Ghost Farts']

	# Uncomment after test
	introduction()
	
	#kingsroom()
	#entryhall()
	#print(kingsguard.inventory)
	#entryhall()
	#help()
	#dicebattle(ghost)
	#battlemode(kingsguard)
	#kingsguardbattle()
