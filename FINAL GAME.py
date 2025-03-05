#goals for tomorrow:
#add random encounters

import random
import time

hints=(
	"Hint: Leather can be found at the farm!",
	"Hint: Scrap can be found at the scrapyard!",
	"Hint: Certain quest items can be found by exploring the area!",
	"Hint: Tom Nook sells 2 random items! I wonder what they are for?",
	"Hint: Wow bro you need hints?"
)

sidequest_status={"yakuza":"incomplete",
	"kratos":"incomplete"
}

quest_status={"weaponsmith":"incomplete",
	"armorsmith":"incomplete",
	"crush":"incomplete",
	"gandalf":"1st"
}

Player_Stats = {"HP": 80, "Armor": 10, "DMG": 15, "Energy": 40,"enemies killed":0}
bells=0

Consumable_info = {
	"apple": {"type": "HP", "restoration": "15","sell price":10},
	"energy drink": {"type": "Energy", "restoration": "5","sell price":10},
	"edible oil": {"type": "Energy", "restoration": "10","sell price":20},
	"full heal": {"type": "HP", "restoration": Player_Stats["HP"],"sell price":35},
	"beef": {"type": "HP", "restoration": 30,"sell price":40}
}
Loot_Bag={"scrap":0, "leather":0, "chocolates":0,"map":0,"artifact":0,"heineken":0,"baby formula":0}
Bag = {
	"apple": {"type": Consumable_info["apple"]["type"], "amount": 1, "effect": Consumable_info["apple"]["restoration"]},
}

E_str = {
	"shadow": 15,
	"hobo": 10,
	"karen": 15,
	"animatronic": 20,
	"freddy fazbear": 25,
	"farmer": 10,
	"cow": 5,
	"cow king": 15,
	"spider horde":10,
	"cave goblin":15,
	"muffet":25,
	"fish":[5,15,30]
}

E_HP = {
	"shadow": 45,
	"hobo": 50,
	"karen": 70,
	"animatronic": 60,
	"freddy fazbear": 80,
	"farmer": 50,
	"cow": 30,
	"cow king": 90,
	"spider horde":25,
	"cave goblin":50,
	"muffet":100,
	"fish":250
}

E_heal = {
	"shadow": 10,
	"hobo": 10,
	"karen": 15,
	"animatronic": 5,
	"freddy fazbear": 5,
	"farmer": 15,
	"cow": 10,
	"cow king": 15,
	"spider horde":5,
	"cave goblin":10,
	"muffet":15,
	"fish":20
}

Loot = {
	"hobo": {"common": ["apple", "energy drink"]},
	"karen": {"common": ["apple", "energy drink"], "rare": ["full heal"]},
	"animatronic": {"common": ["scrap", "edible oil"]},
	"freddy fazbear": {"common": ["scrap", "edible oil"]},
	"farmer": {"common": ["apple"], "uncommon": ["leather"]},
	"cow": {"common": ["leather"], "uncommon": ["beef"]},
	"cow king": {"common": ["leather"], "uncommon": ["beef"]},
	"spider horde":{"rare":["artifact"]},
	"cave goblin":{"rare":["artifact"]},
	"muffet":{"common":["artifact"]}
}

enemies = {
	"supermarket":["hobo","karen",],
	"scrapyard":["hobo","animatronic","freddy fazbear"],
	"farm":["farmer","cow","cow king"],
	"cave":["spider horde","cave goblin","muffet"],
	"rift zone":["fish"]
}
Block_chance = {10: 25, 15: 20, 20: 10}

max_Space=10
Encounter = False
enemy = "shadow"
option = "null"
item_sel = "null"
Name="null"
location="base"
option="null"
tutorial=True

def lose_cutscene():
	print("you died...")
	time.sleep(1)
	print("...but you hear a noise")
	time.sleep(1)
	print("beep... beep.... beep...")
	time.sleep(1)
	print(f"{Name}: Oh no! Im gonna be late for school!")
	time.sleep(1)
	print(f"{Name}: I shouldve never stayed up last night!")
	time.sleep(1)
	print("GAME OVER")
	exit(0)


def final_cutscene():
	print("the fish collapses")
	time.sleep(1)
	print("a bright light goes off")
	time.sleep(1)
	print("beep... beep.... beep...")
	time.sleep(1)
	print("you wake up, without your headache this time...")
	time.sleep(1)
	print(f"{Name}: Was it all a dream?")
	time.sleep(1)
	print("you finally get ready for school and to face the day")
	time.sleep(1)
	print(f"{Name}: Alright, lets do this")
	time.sleep(1)
	print("the end")
	exit(0)

def boss_cutscene():
	global location
	print("you explore the rift zone...")
	time.sleep(1)
	print("but something is... off")
	time.sleep(1)
	print("the world distorts and your friends disappears")
	time.sleep(1)
	print("the faint sound of a bell thrashes your mind")
	time.sleep(1)
	print("then it hits you.")
	time.sleep(1)
	print("this isnt real. it never was.")
	time.sleep(1)
	print("you have to wake up.")
	time.sleep(1)
	print("you rush to patch the rift to wake yourself up when suddenly...")
	time.sleep(1)
	print("you are washed away by a tide!")
	time.sleep(1)
	location="rift zone"
	fighting()

def opening_cutscene():
	print(f"\n{Name}: My head is ringing right now")
	time.sleep(1)
	print(f"{Name}: I shouldnt have stayed up that late...")
	time.sleep(1)
	print(f"{Name}: I have to get ready for school now.")
	time.sleep(1)
	print(f"{Name}: Mom are you there?")
	time.sleep(1)
	print("you are greeted with silence")
	time.sleep(1)
	print(f"{Name}: Oh well, no time to waste")
	global option
	def house_options():
			print("\nI should get ready for school, what should I do?")
			print("---------------------------------")
			print("[A] eat breakfast")
			print("[B] take a shower")
			print("[C] wear something proper")
			print("[D] leave for school")
			return input("-->  ")
	while True:
			option=house_options()
			if option.upper() == "A":
				if Player_Stats["HP"] <100:
					print("you ate breakfast")
					Player_Stats["HP"]+=20
				else:
					print("you already ate breakfast")
			if option.upper() == "B":
				if Player_Stats["Energy"] <50:
					print("you take a shower")
					Player_Stats["Energy"]+=10
				else:
					print("you already took a shower")
			if option.upper() == "C":
				if Player_Stats["Armor"] <15:
					print("you wear proper uniform")
					Player_Stats["Armor"]+=5
				else:
					print("you already wore your uniform")
			if option.upper()=="D" :
				time.sleep(.2)
				print("you leave for school")
				break
	time.sleep(1)
	print("you go outside your house to go to school")
	time.sleep(1)
	print("a figure approaches...")
	fighting()
	time.sleep(1)
	print(f"{Name}: Whoah a sword!")
	time.sleep(2)
	print("you store the sword in your rather spacious bag")
	time.sleep(2)
	print(f"{Name}: I dont remember my bag being this big?")
	time.sleep(2)
	print("youre cut off by a rustling in the bushes...")
	time.sleep(2)
	choice=input("approach the bush? (y/n) \n")
	while choice.upper() not in ["Y","N"]:
		print("not an option, please try again")
		choice=input("approach the bush? (y/n) \n")
	if choice.upper()=="Y":
		time.sleep(1)
		print("you carefully walk up to the bush...")
		time.sleep(1)
		print("something jumps at you!")
		time.sleep(2)
		print("???: Mayor! Im so glad youre here! Where did all the people go?!")
		time.sleep(1)
		print("you freeze before uttering the words...")
		time.sleep(1.5)
		print(f"{Name}: Tom Nook?!?!")
		time.sleep(2)
		print("Tom Nook: Who else would it be? Now tell me where everyone went before I increase your debt!")
		time.sleep(2)
		print(f"{Name}: But how? Youre not even real!")
		time.sleep(2)
		print("Tom Nook: What do you mean 'not real'? Thats impossible!")
		time.sleep(1.5)
		print("How can I be fake if theres others like me?")
		time.sleep(2)
		print(f"{Name}: Theres more of you?")
		time.sleep(2)
		print("Tom Nook: Follow me! Ill show you where they are!")
	elif choice.upper()=="N":
		print("you ignore the sounds")
		time.sleep(2)
		print("you hear tiny steps!")
		time.sleep(1.5)
		print("you try to turn, but!")
		time.sleep(2)
		print("a bag is placed over your head")
		time.sleep(2)
		print(f"{Name}: Who are you!?!")
		time.sleep(2)
		print("???: Dont worry mayor! Im only here to help!")
		time.sleep(2)
		print(f"{Name}: Mayor?! Are you Tom Nook?!?")
		time.sleep(2)
		print("Tom Nook: The one and only!")
		time.sleep(2)
		print("you lift the bag off your head")
		time.sleep(2)
		print(f"{Name}: Why did you try to kidnap me?")
		time.sleep(2)
		print("Tom Nook: The others wanted me to bring you back because they need your help")
		time.sleep(2)
		print(f"{Name}: Theres others?")
		time.sleep(2)
		print("Tom Nook: Follow me and I will show you!")
	time.sleep(2)
	print("you arrive at the base")
	time.sleep(2)
	print("Tom Nook: You can talk to the people here, they can help boost you and possibly help you fix this mess!")
	return
		
def title_screen():
	global option,Name
	def credits():
		print("\nLead Developer \nAndre Quimpo")
		print("\nCo-Developers \nJacob Garganza \nAenon Magabat")
		print("\nPlaytesters \nAlonzo Pahilanga\n")
	def title_options():
		if tutorial:
			print("WELCOME TO FEVER DREAM")
			print("[A] start game")
			print("[B] credits")
			print("[X] exit")
		else:
			print("WELCOME TO FEVER DREAM")
			print("[A] continue game")
			print("[B] credits")
			print("[X] exit")
		return input("-->  ")
	while True:
		option=title_options()
		if option.upper() =="A":
			if tutorial:
				Name=input("what is your name?\n")
				print(f"Oh! {Name} is such a nice name!")
				time.sleep(1)
				opening_cutscene()
				return
			else:
				menu()
		elif option.upper() =="B":
			credits()
		elif option.upper()=="X":
			print("ending game...")
			exit(0)
		else:
			print("invalid input")
	
def menu():
	while True:
		print("\nPAUSED")
		print("[A] Resume Game")
		print("[B] Check Stats")
		print("[C] Check Bag")
		print("[D] Check Loot")
		print("[E] Random Hint")
		print("[X] Exit to Title Screen")
		menu_option = input("-->  ")

		if menu_option.upper() == "A":
			gameplay()  # Resumes game
		elif menu_option.upper() == "B":
			for key, value in Player_Stats.items():
				print(f"{key}: {value}")
		elif menu_option.upper() == "C":
			open_bag()
		elif menu_option.upper() =="D":
			for item,amount in Loot_Bag.items():
				print(f"{item}: {amount}")
		elif menu_option.upper() =="E":
			print(random.choice(hints))
		elif menu_option.upper() == "X":
			title_screen()  # Returns to title screen
		else:
			print("Invalid input, try again.")

def rand_encounters(location):
	global bells
	print("")
	encounter_type = random.choice(["positive", "negative"])

	if encounter_type == "negative":
		if location == "supermarket":
			print("You see a little boy crying in the aisle.")
			print("Mister, have you seen my mommy?")
			print("[A] Help him find his mother")
			print("[B] Ignore him and move on")
			choice = input("--> ").upper()
			if choice == "A":
				print("As you help Timmy, a wild Karen appears!")
				print("Karen: Why are you talking to my child?!")
				print("Karen: For that I will take 25 bells!")
				if bells <25:
					print("Karen: Wowww, you dont even have 25 bells.")
					print(f"-{bells} bells")
					bells=0
				else:
					print("Karen: Thank youuuu")
					bells-=25
			elif choice == "B":
				print("You pretend not to hear him and continue shopping.")

		elif location == "scrapyard":
			print("A figure is running towards you")
			print("[A] Ask where he's going")
			print("[B] Ignore him and move on")
			choice = input("--> ").upper()
			if choice == "A":
				print("He crashes into you and takes something from your bag!")
				if Bag:
					random_item = random.choice(list(Bag.keys()))
					print(f"You lost {random_item}!")
					Bag[random_item]["amount"] -= 1
					if Bag[random_item]["amount"] == 0:
						del Bag[random_item]
				else:
					print("Luckily, your bag was empty!")
			elif choice == "B":
				print("You step aside and avoid him.")

		elif location == "farm":
			print("A sickly man coughs as he approaches you.")
			print("Sick Man: Do you have any medicine...?")
			print("[A] Try to help him")
			print("[B] Walk away quickly")
			choice = input("--> ").upper()
			if choice == "A":
				print("You get too close... He coughs in your face!")
				Player_Stats["HP"] -= 5
				print("You feel a little weaker. \n-5 HP")
			elif choice == "B":
				print("You avoid him and move on.")

	else:  # Positive encounter
		if location == "supermarket":
			print("You spot a gangster carrying a baby.")
			if sidequest_status["yakuza"]=="complete":
				print("you wave at each other")
				return
			print("[A] Offer him a baby formula")
			print("[B] Ignore him and continue shopping")
			choice = input("--> ").upper()
			if choice == "A":
				if "baby formula" in Loot_Bag and Loot_Bag["baby formula"] > 0:
					Loot_Bag["baby formula"] -= 1
					print("The gangster smirks and hands you 50 bells.")
					bells += 50
					sidequest_status["yakuza"]="complete"
				else:
					print("You don't have a baby formula!")
			elif choice == "B":
				print("You walk past him without a second thought.")

		elif location == "scrapyard":
			print("You see a knight from the Crusades inspecting a pile of scrap.")
			print("[A] Give him 5 scrap")
			print("[B] Leave him be")
			choice = input("--> ").upper()
			if choice == "A":
				if "scrap" in Loot_Bag and Loot_Bag["scrap"] >= 5:
					Loot_Bag["scrap"] -= 5
					print("Crusader: Thank you, kind traveler. Here, have my Holy Water")
					print("+1 full heal")
					print(f"{Name}: This is a full heal..?")
					print("The crusader runs off")
					if "full heal" in Bag:
						Bag["full heal"]["amount"] += 1
					else:
						Bag["full heal"] = {"type": "HP","amount": 1,"effect": Player_Stats["HP"]}
				else:
					print("You don't have enough scrap!")
			elif choice == "B":
				print("You let him be and continue exploring.")

		elif location == "farm":
			print("A pale warrior is sharpening his blades near the crops.")
			if sidequest_status["kratos"]=="complete":
				print("you wave at each other")
				return
			print("[A] Offer him a Heineken")
			print("[B] Leave him alone")
			choice = input("--> ").upper()
			if choice == "A":
				if "heineken" in Loot_Bag and Loot_Bag["heineken"] > 0:
					Loot_Bag["heineken"] -= 1
					if Loot_Bag["heineken"] == 0:
						del Loot_Bag["heineken"]
					print("He grunts in approval and strengthens your weapon. \n+5 DMG")
					Player_Stats["DMG"] += 5
					sidequest_status["kratos"]="complete"
				else:
					print("You don't have a Heineken!")
			elif choice == "B":
				print("You keep your distance and continue exploring.")

def shop():
	def buy():
		global bells,max_Space
		while True:
			print(f"\nbells: {bells}")
			print("--------SHOP--------")
			print("[A] apple - 15 bells")
			print("[B] energy drink - 15 bells")
			print("[C] baby formula - 25 bells")
			print("[D] full heal - 50 bells")
			print("[E] heineken - 100 bells (ON SALE!!)")
			print("[X] exit")
			choice = input("-->  ").upper()

			if choice == "X":
				return  # Exit buy menu

			items = {
				"A": ("apple", 15),
				"B": ("energy drink", 15),
				"C":("baby formula",25),
				"D": ("full heal", 50),
				"E": ("heineken", 100)
			}
			if bag_check()>=max_Space:
				print("you have no more space in your bag")
				return
			else:
				if choice in items:
					item, cost = items[choice]
					if bells >= cost:
						print(f"bought {item}")
						bells -= cost
						if item in Consumable_info:
							if item in Bag:
								Bag[item]["amount"] += 1
							else:
								Bag[item] = {
									"type": Consumable_info[item]["type"],
									"amount": 1,
									"effect": Consumable_info[item]["restoration"]
								}
						else:
							if item == "heineken":
								if item in Loot_Bag:
									Loot_Bag[item] += 1
								else:
									Loot_Bag[item] = 1
	
						print(f"You received a {item}!")
					else:
						print("Not enough bells!")
				else:
					print("Invalid input, try again.")
	def sell():
		global bells
		while True:
			print(f"\nbells: {bells}")
			print("--------SHOP--------")
			for item in Bag:
				print(f"{item} ({Bag[item]['amount']}): {Consumable_info[item]['sell price']} bells")
			print("[X] exit")
			sell_choice=input("--> ")
			if sell_choice.upper()=="X":
				break
			else:
				if sell_choice in Bag:
					print(f"sold {sell_choice}")
					bells+=Consumable_info[sell_choice]["sell price"]
					Bag[sell_choice]["amount"]-=1
					if Bag[sell_choice]["amount"] == 0:
						del Bag[sell_choice]
				else:
					print("you dont have that item")
	while True:
		print("\nTom Nook: Welcome to my shop!")
		print("[A] buy items")
		print("[B] sell items")
		print("[X] leave shop")
		dialogue_choice=input("-->  ")
		if dialogue_choice.upper()=="A":
			buy()
		elif dialogue_choice.upper()=="B":
			sell()
		elif dialogue_choice.upper()=="X":
			print("you walk away")
			break
		else:
			print("invalid input, try again")

def bag_check():
	return sum(item["amount"] for item in Bag.values())

def open_bag():
	print("HP items")
	for item, data in Bag.items():
		if data["type"] == "HP":
			print(f"{item}(s): {data['amount']}")
			print(f"Heals {data['effect']} {data['type']}")
	print("")
	print("Energy items")
	for item, data in Bag.items():
		if data["type"] == "Energy":
			print(f"{item}(s): {data['amount']}")
			print(f"Restores {data['effect']} {data['type']}")

def fighting():
	global option,item_sel,enemy, tutorial
	
	if tutorial:
		enemy="shadow"
	else:
		enemy = random.choice(enemies[location])

	HP = Player_Stats["HP"]
	max_HP = Player_Stats["HP"]
	DMG = Player_Stats["DMG"]
	Engy = Player_Stats["Energy"]
	Blk_chance = Block_chance[Player_Stats["Armor"]]
	max_Engy = Player_Stats["Energy"]

	# Enemy stats
	F_HP = E_HP[enemy]
	max_EHP = E_HP[enemy]
	E_dmg = E_str[enemy]
	
	def tutorial_fight():
		global option, item_sel, enemy, tutorial
		nonlocal HP, Engy, max_HP, max_Engy, F_HP, max_EHP, DMG, E_dmg

		print(f"A shadowy figure appears... ")

		# **Basic Attack Tutorial**
		print("Hint: Try attacking! (Press 'A')")
		while True:
			option=fight_options()
			if option.upper() == "A":
				print(f"You strike the {enemy}!")
				Engy -= 4  # Energy deduction
				F_HP -= DMG
				break
			else:
				print("Hint: You should attack.")

		# **Enemy Counterattack**
		print(f"The {enemy} strikes!")
		HP -= E_dmg
		print("Hint: After every round, you restore 2 energy.")
		Engy = min(Engy + 2, max_Engy)

		# **Dodge Tutorial**
		print("Hint: The enemy is attacking, try dodging! (Press 'C')")
		while True:
			option = fight_options()
			if option.upper() == "C":
				print(f"The {enemy} attacks...")
				print("But you dodged it!")
				Engy += 2  # Reward energy for dodging
				break
			else:
				print("Hint: You should dodge.")

		# **Healing Tutorial**
		print("Hint: You're injured, try healing using an item (Press 'B')")
		while True:
			option = fight_options()
			if option.upper() == "B":
				print("You open your bag:")
				open_bag()
				while True:
					item_sel = input("Use -->  ")
					if item_sel in Bag and Bag[item_sel]["amount"] > 0:
						if Bag[item_sel]["type"] == "HP":
							HP += int(Bag[item_sel]["effect"])  # Ensure healing is an integer
							HP = min(HP, max_HP)  # Prevent overhealing
							print(f"Used {item_sel}.")
							Bag[item_sel]["amount"] -= 1
							if Bag[item_sel]["amount"] == 0:
								del Bag[item_sel]  # Remove item if used up
							break
						else:
							print("Hint: That item isn't for healing.")
					else:
						print("Hint: Type the exact item name.")
				break
			else:
				print("Hint: You should heal.")

		# **Finishing the Fight**
		print("Hint: Finish off the enemy!")
		Engy = min(Engy + 2, max_Engy)

		while F_HP > 0:
			option = fight_options()

			if option.upper() == "A":
				Engy-4
				print(f"You strike the {enemy}!")
				Engy=min(Engy+2,max_Engy)
				F_HP -= DMG
				if F_HP <= 0:
					break
				if random.randint(1,2)==1:
					print(f"The {enemy} heals itself!")
					F_HP = min(F_HP + E_heal[enemy], max_EHP)
				else: 
					print(f"the {enemy} does nothing")
			elif option.upper() == "B":
				print("Hint: There are no more tutorial items, try another option.")

			elif option.upper() == "C":
				print(f"You hesitate...")
				Engy=min(Engy+2,max_Engy)
				if random.randint(1,2)==1:
					print(f"The {enemy} heals itself!")
					F_HP = min(F_HP + E_heal[enemy], max_EHP)
				else: 
					print("you both do nothing")

			elif option.upper() == "D":
				print("Hint: You cannot run in the tutorial.")

		print(f"\nYou defeated the {enemy}!")
		print(f"The {enemy} dropped a sword!")
		print("Obtained sword! \n+5 DMG!")
		Player_Stats["DMG"] += 5
		tutorial = False
		return
	
	def drop_loot(enemy):
		if enemy=="fish":
			final_cutscene()
		def cash_drop():
			global bells
			if random.randint(1,2)==1:
				M_drop=random.randint(1,25)
				print(f"the {enemy} also dropped {M_drop} bells!")
				bells+=M_drop
				print(bells)
		
		global max_Space
		loot_roll = random.randint(1, 100)
		if loot_roll <= 15:
			rarity = "rare"
		elif 16 <= loot_roll <= 40:
			rarity = "uncommon"
		elif 41 <= loot_roll <= 80:
			rarity = "common"
		else:
			rarity = "no drop"
	
		if rarity in Loot[enemy]:
			item = random.choice(Loot[enemy][rarity])
			if item in Consumable_info:
				if bag_check()>=max_Space:
					print("you leave the item because you have no space")
					cash_drop()
					return
				if item in Bag:
					Bag[item]["amount"] += 1
				else:
					Bag[item] = {
						"type": Consumable_info[item]["type"],
						"amount": 1,
						"effect": Consumable_info[item]["restoration"]
					}
				print(f"You received a {item}!")
			else:
				print(f"You received a {item}!")
				Loot_Bag[item] += 1
			print(Loot_Bag)
			cash_drop()
			
	def fight_options():
		nonlocal HP, Engy, F_HP
		global option
		option = "null"
		print("\nYour HP:", HP)
		print("Your Energy:", Engy)
		print("Enemy HP:", F_HP)
		print("----------------------------")
		print("[A] Strike: 4 energy")
		print("[B] Use item")
		print("[C] Dodge")
		print("[D] Run")
		return input("--> ")
		
	def boss_ai():
		global option
		nonlocal Blk_chance, F_HP, HP, Engy, max_Engy, DMG, max_HP, max_EHP
		B_atk1=E_str[enemy][0]
		B_atk2 =E_str[enemy][1]
		B_atk3 =E_str[enemy][2]
		enemy_act = random.randint(1, 5)
		if enemy_act == 1:
			print(f"The {enemy} slaps you!")
			if option.upper() == "C":
				print("But you dodged it!")
				option = "null"
				return            
			block = random.randint(1, Blk_chance)
			if block == 1:
				print("But you blocked it!")
				Engy = min(Engy + 2, max_Engy)
			else:
				print("You were hit!")
				HP -= B_atk1
				Engy = min(Engy + 2, max_Engy)     
			option = "null"
		elif enemy_act == 2:
			print(f"The {enemy} spawns a tsunami!")
			if option.upper() == "C":
				print("But you dodged it!")
				option = "null"
				return            
			block = random.randint(1, Blk_chance)
			if block == 1:
				print("But you blocked it!")
				Engy = min(Engy + 2, max_Engy)
			else:
				print("You were hit!")
				HP -= B_atk2
				Engy = min(Engy + 2, max_Engy)     
			option = "null"
		elif enemy_act == 3:
			print(f"The {enemy} bites you!")
			if option.upper() == "C":
				print("But you dodged it!")
				option = "null"
				return            
			block = random.randint(1, Blk_chance)
			if block == 1:
				print("But you blocked it!")
				Engy = min(Engy + 2, max_Engy)
			else:
				print("You were hit!")
				HP -= B_atk3
				Engy = min(Engy + 2, max_Engy)     
			option = "null"
		elif enemy_act == 2:
			if F_HP < max_EHP:
				print(f"The {enemy} heals!")
				F_HP = min(F_HP + E_heal[enemy], max_EHP)
		else:
			print(f"The {enemy}  flops around.")  
			Engy = min(Engy + 2, max_Engy)
			option = "null"
	def enemy_ai():
		global option
		nonlocal Blk_chance, F_HP, HP, Engy, max_Engy, DMG, max_HP, max_EHP, E_dmg
		if enemy=="fish":
			boss_ai()
			return
		enemy_act = random.randint(1, 3)
		if enemy_act == 1:
			print(f"The {enemy} attacks!")
			if option.upper() == "C":
				print("But you dodged it!")
				option = "null"
				return            
			block = random.randint(1, Blk_chance)
			if block == 1:
				print("But you blocked it!")
				Engy = min(Engy + 2, max_Engy)
			else:
				print("You were hit!")
				HP -= E_dmg
				Engy = min(Engy + 2, max_Engy)     
			option = "null"
		elif enemy_act == 2:
			if F_HP < max_EHP:
				print(f"The {enemy} heals!")
				F_HP = min(F_HP + E_heal[enemy], max_EHP)
			else:
				print(f"The {enemy} stands still.")  
			Engy = min(Engy + 2, max_Engy)
			option = "null"
		elif enemy_act == 3 and option.upper() == "A":
			enemy_block = random.randint(1, 25)
			if enemy_block == 1:
				print(f"The {enemy} blocked your attack!")
				F_HP += DMG
			else:
				print(f"The {enemy} tried dodging your attack and failed.")
			Engy = min(Engy + 2, max_Engy)
			option = "null"
		else:
			print(f"The {enemy} does nothing.")

	print(f"The {enemy} startles you!")
	if tutorial:
		tutorial_fight()
		return
	while True:
		if HP<1:
			lose_cutscene()
		option = fight_options()

		if option.upper() == "A":
			if Engy < 4:
				print("You don't have enough energy!")
				fight_options()
			else:
				print(f"You strike the {enemy}!")
				Engy -= 4
				F_HP -= DMG
				if F_HP <= 0:
					print(f"You defeated the {enemy}!")
					Player_Stats["enemies killed"]+=1
					drop_loot(enemy)
					return
				enemy_ai()

		elif option.upper() == "B":
			while True:
				if len(Bag) <= 0:
					print("You have nothing in your bag!")
					break
				elif HP == max_HP and Engy == max_Engy:
					print("You don't need to use anything right now!")
					break
				else:
					print("You open your bag.")
					open_bag()
					print("[X] Close bag")
					item_sel = input("--> ")
					if item_sel.upper() == "X":
						break

					if item_sel in Bag:
						if Bag[item_sel]["type"] == "HP":
							if HP == max_HP:
								print("You don't need to heal.")
							else:
								HP += int(Bag[item_sel]["effect"])
								HP = min(HP, max_HP)

						elif Bag[item_sel]["type"] == "Energy":
							if Engy == max_Engy:
								print("You don't need energy.")
							else:
								Engy += int(Bag[item_sel]["effect"])
								Engy = min(Engy, max_Engy)

						print(f"Used {item_sel}.")
						Bag[item_sel]["amount"] -= 1

						if Bag[item_sel]["amount"] == 0:
							del Bag[item_sel]
						break

		elif option.upper() == "C":
			print("You prepare to block...")
			Engy = min(Engy + 2, max_Engy)
			enemy_ai()

		elif option.upper() == "D":
			print("You try to run away...")
			if random.randint(1, 10) == 1:
				print("You ran away!")
				return
			else:
				print("But you failed!")
			enemy_ai()
		else:
			print("invalid option")
	
def gameplay():
	global location
	def player_options():
		if location=="base":
			print("\nwhat will you do?")
			print("----------------------------")
			print("[A] talk to weaponsmith")
			print("[B] talk to armorsmith")
			print("[C] talk to Tom Nook")
			print("[D] talk to your crush")
			print("[E] talk to gandalf")
			print("[F] go somewhere else")
			print("[X] open menu")
		else:
			print("\nwhat will you do?")
			print("----------------------------")
			print(f"[A] explore {location}")
			print("[B] go somwhere else")
			print("[X] open menu")
		return input("-->  ")
	def travel_menu():
		print("\nwhere will you go?")
		print("----------------------------")
		print("[A] supermarket")
		print("[B] scrapyard")
		print("[C] farm")
		print("[D] base")
		print("[X] do something else")
		
		travel_option = input("--> ")
		global location
		past_location=location
		if travel_option.upper() == "A":
			location = "supermarket"
		elif travel_option.upper() == "B":
			location = "scrapyard"
		elif travel_option.upper() == "C":
			location = "farm"
		elif travel_option.upper() == "D":
			location = "base"
		elif travel_option.upper() == "X":
			return
		
		if location == past_location:
			print("You are already here!")
		else:
			print(f"You go to the {location}")
	
	while True:
		print(f"\nyou are at the {location}")
		option=player_options()
		if location=="base":
			if option.upper()=="A":
				if quest_status["weaponsmith"]=="complete":
					print("\nWeaponsmith: You know, the smell of metal makes me WAKE UP every morning")
					print("...")
					print("a sense of uncertainty washes over you")
				else:
					print("\nWeaponsmith: I can upgrade your sword for 5 scrap")
					print("[A] 'I have 5 scrap!'")
					print("[B] 'nevermind'")
					dialogue_choice=input("-->  ")
					if dialogue_choice.upper()=="A":
						if Loot_Bag["scrap"]<5:
							print("you dont have enough scrap!")
							
						else:
							print("Weaponsmith: heres your new sword pal!")
							print("+5 dmg")
							Player_Stats["DMG"]+=5
							Loot_Bag["scrap"]-=5
							quest_status["weaponsmith"]="complete"
						
					elif dialogue_choice.upper()=="B":
						print("you walk away")
			elif option.upper()=="B":
					if quest_status["armorsmith"]=="complete":
						print("\nArmorsmith: My dad used shoulder plates to WAKE me UP once")
						print("...")
						print("you feel as if you are forgetting something")
					else:
						print("\nArmorsmith: I can make you some armor for 3 scrap and 5 leather")
						print("[A] 'I have 3 scrap and 5 leather!'")
						print("[B] 'nevermind'")
						dialogue_choice=input("-->  ")
						if dialogue_choice.upper()=="A":
							if Loot_Bag["scrap"]<3 or Loot_Bag["leather"]<5:
								print("you dont have enough materials!")
								
							else:
								print("Armorsmith: heres your new armor pal!")
								print("+5 armor")
								Player_Stats["Armor"]+=5
								Loot_Bag["scrap"]-=3
								Loot_Bag["leather"]-=5
								quest_status["armorsmith"]="complete"
							
						elif dialogue_choice.upper()=="B":
							print("you walk away")
			elif option.upper()=="C":
				print("\nTom Nook: Feel free to buy or sell anything at my shop!")
				print("[A] open shop")
				print("[B] walk away")
				dialogue_choice=input("-->  ")
				if dialogue_choice.upper()=="A":
					shop()
				elif dialogue_choice.upper()=="B":
					print("you walk away")
			elif option.upper()=="D":
				if quest_status["crush"]=="complete":
						print("\nCrush: These chocolates give me a reason to WAKE UP every morning")
						print("...")
						print("this cant be real. why are they here?")
				else:
					print("\nCrush: Do you have chocolates for me?")
					print("[A] 'sure!'")
					print("[B] 'nah'")
					dialogue_choice=input("-->  ")
					if dialogue_choice.upper()=="A":
						if Loot_Bag["chocolates"]<1:
							print("Crush: you liar!")
							Player_Stats["HP"]-=5
						else:
							Loot_Bag["chocolates"]-=1
							Player_Stats["HP"]+=25
							print("Crush: Thank you so much!")
							quest_status["crush"]="complete"						
					elif dialogue_choice.upper()=="B":
						print("oh, you can find them at the supermarket")						
			elif option.upper() == "E":
				if quest_status["gandalf"] == "1st":
					if quest_status["weaponsmith"] == "complete":
						print("\nGandalf: Ah, I see you have strengthened your sword. Your first task is to find a map at the farm.")
						print("[A] 'I'll find it!'")
						print("[B] 'Maybe later.'")
						dialogue_choice = input("--> ")
						if dialogue_choice.upper() == "A":
							print("Gandalf: Good! Return to me once you have the map.")
							quest_status["gandalf"] = "map quest"
						elif dialogue_choice.upper() == "B":
							print("Gandalf: Very well, return when you are ready.")
					else:
						print("\nGandalf: You are not ready. Strengthen your sword first.")
				elif quest_status["gandalf"] == "map quest":
					if Loot_Bag["map"] > 0:
						print("\nGandalf: Ah, you found the map! But you are still too vulnerable. You must upgrade your armor.")
						Loot_Bag["map"]=0
						quest_status["gandalf"] = "armor requirement"
					else:
						print("\nGandalf: You haven't found the map yet. Seek it at the farm.")
			
				elif quest_status["gandalf"] == "armor requirement":
					if quest_status["armorsmith"] == "complete":
						print("\nGandalf: You are ready for this next task, but are you ready for the foes you will fight within?.")
						print("[A] 'I am ready'")
						print("[B] 'Ill do this later'")
						dialogue_choice=input("-->  ")
						if dialogue_choice.upper()=="A":
							print("Gandalf: Very well, I shall bring you there")
							print("Gandalf brings you to the cave")
							print("Gandalf: Return when you have the artifact")
							quest_status["gandalf"] = "artifact quest"
							location="cave"
						elif dialogue_choice.upper()=="B":
							print("Gandalf: Return when you are ready.")
					else:
						print("\nGandalf: You need stronger armor before continuing. Speak to the armorsmith.")
			
				elif quest_status["gandalf"] == "artifact quest":
					if Loot_Bag["artifact"] > 0:
						print("\nGandalf: You have returned with the artifact. But you must be even stronger for the final challenge.")
						Loot_Bag["artifact"]=0
						quest_status["gandalf"] = "health requirement"
			
				elif quest_status["gandalf"] == "health requirement":
					if quest_status["crush"] == "complete":
						print("Gandalf: You have gained the strength you need, but are you prepared to come with me to fix this?")
						print("[A] 'Lets do this!'")
						print("[B] 'Let me gather my thoughts first'")
						dialogue_choice=input("-->  ")
						if dialogue_choice.upper()=="A":
							print("Gandalf: Very well, let us set off to the rift zone to patch the rift and fix this mess.")
							print("you and the whole group journey to the rift zone")
							boss_cutscene()
						if dialogue_choice.upper()=="B":
							print("Gandalf: Return when you are ready.")
					else:
						print("\nGandalf: You are not yet strong enough. Perhaps there is someone who can make you stronger?")

				#quest accept		
			elif option.upper()=="F":
				travel_menu()
				#travel
			elif option.upper()=="X":
				menu()	
		else:
			if option.upper() == "A":
				print(f"You explore the {location}.")
				if location=="rift zone":
					boss_cutscene()
				else:
					if random.randint(1,3)==1:
						fighting()
					elif random.randint(1,3)==2:
						if random.randint(1,5)==1:
							rand_encounters(location)
					if location=="supermarket" and quest_status["crush"]=="incomplete":
						if random.randint(1,20)==1:
							if Loot_Bag["chocolates"]<1:
								print("you found chocolates!")
								Loot_Bag["chocolates"]+=1
					if location=="farm" and quest_status["gandalf"] == "map quest":
						if random.randint(1,30)==1:
							print("you found a map!")
							Loot_Bag["map"]+=1
			elif option.upper() == "B":
				if location=="cave":
					if Loot_Bag["artifact"]>0:
						travel_menu()
					else:
						print("you cant leave until you finish your business here")
				elif location=="rift zone":
					print("you must finish the fight")
				else:
					travel_menu()  # Allow the player to go somewhere else
			elif option.upper() == "X":
				menu()
def game():
	title_screen()
	gameplay()


game()