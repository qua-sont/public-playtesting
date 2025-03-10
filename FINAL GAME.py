import random,time,sys

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

Player_Stats = {"HP": 80, "Armor": 10, "DMG": 15, "Energy": 20,"enemies killed":0}
bells=500000

Consumable_info = {
	"apple": {"type": "HP", "restoration": "15","sell price":10},
	"energy drink": {"type": "Energy", "restoration": "5","sell price":10},
	"edible oil": {"type": "Energy", "restoration": "10","sell price":20},
	"full heal": {"type": "HP","sell price":35},
	"beef": {"type": "HP", "restoration": 30,"sell price":40}
}
Loot_Bag={}
Bag = {
	"apple": {"type": Consumable_info["apple"]["type"], "amount": 1, "effect": Consumable_info["apple"]["restoration"]},
	"full heal":{"type":Consumable_info["full heal"]["type"],"amount":1}
}

E_str = {
	"shadow": 15,
	"hobo": 15,
	"karen": 20,
	"animatronic": 25,
	"freddy fazbear": 30,
	"farmer": 10,
	"bull": 5,
	"Otis": 30,
	"spider horde": 25,
	"cave goblin": 30,
	"muffet":40,
	"fish":[25,35,50]
}

E_HP = {
	"shadow": 45,
	"hobo": 80,
	"karen": 120,
	"animatronic": 120,
	"freddy fazbear": 150,
	"farmer": 100,
	"bull": 110,
	"Otis": 150,
	"spider horde":75,
	"cave goblin":140,
	"muffet":200,
	"fish":500
}

E_heal = {
	"shadow": 10,
	"hobo": 10,
	"karen": 15,
	"animatronic": 5,
	"freddy fazbear": 5,
	"farmer": 15,
	"bull": 10,
	"Otis": 15,
	"spider horde":5,
	"cave goblin":10,
	"muffet":15,
	"fish":75
}

Loot = {
	"hobo": ["apple", "energy drink","scrap","leather"],
	"karen":  ["apple", "energy drink","full heal"],
	"animatronic":["scrap", "edible oil"],
	"freddy fazbear": ["scrap", "edible oil"],
	"farmer":["apple","leather"],
	"bull":["leather","beef"],
	"Otis":  ["leather","beef","leather"],
	"spider horde":["apple","energy drink"],
	"cave goblin":["apple","energy drink"],
	"muffet":["artifact","apple","energy drink","full heal"]
}

enemies = {
	"supermarket":["hobo","karen",],
	"scrapyard":["hobo","animatronic","freddy fazbear"],
	"farm":["farmer","bull","Otis"],
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

def say(dialouge, sec):
	def print_slow(str):
	    for c in str + '\n':
	    	sys.stdout.write(c)
	    	sys.stdout.flush()
	    	time.sleep(3./90)
	    print_slow(dialouge)
	    time.sleep(sec)






def lose_cutscene():
	print_slow("you died...")
	time.sleep(1)
	print_slow("...but you hear a noise")
	time.sleep(1)
	print_slow("beep... beep.... beep...")
	time.sleep(1)
	print_slow(f"{Name}: Oh no! Im gonna be late for school!")
	time.sleep(1)
	print_slow(f"{Name}: I shouldve never stayed up last night!")
	time.sleep(1)
	print_slow("GAME OVER")
	exit(0)

def final_cutscene():
	print_slow("the fish collapses")
	time.sleep(1)
	print_slow("a bright light goes off")
	time.sleep(1)
	print_slow("beep... beep.... beep...")
	time.sleep(1)
	print_slow("you wake up, without your headache this time...")
	time.sleep(1)
	print_slow(f"{Name}: Was it all a dream?")
	time.sleep(1)
	print_slow("you finally get ready for school and to face the day")
	time.sleep(1)
	print_slow(f"{Name}: Alright, lets do this")
	time.sleep(1)
	print_slow("the end")
	exit(0)

def boss_cutscene():
	global location
	print_slow("you explore the rift zone...")
	time.sleep(1)
	print_slow("but something is... off")
	time.sleep(1)
	print_slow("the world distorts and your friends disappears")
	time.sleep(1)
	print_slow("the faint sound of a bell thrashes your mind")
	time.sleep(1)
	print_slow("then it hits you.")
	time.sleep(1)
	print_slow("this isnt real. it never was.")
	time.sleep(1)
	priprint_slownt("you have to wake up.")
	time.sleep(1)
	print_slow("you rush to patch the rift to wake yourself up when suddenly...")
	time.sleep(1)
	print_slow("you are washed away by a tide!")
	time.sleep(1)
	location="rift zone"
	fighting()

def opening_cutscene():
	say(f"\n{Name}: My head is ringing right now", 1)
	print_slow(f"{Name}: I shouldnt have stayed up that late...")
	print_slow(f"{Name}: I have to get ready for school now.")
	print_slow(f"{Name}: Mom are you there?")
	print_slow("you are greeted with silence")
	print_slow(f"{Name}: Oh well, no time to waste")
	global option
	def house_options():
			print_slow("\nI should get ready for school, what should I do?")
			print("---------------------------------")
			print("[A] eat breakfast")
			print("[B] take a shower")
			print("[C] wear something proper")
			print("[D] leave for school")
			return input("-->  ").upper()
	while True:
			option=house_options()
			time.sleep(1)
			if option == "A":
				if Player_Stats["HP"] <100:
					print_slow("you ate breakfast")
					Player_Stats["HP"]+=20
				else:
					print_slow("you already ate breakfast")
			if option == "B":
				if Player_Stats["Energy"] <30:
					print_slow("you take a shower")
					Player_Stats["Energy"]+=10
				else:
					print_slow("you already took a shower")
			if option == "C":
				if Player_Stats["Armor"] <15:
					print_slow("you wear proper uniform")
					Player_Stats["Armor"]+=5
				else:
					print_slow("you already wore your uniform")
			if option=="D" :
				time.sleep(.2)
				print_slow("you leave for school")
				break
	print_slow("you go outside your house to go to school")
	print_slow("a figure approaches...")
	fighting()
	print_slow(f"{Name}: Whoah a sword!")
	print_slow("you store the sword in your rather spacious bag")
	print_slow(f"{Name}: I dont remember my bag being this big?")
	time.sleep(2)
	print_slow("youre cut off by a rustling in the bushes...")
	time.sleep(2)
	choice=input("approach the bush? (y/n) \n").upper()
	time.sleep(1)
	while choice not in ["Y","N"]:
		print_slow("not an option, please try again")
		choice=input("approach the bush? (y/n) \n").upper()
	if choice=="Y":
		time.sleep(1)
		print_slow("you carefully walk up to the bush...")
		time.sleep(1)
		print_slow("something jumps at you!")
		time.sleep(2)
		print_slow("???: Mayor! Im so glad youre here! Where did all the people go?!")
		time.sleep(1)
		print_slow("you freeze before uttering the words...")
		time.sleep(1.5)
		print_slow(f"{Name}: Tom Nook?!?!")
		time.sleep(2)
		print_slow("Tom Nook: Who else would it be? Now tell me where everyone went before I increase your debt!")
		time.sleep(2)
		print_slow(f"{Name}: But how? Youre not even real!")
		time.sleep(2)
		print_slow("Tom Nook: What do you mean 'not real'? Thats impossible!")
		time.sleep(1.5)
		print_slow("How can I be fake if theres others like me?")
		time.sleep(2)
		print_slow(f"{Name}: Theres more of you?")
		time.sleep(2)
		print_slow("Tom Nook: Follow me! Ill show you where they are!")
	elif choice=="N":
		print_slow("you ignore the sounds")
		time.sleep(2)
		print_slow("you hear tiny steps!")
		time.sleep(1.5)
		print_slow("you try to turn, but!")
		time.sleep(2)
		print_slow("a bag is placed over your head")
		time.sleep(2)
		print_slow(f"{Name}: Who are you!?!")
		time.sleep(2)
		print_slow("???: Dont worry mayor! Im only here to help!")
		time.sleep(2)
		print_slow(f"{Name}: Mayor?! Are you Tom Nook?!?")
		time.sleep(2)
		print_slow("Tom Nook: The one and only!")
		time.sleep(2)
		print_slow("you lift the bag off your head")
		time.sleep(2)
		print_slow(f"{Name}: Why did you try to kidnap me?")
		time.sleep(2)
		print_slow("Tom Nook: The others wanted me to bring you back because they need your help")
		time.sleep(2)
		print_slow(f"{Name}: Theres others?")
		time.sleep(2)
		print_slow("Tom Nook: Follow me and I will show you!")
	time.sleep(2)
	print_slow("you arrive at the base")
	time.sleep(2)
	print_slow("Tom Nook: You can talk to the people here, they can help boost you and possibly help you fix this mess!")
	return
		
def title_screen():
	global option,Name
	def credits():
		print_slow("\nLead Developer \nAndre Quimpo")
		print_slow("\nCo-Developers \nJacob Garganza \nAenon Magabat")
		print_slow("\nPlaytesters \nAlonzo Pahilanga\n")
	def title_options():
		if tutorial:
			say("\nWELCOME TO FEVER DREAM")
			print("[A] start game")
			print("[B] credits")
			print("[X] exit")
		else:
			print_slow("\nWELCOME TO FEVER DREAM")
			print("[A] continue game")
			print("[B] credits")
			print("[X] exit")
		return input("-->  ").upper()
	while True:
		option=title_options()
		if option =="A":
			if tutorial:
				Name=input("what is your name?\n")
				print_slow(f"Oh! {Name} is such a nice name!")
				time.sleep(1)
				opening_cutscene()
				return
			else:
				menu()
		elif option =="B":
			credits()
		elif option=="X":
			print_slow("leaving game...")
			exit(0)
		else:
			print("invalid input")
	
def menu():
	global bells
	while True:
		print("\nPAUSED")
		print("[A] Resume Game")
		print("[B] Check Stats")
		print("[C] Random Hint")
		print("[X] Exit to Title Screen")
		menu_option = input("-->  ").upper()

		if menu_option == "A":
			gameplay()  # Resumes game
		elif menu_option == "B":
			for key, value in Player_Stats.items():
				print_slow(f"{key}: {value}")
		elif menu_option =="C":
			print_slow(random.choice(hints))
		elif menu_option == "X":
			title_screen()  # Returns to title screen
		else:
			print_slow("Invalid input, try again.")

def rand_encounters(location):
	global bells
	print("")
	encounter_type = random.choice(["positive", "negative"])

	if encounter_type == "negative":
		if location == "supermarket":
			print_slow("You see a little boy crying in the aisle.")
			print_slow("Mister, have you seen my mommy?")
			while True:
				print("[A] Help him find his mother")
				print("[B] Ignore him and move on")
				choice = input("--> ").upper()
				time.sleep(1)
				if choice == "A":
					print_slow("As you help Timmy, a wild Karen appears!")
					print_slow("Karen: Why are you talking to my child?!")
					print_slow("Karen: For that, I will take 25 bells!")
					if bells < 25:
						if bells == 0:
							print_slow("Karen: Wow. Just wow. Not even a single bell")
						else:
							print_slow("Karen: Wowww, you don't even have 25 bells.\n-{bells} bells")
							bells = 0
					else:
						print_slow(f"Karen: Thanks for the bells, loser!\n-{bells} bells")
						bells -= 25
					break
				elif choice == "B":
					print_slow("You pretend not to hear him and continue shopping.")
					break
				else:
					print_slow("Invalid input! Please enter A or B.")

		elif location == "scrapyard":
			print_slow("A figure is running towards you.")
			while True:
				print("[A] Ask where he's going")
				print("[B] Ignore him and move on")
				choice = input("--> ").upper()
				time.sleep(1)
				if choice == "A":
					print_slow("He crashes into you and takes something from your bag!")
					if Bag:
						random_item = random.choice(list(Bag.keys()))
						print_slow(f"You lost {random_item}!")
						Bag[random_item]["amount"] -= 1
						if Bag[random_item]["amount"] == 0:
							del Bag[random_item]
					else:
						print_slow("Luckily, your bag was empty!")
					break
				elif choice == "B":
					print_slow("You step aside and avoid him.")
					break
				else:
					print_slow("Invalid input! Please enter A or B.")

		elif location == "farm":
			print_slow("A sickly man coughs as he approaches you.")
			print_slow("Sick Man: Do you have any medicine...?")
			while True:
				print("[A] Try to help him")
				print("[B] Walk away quickly")
				choice = input("--> ").upper()
				time.sleep(1)
				if choice == "A":
					print_slow("You get too close... He coughs in your face!")
					Player_Stats["HP"] -= 5
					print_slow("You feel a little weaker. \n-5 HP")
					break
				elif choice == "B":
					print_slow("You avoid him and move on.")
					break
				else:
					print_slow("Invalid input! Please enter A or B.")

	else:  # Positive encounter
		if location == "supermarket":
			print_slow("You spot a gangster carrying a baby.")
			if sidequest_status["yakuza"] == "complete":
				print_slow("You wave at each other.")
				return
			while True:
				print("[A] Offer him a baby formula")
				print("[B] Ignore him and continue shopping")
				choice = input("--> ").upper()
				time.sleep(1)
				if choice == "A":
					if "baby formula" in Loot_Bag:
						del Loot_Bag["baby formula"]
						print_slow("The gangster smirks and hands you 50 bells.")
						bells += 50
						sidequest_status["yakuza"] = "complete"
					else:
						print_slow("You don't have any baby formula!")
						print_slow("You walk away.")
					break
				elif choice == "B":
					print_slow("You walk past him without a second thought.")
					break
				else:
					print_slow("Invalid input! Please enter A or B.")

		elif location == "scrapyard":
			print_slow("You see a knight from the Crusades inspecting a pile of scrap.")
			while True:
				print("[A] Give him 5 scrap")
				print("[B] Leave him be")
				choice = input("--> ").upper()
				time.sleep(1)
				if choice == "A":
					if "scrap" in Loot_Bag and Loot_Bag["scrap"] >= 5:
						Loot_Bag["scrap"] -= 5
						if Loot_Bag["scrap"]<1:
							del Loot_Bag["scrap"]
						print_slow("Crusader: Thank you, kind traveler. Here, have my Holy Water.\n+1 full heal")
						print_slow(f"{Name}: This is a full heal..?")
						print_slow("The crusader runs off.")
						if "full heal" in Bag:
							Bag["full heal"]["amount"] += 1
						else:
							Bag["full heal"] = {"type": "HP", "amount": 1}
					else:
						print_slow("You don't have enough scrap!")
						print_slow("The crusader runs off.")
					break
				elif choice == "B":
					print_slow("You let him be and continue exploring.")
					break
				else:
					print_slow("Invalid input! Please enter A or B.")

		elif location == "farm":
			print_slow("A pale warrior is sharpening his blades near the crops.")
			if sidequest_status["kratos"] == "complete":
				print_slow("You wave at each other.")
				return
			while True:
				print("[A] Offer him a Heineken")
				print("[B] Leave him alone")
				choice = input("--> ").upper()
				time.sleep(1)
				if choice == "A":
					if "heineken" in Loot_Bag:
						del Loot_Bag["heineken"]
						print_slow("He grunts in approval and strengthens your weapon. \n+5 DMG")
						Player_Stats["DMG"] += 5
						sidequest_status["kratos"] = "complete"
					else:
						print_slow("You don't have a Heineken!")
						print_slow("He gestures for you to leave.")
					break
				elif choice == "B":
					print_slow("You keep your distance and continue exploring.")
					break
				else:
					print_slow("Invalid input! Please enter A or B.")

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
			if choice in items:
				item, cost = items[choice]
				if bag_check()>=max_Space:
					print("you have no more space in your bag")
					return
				if bells >= cost:
					print(f"bought {item}")
					bells -= cost
					if item in Consumable_info:
						if item in Bag:
							Bag[item]["amount"] += 1
						else:
							Bag[item] = {"type": Consumable_info[item]["type"],"amount": 1,"effect": Consumable_info[item]["restoration"]}
					else:
						if item in Loot_Bag:
							print(f"Tom Nook: Im afraid I have no more {item} in stock")
						else:
							Loot_Bag[item]=1
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
			sell_choice=input("--> ").lower()
			if sell_choice=="x":
				break
			else:
				if sell_choice in Bag:
					print_slow(f"sold {sell_choice}")
					bells+=Consumable_info[sell_choice]["sell price"]
					Bag[sell_choice]["amount"]-=1
					if Bag[sell_choice]["amount"] == 0:
						del Bag[sell_choice]
				else:
					print_slow("you dont have that item")
	while True:
		print_slow("\nTom Nook: Welcome to my shop!")
		print("[A] buy items")
		print("[B] sell items")
		print("[X] leave shop")
		dialogue_choice=input("-->  ").upper()
		if dialogue_choice=="A":
			buy()
		elif dialogue_choice=="B":
			sell()
		elif dialogue_choice=="X":
			print_slow("you walk away")
			break
		else:
			print_slow("invalid input, try again")

def bag_check():
	return sum(item["amount"] for item in Bag.values())

def open_bag():
	print_slow("HP items")
	for item, data in Bag.items():
		if data["type"] == "HP":
			if item=="full heal":
				print_slow(f"{item}(s): {data['amount']}")
				print_slow(f"Heals {Player_Stats['HP']} {data['type']}")
			else:
				print_slow(f"{item}(s): {data['amount']}")
				print_slow(f"Restores {data['effect']}")
	print_slow("\nEnergy items")
	for item, data in Bag.items():
		if data["type"] == "Energy":
			print_slow(f"{item}(s): {data['amount']}")
			print_slow(f"Restores {data['effect']} {data['type']}")

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

		print_slow(f"A shadowy figure appears... ")

		# **Basic Attack Tutorial**
		print_slow("Hint: Try attacking! (Press 'A')")
		while True:
			option=fight_options()
			if option == "A":
				print_slow(f"You strike the {enemy}!")
				Engy -= 4  # Energy deduction
				F_HP -= DMG
				break
			else:
				print_slow("Hint: You should attack.")

		# **Enemy Counterattack**
		print_slow(f"The {enemy} strikes back!")
		HP -= E_dmg
		print("Hint: After every round, you restore 2 energy.")
		Engy = min(Engy + 2, max_Engy)

		# **Dodge Tutorial**
		print("\nHint: The enemy is attacking, try dodging! (Press 'C')")
		while True:
			option = fight_options()
			if option == "C":
				print_slow(f"The {enemy} attacks...")
				print_slow("But you dodged it!")
				Engy=min(Engy+2,max_Engy)
				break
			else:
				print("Hint: You should dodge.")

		# **Healing Tutorial**
		print("Hint: You're injured, try healing using an item (Press 'B')")
		while True:
			option = fight_options()
			if option == "B":
				print_slow("You open your bag:")
				open_bag()
				while True:
					item_sel = input("Use -->  ").lower()
					if item_sel in Bag and Bag[item_sel]["amount"] > 0:
						if Bag[item_sel]["type"] == "HP":
							HP += int(Bag[item_sel]["effect"])  # Ensure healing is an integer
							HP = min(HP, max_HP)  # Prevent overhealing
							print_slow(f"Used {item_sel}.")
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

			if option == "A":
				Engy-=4
				print_slow(f"You strike the {enemy}!")
				Engy=min(Engy+2,max_Engy)
				F_HP -= DMG
				if F_HP <= 0:
					break
				if random.randint(1,2)==1:
					print_slow(f"The {enemy} heals itself!")
					F_HP = min(F_HP + E_heal[enemy], max_EHP)
				else: 
					print_slow(f"the {enemy} does nothing")
			elif option == "B":
				print("Hint: There are no more tutorial items, try another option.")

			elif option == "C":
				print_slow(f"You hesitate...")
				Engy=min(Engy+2,max_Engy)
				if random.randint(1,2)==1:
					print_slow(f"The {enemy} heals itself!")
					F_HP = min(F_HP + E_heal[enemy], max_EHP)
				else: 
					print_slow("you both do nothing")

			elif option == "D":
				print("Hint: You cannot run in the tutorial.")

		print_slow(f"\nYou defeated the {enemy}!")
		print_slow(f"The {enemy} dropped a sword!")
		print_slow("Obtained sword! \n+5 DMG!")
		Player_Stats["DMG"] += 5
		tutorial = False
		time.sleep(3)
		return
	
	def drop_loot():
		global enemy
		if enemy=="fish":
			final_cutscene()
		def cash_drop():
			global bells
			if random.randint(1,2)==1:
				M_drop=random.randint(1,25)
				print_slow(f"the {enemy} also dropped {M_drop} bells!")
				bells+=M_drop
		
		global max_Space
		loot_roll = random.randint(1, 6)
		if loot_roll <= 5:
			chance="drop"
		else:
			chance = "no drop"
	
		if chance =="drop":
			item = random.choice(Loot[enemy])
			if item in Consumable_info:
				if bag_check()>=max_Space:
					print_slow(f"you leave the {item} because you have no space")
					cash_drop()
					return
				if item in Bag:
					Bag[item]["amount"] += 1
				else:
					if item=="full heal":
						Bag[item] = {"type": Consumable_info[item]["type"],"amount": 1}
					else:
						Bag[item] = {"type": Consumable_info[item]["type"],"amount": 1,"effect": Consumable_info[item]["restoration"]}
			else:
				if item in Loot_Bag:
					Loot_Bag[item] += 1
				else:
					Loot_Bag[item]=1
			print_slow(f"You received a {item}!")
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
		return input("--> ").upper()
		
	def boss_ai():
		global option
		nonlocal Blk_chance, F_HP, HP, Engy, max_Engy, DMG, max_HP, max_EHP
		B_atk1=E_str[enemy][0]
		B_atk2 =E_str[enemy][1]
		B_atk3 =E_str[enemy][2]
		enemy_act = random.randint(1, 5)
		if enemy_act == 1:
			Engy=min(Engy+2,max_Engy)
			print_slow(f"The {enemy} slaps you!")
			if option == "C":
				print_slow("But you dodged it!")
				option = "null"
				return            
			block = random.randint(1, Blk_chance)
			if block == 1:
				print_slow("But you blocked it!")
			else:
				print_slow("You were hit!")
				HP -= B_atk1   
			option = "null"
		elif enemy_act == 2:
			print_slow(f"The {enemy} spawns a tsunami!")
			Engy=min(Engy+2,max_Engy)
			if option == "C":
				print_slow("But you dodged it!")
				option = "null"
				return            
			block = random.randint(1, Blk_chance)
			if block == 1:
				print_slow("But you blocked it!")
			else:
				prinprint_slowt("You were hit!")
				HP -= B_atk2
			option = "null"
		elif enemy_act == 3:
			print_slow(f"The {enemy} bites you!")
			Engy=min(Engy+2,max_Engy)
			if option == "C":
				print_slow("But you dodged it!")
				option = "null"
				return            
			block = random.randint(1, Blk_chance)
			if block == 1:
				print_slow("But you blocked it!")
			else:
				print_slow("You were hit!")
				HP -= B_atk3
			option = "null"
		elif enemy_act == 2:
			Engy=min(Engy+2,max_Engy)
			if F_HP < max_EHP:
				print_slow(f"The {enemy} heals!")
				F_HP = min(F_HP + E_heal[enemy], max_EHP)
		else:
			print_slow(f"The {enemy} flops around.")  
			option = "null"
			
	def enemy_ai():
		global option
		nonlocal Blk_chance, F_HP, HP, Engy, max_Engy, DMG, max_HP, max_EHP, E_dmg
		if enemy=="fish":
			boss_ai()
			return
		enemy_act = random.randint(1, 5)
		if enemy_act <=3:
			Engy=min(Engy+2,max_Engy)
			print_slow(f"The {enemy} attacks!")
			if option == "C":
				print_slow("But you dodged it!")
				option = "null"
				return            
			block = random.randint(1, Blk_chance)
			if block == 1:
				print_slow("But you blocked it!")
			else:
				print_slow("You were hit!")
				HP -= E_dmg  
			option = "null"
		elif enemy_act == 4:
			Engy=min(Engy+2,max_Engy)
			if F_HP < max_EHP:
				print_slow(f"The {enemy} heals!")
				F_HP = min(F_HP + E_heal[enemy], max_EHP)
			else:
				print_slow(f"The {enemy} stands still.")  
			option = "null"
		else:
			Engy=min(Engy+2,max_Engy)
			if option == "A":
				enemy_block = random.randint(1, 25)
				if enemy_block == 1:
					print_slow(f"The {enemy} blocked your attack!")
					F_HP += DMG
				else:
					print_slow(f"The {enemy} tried dodging your attack and failed.")
				option = "null"
			else:
				print_slow(f"The {enemy} does nothing.")


	if tutorial:
		tutorial_fight()
		return
	print_slow(f"The {enemy} suprises you!")
	while True:
		if HP<1:
			lose_cutscene()
		option = fight_options()

		if option == "A":
			if Engy < 4:
				print_slow("You don't have enough energy!")
				fight_options()
			else:
				print_slow(f"You strike the {enemy}!")
				Engy -= 4
				F_HP -= DMG
				if F_HP <= 0:
					print_slow(f"You defeated the {enemy}!")
					Player_Stats["enemies killed"]+=1
					drop_loot()
					return
				enemy_ai()

		elif option == "B":
			while True:
				if len(Bag) <= 0:
					("You have nothing in your bag!")
					break
				elif HP == max_HP and Engy == max_Engy:
					print("You don't need to use anything right now!")
					break
				else:
					print_slow("You open your bag.")
					open_bag()
					print("[X] Close bag")
					item_sel = input("--> ").lower()
					time.sleep(1)
					if item_sel == "x":
						break

					if item_sel in Bag:
						if Bag[item_sel]["type"] == "HP":
							if HP == max_HP:
								print_slow("You don't need to heal.")
							else:
								if item_sel=="full heal":
									HP=max_HP
								else:
									HP += int(Bag[item_sel]["effect"])
									HP = min(HP, max_HP)

						elif Bag[item_sel]["type"] == "Energy":
							if Engy == max_Engy:
								print_slow("You don't need energy.")
							else:
								Engy += int(Bag[item_sel]["effect"])
								Engy = min(Engy, max_Engy)

						print_slow(f"Used {item_sel}.")
						Bag[item_sel]["amount"] -= 1

						if Bag[item_sel]["amount"] == 0:
							del Bag[item_sel]
						break

		elif option == "C":
			print_slow("You prepare to block...")
			Engy = min(Engy + 2, max_Engy)
			enemy_ai()

		elif option == "D":
			print_slow("You try to run away...")
			time.sleep(1.5)
			if random.randint(1, 5) == 1:
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
		while True:
			if location == "base":
				print("\nWhat will you do?")
				print("----------------------------")
				print("[A] Talk to weaponsmith")
				print("[B] Talk to armorsmith")
				print("[C] Talk to Tom Nook")
				print("[D] Talk to your crush")
				print("[E] Talk to Gandalf")
				print("[F] Check loot")
				print("[G] Go somewhere else")
				print("[X] Open menu")
			else:
				print("\nWhat will you do?")
				print("----------------------------")
				print(f"[A] Explore {location}")
				print("[B] Go somewhere else")
				print("[C] Open bag")
				print("[D] Check loot")
				print("[X] Open menu")

			option = input("--> ").upper()
			if option in ["A", "B", "C", "D", "E", "F","G", "X"]:
				return option
			print("Invalid input! Please enter a valid option.")

	def travel_menu():
		while True:
			print("\nWhere will you go?")
			print("----------------------------")
			print("[A] Supermarket")
			print("[B] Scrapyard")
			print("[C] Farm")
			print("[D] Base")
			print("[X] Do something else")

			travel_option = input("--> ").upper()
			time.sleep(1)
			global location
			past_location = location

			if travel_option == "A":
				location = "supermarket"
			elif travel_option == "B":
				location = "scrapyard"
			elif travel_option == "C":
				location = "farm"
			elif travel_option == "D":
				location = "base"
			elif travel_option == "X":
				return

			if location == past_location:
				print_slow("You are already here!")
			else:
				print_slow(f"You go to the {location}")
			break
	while True:
		print_slow(f"\nYou are at the {location}")
		option = player_options()

		if location == "base":
			if option == "A":
				if quest_status["weaponsmith"] == "complete":
					print_slow("\nWeaponsmith: You know, the smell of metal makes me WAKE UP every morning")
					print_slow("...")
					print_slow("A sense of uncertainty washes over you")
				else:
					print_slow("\nWeaponsmith: I can upgrade your sword for 5 scrap")
					while True:
						print("[A] 'I have 5 scrap!'")
						print("[B] 'Where do I find scrap?'")
						print("[C] 'Nevermind'")
						dialogue_choice = input("--> ").upper()
						if dialogue_choice == "A":
							if "scrap" not in Loot_Bag or Loot_Bag["scrap"] <= 5:
								print_slow("You don't have enough scrap!")
							else:
								print_slow("Weaponsmith: Here's your new sword, pal!\n+5 DMG")
								Player_Stats["DMG"] += 5
								Loot_Bag["scrap"] -= 5
								if Loot_Bag["scrap"]<1:
									del Loot_Bag["scrap"]
								quest_status["weaponsmith"] = "complete"
							break
						elif dialogue_choice == "B":
							print_slow("Scrap can be found in the scrapyard or as a random drop from hobos.")
							break
						elif dialogue_choice == "C":
							print_slow("You walk away.")
							break
						print("Invalid input! Please enter A, B, or C.")

			elif option == "B":
				if quest_status["armorsmith"] == "complete":
					print_slow("\nArmorsmith: My dad used shoulder plates to WAKE me UP once")
					print_slow("...")
					print_slow("You feel as if you are forgetting something")
				else:
					print_slow("\nArmorsmith: I can make you some armor for 3 scrap and 5 leather")
					while True:
						print("[A] 'I have 3 scrap and 5 leather!'")
						print("[B] 'Where do I find scrap and leather?'")
						print("[C] 'Nevermind'")
						dialogue_choice = input("--> ").upper()
						if dialogue_choice == "A":
							if "scrap" not in Loot_Bag or "leather" not in Loot_Bag:
								print("You don't have enough materials!")
								break
							else:
								if Loot_Bag["scrap"] < 3 or Loot_Bag["leather"] < 5:
									print("You don't have enough materials!")
									break
								else:
									print_slow("Armorsmith: Here's your new armor, pal!\n+5 Armor\n+25 HP")
									Player_Stats["Armor"] += 5
									Player_Stats["HP"] += 25
									Loot_Bag["scrap"] -= 3
									if Loot_Bag["scrap"]<1:
										del Loot_Bag["scrap"]
									Loot_Bag["leather"] -= 5
									if Loot_Bag["leather"]<1:
										del Loot_Bag["leather"]
									quest_status["armorsmith"] = "complete"
								break
						elif dialogue_choice == "B":
							print_slow("Scrap can be found at the scrapyard, while leather can be found at the farm. Hobos have a chance of dropping either item though.")
							break
						elif dialogue_choice == "C":
							print_slow("You walk away.")
							break
						print("Invalid input! Please enter A, B, or C.")

			elif option == "C":
				while True:
					print_slow("\nTom Nook: Feel free to buy or sell anything at my shop!")
					print("[A] Open shop")
					print("[B] Walk away")
					dialogue_choice = input("--> ").upper()
					if dialogue_choice == "A":
						shop()
						break
					elif dialogue_choice == "B":
						print_slow("You walk away.")
						break
					print("Invalid input! Please enter A or B.")

			elif option == "D":
				if quest_status["crush"] == "complete":
					print_slow("\nCrush: These chocolates give me a reason to WAKE UP every morning")
					print_slow("...")
					print_slow("This can't be real. Why are they here?")
				else:
					while True:
						print_slow("\nCrush: Do you have chocolates for me?")
						print("[A] 'Sure!'")
						print("[B] 'Where do I find chocolates?'")
						print("[C] 'Nah'")
						dialogue_choice = input("--> ").upper()
						if dialogue_choice == "A":
							if "chocolates" not in Loot_Bag:
								print_slow("Crush: You liar!")
								print_slow("She slaps you\n-5 HP")
								Player_Stats["HP"] -= 5
							else:
								del Loot_Bag["chocolates"]
								Player_Stats["HP"] += 25
								print_slow("Crush: Thank you so much!\n+25 HP!")
								quest_status["crush"] = "complete"
							break
						elif dialogue_choice == "B":
							print_slow("Oh, you can find them at the supermarket.")
							break
						elif dialogue_choice == "C":
							print_slow("You walk away.")
							break
						print("Invalid input! Please enter A, B, or C.")
			elif option.upper() == "E":  # Talking to Gandalf
				if quest_status["gandalf"] == "1st":
					if quest_status["weaponsmith"] == "complete":
						print_slow("\nGandalf: Ah, I see you have strengthened your sword. Your first task is to find a map at the farm.")
						while True:
							print("[A] 'I'll find it!'")
							print("[B] 'Maybe later.'")
							dialogue_choice = input("--> ").upper()
							if dialogue_choice == "A":
								print_slow("Gandalf: Good! Return to me once you have the map.")
								quest_status["gandalf"] = "map quest"
								break
							elif dialogue_choice == "B":
								print_slow("Gandalf: Very well, return when you are ready.")
								break
							else:
								print("Invalid choice! Please select A or B.")
					else:
						print_slow("\nGandalf: You are not ready. Strengthen your sword first.")
			
				elif quest_status["gandalf"] == "map quest":
					if Loot_Bag["map"] > 0:
						print_slow("\nGandalf: Ah, you found the map! But you are still too vulnerable. You must upgrade your armor.")
						del Loot_Bag["map"]
						quest_status["gandalf"] = "armor requirement"
					else:
						print_slow("\nGandalf: You haven't found the map yet. Seek it at the farm.")
			
				elif quest_status["gandalf"] == "armor requirement":
					if quest_status["armorsmith"] == "complete":
						print_slow("\nGandalf: You are ready for this next task, but are you ready for the foes you will fight within?")
						while True:
							print("[A] 'I am ready'")
							print("[B] 'I'll do this later'")
							dialogue_choice = input("--> ").upper()
							if dialogue_choice == "A":
								print_slow("Gandalf: Very well, I shall bring you there.")
								print_slow("Gandalf brings you to the cave.")
								print_slow("Gandalf: Return when you have the artifact.")
								quest_status["gandalf"] = "artifact quest"
								location = "cave"
								break
							elif dialogue_choice == "B":
								print_slow("Gandalf: Return when you are ready.")
								break
							else:
								print("Invalid choice! Please select A or B.")
					else:
						print_slow("\nGandalf: You need stronger armor before continuing. Speak to the armorsmith.")
			
				elif quest_status["gandalf"] == "artifact quest":
					if Loot_Bag["artifact"] > 0:
						print_slow("\nGandalf: You have returned with the artifact. But you must be even stronger for the final challenge.")
						del Loot_Bag["artifact"]
						quest_status["gandalf"] = "health requirement"
					else:
						print_slow("\nGandalf: You haven't found the artifact yet. Seek it in the cave.")
			
				elif quest_status["gandalf"] == "health requirement":
					if quest_status["crush"] == "complete":
						print_slow("Gandalf: You have gained the strength you need, but are you prepared to come with me to fix this?")
						while True:
							print("[A] 'Let's do this!'")
							print("[B] 'Let me gather my thoughts first'")
							dialogue_choice = input("--> ").upper()
							if dialogue_choice == "A":
								print_slow("Gandalf: Very well, let us set off to the rift zone to patch the rift and fix this mess.")
								print_slow("You and the whole group journey to the rift zone.")
								boss_cutscene()
								break
							elif dialogue_choice == "B":
								print_slow("Gandalf: Return when you are ready.")
								break
							else:
								print("Invalid choice! Please select A or B.")
					else:
						print_slow("\nGandalf: You are not yet strong enough. Perhaps there is someone who can make you stronger?")

			elif option == "F":
				for item,amount in Loot_Bag.items():
					print_slow(f"{item}: {amount}")
				print_slow(f"bells: {bells}")
			elif option == "G":
				travel_menu()

			elif option == "X":
				menu()

		else:
			if option == "A":
				print_slow(f"You explore the {location}.")
				if location == "rift zone":
					boss_cutscene()
				else:
					event = random.randint(1, 6)
					if event <= 4:
						fighting()
					elif event == 5:
						if random.randint(1, 3) == 1:
							rand_encounters(location)
					if location == "supermarket" and quest_status["crush"] == "incomplete":
						if random.randint(1, 15) == 1 and "chocolates" not in Loot_Bag:
							print_slow("You found chocolates!")
							Loot_Bag["chocolates"] = 1
					if location == "farm" and quest_status["gandalf"] == "map quest":
						if random.randint(1, 20) == 1 and "map" not in Loot_Bag:
							print_slow("You found a map!")
							Loot_Bag["map"] = 1

			elif option == "B":
				if location in ["cave", "rift zone"] and "artifact" not in Bag:
					print_slow("You can't leave until you get an artifact")
				else:
					travel_menu()
			elif option == "C":
				open_bag()
			elif option == "D":
				for item,amount in Loot_Bag.items():
					print_slow(f"{item}: {amount}")
				print_slow(f"bells: {bells}")
			elif option == "X":
				menu()
def game():
	title_screen()
	gameplay()


game()