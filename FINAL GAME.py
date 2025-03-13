import random,sys
from time import sleep as wait

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
	"karen": 15,
	"animatronic": 25,
	"freddy fazbear": 30,
	"farmer": 10,
	"bull": 20,
	"Otis": 25,
	"spider horde": 15,
	"cave goblin": 20,
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

def say(dialogue, sec):
	def print_slow(str, time):
		for c in str + '\n':
			sys.stdout.write(c)
			sys.stdout.flush()
			wait(3./90)
		wait(time)
	print_slow(dialogue, sec)






def lose_cutscene():
	say("you died...", 1)
	say("...but you hear a noise", 1)
	say("beep... beep.... beep...", 1)
	say(f"{Name}: Oh no! I'm gonna be late for school!", 1)
	say(f"{Name}: I should've never stayed up last night!", 1)
	say("GAME OVER", 1)
	exit(0)


def final_cutscene():
	say("the fish collapses", 1)
	say("a bright light goes off", 1)
	say("beep... beep.... beep...", 1)
	say("you wake up, without your headache this time...", 1)
	say(f"{Name}: Was it all a dream?", 1)
	say("you finally get ready for school and to face the day", 1)
	say(f"{Name}: Alright, lets do this", 1)
	say("the end", 1)
	exit(0)

def boss_cutscene():
	global location
	say("you explore the rift zone...", 1)
	say("but something is... off", 1)
	say("the world distorts and your friends disappear", 1)
	say("the faint sound of a bell thrashes your mind", 1)
	say("then it hits you.", 1)
	say("this isn't real. it never was.", 1)
	say("you have to wake up.", 1)
	say("you rush to patch the rift to wake yourself up when suddenly...", 1)
	say("you are washed away by a tide!", 1)
	location = "rift zone"
	fighting()


def opening_cutscene():
	say(f"\n{Name}: My head is ringing right now", 1)
	say(f"{Name}: I shouldn't have stayed up that late...", 1)
	say(f"{Name}: I have to get ready for school now.", 1)
	say(f"{Name}: Mom, are you there?", 1)
	say("you are greeted with silence", 1)
	say(f"{Name}: Oh well, no time to waste", 1)
	global option
	def house_options():
		say("\nI should get ready for school, what should I do?",1)
		print("---------------------------------\n"  
			+ "[A] Eat breakfast\n"  
			+ "[B] Take a shower\n"  
			+ "[C] Wear something proper\n"  
			+ "[D] Leave for school")
		return input("-->  ").upper()
	while True:
		option = house_options()
		wait(1) 
		if option == "A":
			if Player_Stats["HP"] < 100:
				say("you ate breakfast", 1)
				Player_Stats["HP"] += 20
			else:
				say("you already ate breakfast", 1)
		if option == "B":
			if Player_Stats["Energy"] < 30:
				say("you take a shower", 1)
				Player_Stats["Energy"] += 10
			else:
				say("you already took a shower", 1)
		if option == "C":
			if Player_Stats["Armor"] < 15:
				say("you wear proper uniform", 1)
				Player_Stats["Armor"] += 5
			else:
				say("you already wore your uniform", 1)
		if option == "D":
			say("you leave for school", 1)
			break
	say("you go outside your house to go to school", 1)
	say("a figure approaches...", 1)
	fighting()  # Make sure the fighting function is defined elsewhere
	say(f"{Name}: Whoah a sword!", 2)
	say("you store the sword in your rather spacious bag", 2)
	say(f"{Name}: I don't remember my bag being this big?", 2)
	say("you're cut off by a rustling in the bushes...", 2)
	choice = input("approach the bush? (y/n) \n").upper()
	wait(1)
	while choice not in ["Y", "N"]:
		say("not an option, please try again", 1)
		choice = input("approach the bush? (y/n) \n").upper()
	if choice == "Y":
		say("you carefully walk up to the bush...", 1)
		say("something jumps at you!", 2)
		say("???: Mayor! I'm so glad you're here! Where did all the people go?!", 1)
		say("you freeze before uttering the words...", 1.5)
		say(f"{Name}: Tom Nook?!? ", 2)
		say("Tom Nook: Who else would it be? Now tell me where everyone went before I increase your debt!", 2)
		say(f"{Name}: But how? You're not even real!", 2)
		say("Tom Nook: What do you mean 'not real'? That's impossible!", 1.5)
		say("How can I be fake if there's others like me?", 2)
		say(f"{Name}: There's more of you?", 2)
		say("Tom Nook: Follow me! I'll show you where they are!", 1)
	elif choice == "N":
		say("you ignore the sounds", 1)
		say("you hear tiny steps!", 1.5)
		say("you try to turn, but!", 2)
		say("a bag is placed over your head", 2)
		say(f"{Name}: Who are you!?!", 2)
		say("???: Don't worry mayor! I'm only here to help!", 2)
		say(f"{Name}: Mayor?! Are you Tom Nook?!?", 2)
		say("Tom Nook: The one and only!", 2)
		say("you lift the bag off your head", 2)
		say(f"{Name}: Why did you try to kidnap me?", 2)
		say("Tom Nook: The others wanted me to bring you back because they need your help", 2)
		say(f"{Name}: There's others?", 2)
		say("Tom Nook: Follow me and I will show you!", 1)
	say("you arrive at the base", 2)
	say("Tom Nook: You can talk to the people here, they can help boost you and possibly help you fix this mess!", 2)
	return

		
def title_screen():
	global option, Name, tutorial
	def credits():
		say("\nLead Developer \nAndre Quimpo", 1)
		say("\nCo-Developers \nJacob Garganza \nAenon Magabat", 1)
		say("\nPlaytesters \nAlonzo Pahilanga\n", 1)

	def title_options():
		if tutorial:
			say("\nWELCOME TO FEVER DREAM",1)
			print("[A] Start game\n"  
				+ "[B] Credits\n"  
				+ "[X] Exit")
		else:
			say("\nWELCOME TO FEVER DREAM", 1)
			print("[A] Continue game\n"  
				+ "[B] Credits\n"  
				+ "[X] Exit")
		return input("-->  ").upper()

	while True:
		option = title_options()
		if option == "A":
			if tutorial:
				Name = input("what is your name?\n")
				say(f"Oh! {Name} is such a nice name!", 1)
				opening_cutscene()  # Assuming this is defined elsewhere
				return
			else:
				menu()  # Assuming this is defined elsewhere
		elif option == "B":
			credits()  # Assuming this is defined elsewhere
		elif option == "X":
			say("leaving game...", 1)
			exit(0)
		else:
			print("invalid input")
	
def menu():
	global bells
	while True:
		say("\nPAUSED", 1)
		print("[A] Resume Game\n"  
			+ "[B] Check Stats\n"  
			+ "[C] Random Hint\n"  
			+ "[X] Exit to Title Screen")
		menu_option = input("-->  ").upper()

		if menu_option == "A":
			gameplay()  # Resumes game
		elif menu_option == "B":
			for key, value in Player_Stats.items():
				print_slow(f"{key}: {value}", 1)
		elif menu_option == "C":
			print_slow(random.choice(hints), 1)
		elif menu_option == "X":
			title_screen()  # Returns to title screen
		else:
			print_slow("Invalid input, try again.", 1)


def rand_encounters():
	global bells,location
	encounter_type = random.choice(["positive", "negative"])

	if encounter_type == "negative":
		if location == "supermarket":
			say("\nYou see a little boy crying in the aisle.", 1)
			say("Mister, have you seen my mommy?", 1)
			while True:
				print("[A] Help him find his mother\n"  
					+ "[B] Ignore him and move on")
				choice = input("--> ").upper()
				wait(1)
				if choice == "A":
					say("As you help Timmy, a wild Karen appears!", 1)
					say("Karen: Why are you talking to my child?!", 1)
					say("Karen: For that, I will take 25 bells!", 1)
					if bells < 25:
						if bells == 0:
							say("Karen: Wow. Just wow. Not even a single bell", 1)
						else:
							say(f"Karen: Wowww, you don't even have 25 bells.\n-{bells} bells", 1)
							bells = 0
					else:
						say(f"Karen: Thanks for the bells, loser!\n-{bells} bells", 1)
						bells -= 25
					break
				elif choice == "B":
					say("You pretend not to hear him and continue shopping.", 1)
					break
				else:
					say("Invalid input! Please enter A or B.", 1)

		elif location == "scrapyard":
			say("\nA figure is running towards you.", 1)
			while True:
				print("[A] Ask where he's going\n"  
					+ "[B] Ignore him and move on")
				choice = input("--> ").upper()
				wait(1)
				if choice == "A":
					say("He crashes into you and takes something from your bag!", 1)
					if Bag:
						random_item = random.choice(list(Bag.keys()))
						say(f"You lost {random_item}!", 1)
						Bag[random_item]["amount"] -= 1
						if Bag[random_item]["amount"] == 0:
							del Bag[random_item]
					else:
						say("Luckily, your bag was empty!", 1)
					break
				elif choice == "B":
					say("You step aside and avoid him.", 1)
					break
				else:
					say("Invalid input! Please enter A or B.", 1)

		elif location == "farm":
			say("\nA sickly man coughs as he approaches you.", 1)
			say("Sick Man: Do you have any medicine...?", 1)
			while True:
				print("[A] Try to help him\n"  
					+ "[B] Walk away quickly")
				choice = input("--> ").upper()
				wait(1)
				if choice == "A":
					say("You get too close... He coughs in your face!", 1)
					Player_Stats["HP"] -= 5
					say("You feel a little weaker. \n-5 HP", 1)
					break
				elif choice == "B":
					say("You avoid him and move on.", 1)
					break
				else:
					say("Invalid input! Please enter A or B.", 1)

	else:  # Positive encounter
		if location == "supermarket":
			say("\nYou spot a gangster carrying a baby.", 1)
			if sidequest_status["yakuza"] == "complete":
				say("You wave at each other.", 1)
				return
			while True:
				print("[A] Offer him a baby formula\n"  
					+ "[B] Ignore him and continue shopping")
				choice = input("--> ").upper()
				wait(1)
				if choice == "A":
					if "baby formula" in Loot_Bag:
						del Loot_Bag["baby formula"]
						say("The gangster smirks and hands you 50 bells.", 1)
						bells += 50
						sidequest_status["yakuza"] = "complete"
					else:
						say("You don't have any baby formula!", 1)
						say("You walk away.", 1)
					break
				elif choice == "B":
					say("You walk past him without a second thought.", 1)
					break
				else:
					say("Invalid input! Please enter A or B.", 1)

		elif location == "scrapyard":
			say("\nYou see a knight from the Crusades inspecting a pile of scrap.", 1)
			while True:
				print("[A] Give him 5 scrap\n"  
					+ "[B] Leave him be")
				choice = input("--> ").upper()
				time.sleep(1)
				if choice == "A":
				    if "scrap" in Loot_Bag and Loot_Bag["scrap"] >= 5:
				        Loot_Bag["scrap"] -= 5
				        if Loot_Bag["scrap"] < 1:
				            del Loot_Bag["scrap"]
				        say("Crusader: Thank you, kind traveler. Here, have my Holy Water.\n+1 full heal", 1)
				        say(f"{Name}: This is a full heal..?", 1)
				        say("The crusader runs off.", 1)
				        if "full heal" in Bag:
				            Bag["full heal"]["amount"] += 1
				        else:
				            Bag["full heal"] = {"type": "HP", "amount": 1}
				    else:
				        say("You don't have enough scrap!", 1)
				        say("The crusader runs off.", 1)
				    break
				elif choice == "B":
				    say("You let him be and continue exploring.", 1)
				    break
				else:
				    say("Invalid input! Please enter A or B.", 1)
				
		elif location == "farm":
			say("\nA pale warrior is sharpening his blades near the crops.", 1)
			if sidequest_status["kratos"] == "complete":
				say("You wave at each other.", 1)
				return
			while True:
				print("[A] Offer him a Heineken\n"  
					+ "[B] Leave him alone")
				choice = input("--> ").upper()
				time.sleep(1)
				if choice == "A":
					if "heineken" in Loot_Bag:
						del Loot_Bag["heineken"]
						say("He grunts in approval and strengthens your weapon. \n+5 DMG", 1)
						Player_Stats["DMG"] += 5
						sidequest_status["kratos"] = "complete"
					else:
						say("You don't have a Heineken!", 1)
						say("He gestures for you to leave.", 1)
					break
				elif choice == "B":
					say("You keep your distance and continue exploring.", 1)
					break
				else:
					say("Invalid input! Please enter A or B.", 1)

def shop():
	def buy():
		global bells, max_Space
		bulk=0
		while True:
			say(f"\nbells: {bells}\n--------SHOP--------", 1)
			print("[A] Apple - 15 bells\n"  
				+ "[B] Energy drink - 15 bells\n"  
				+ "[C] Baby formula - 25 bells\n"  
				+ "[D] Full heal - 50 bells\n"  
				+ "[E] Heineken - 100 bells (ON SALE!!)\n"  
				+ "[X] Exit")

			items = {
				"A": ("apple", 15),
				"B": ("energy drink", 15),
				"C": ("baby formula", 25),
				"D": ("full heal", 50),
				"E": ("heineken", 100)
				}

			choice = input("-->  ").upper()
			if choice == "X":
				return  # Exit buy menu

			if choice in items:
				item, cost = items[choice]
				if item not in Loot_Bag:
					if bag_check() >= max_Space:
					say("You have no more space in your bag", 1)
					continue
				else:
					bells-=cost
					Loot_Bag[item]=1
					say(f"You received... a {item}?")

				while True:
					try:
						bulk = int(input("How many will you buy?\n"))
						if bulk == 0:
							say("You decided to not buy the item", 1)
							return
						if bag_check() + bulk > max_Space:
							rem_spaces = max_Space - bag_check()
							say(f"You only have {rem_spaces} spaces left in your bag", 1)
						else:
							break
					except ValueError:
						say("Invalid input! Enter a number.", 1)

				total_price = cost * bulk
				if bells >= total_price:
					bells -= total_price
					if item in Consumable_info:
						if item in Bag:
							Bag[item]["amount"] += bulk
						else:
							if item =="full heal":
								Bag[item]={"type": Consumable_info[item]["type"], "amount": bulk}
							else:
									Bag[item]={"type":Consumable_info[item]["type"], "amount": bulk, "effect": Consumable_info[item]["restoration"]}
					else:
						if item in Loot_Bag:
							say(f"Tom Nook: I'm afraid I have no more {item} in stock", 1)
						else:
							Loot_Bag[item] = 1
					say(f"You received {bulk} {item}(s)!", 1)
				else:
					say("Not enough bells!", 1)
			else:
				say("Invalid input, try again.", 1)

	def sell():
		global bells
		while True:
			say(f"\nbells: {bells}", 1)
			say("--------SHOP--------", 1)
			for item in Bag:
				print(f"{item} ({Bag[item]['amount']}): {Consumable_info[item]['sell price']} bells")
			print("[X] exit")
			sell_choice = input("--> ").lower()
			if sell_choice == "x":
				break
			else:
				if sell_choice in Bag:
					while True:
						try:
							bulk = int(input("How many will you sell?\n"))
							if bulk > Bag[sell_choice]["amount"]:
								say(f"You only have {Bag[sell_choice]['amount']} {sell_choice}(s)", 1)
							else:
								break
						except ValueError:
							say("Invalid input! Enter a number.", 1)
						say(f"sold {bulk} {sell_choice}", 1)
						bells += Consumable_info[sell_choice]["sell price"]* bulk
						Bag[sell_choice]["amount"] -= bulk
						if Bag[sell_choice]["amount"] == 0:
							del Bag[sell_choice]
					else:
						say("you don't have that item", 1)

	while True:
		say("\nTom Nook: Welcome to my shop!", 1)
		print("[A] buy items")
		print("[B] sell items")
		print("[X] leave shop")
		dialogue_choice = input("-->  ").upper()
		if dialogue_choice == "A":
			buy()
		elif dialogue_choice == "B":
			sell()
		elif dialogue_choice == "X":
			say("you walk away", 1)
			break
		else:
			say("invalid input, try again", 1)

def bag_check():
	return sum(item["amount"] for item in Bag.values())

def open_bag():
	say("HP items", 1)
	for item, data in Bag.items():
		if data["type"] == "HP":
			if item == "full heal":
				print(f"{item}(s): {data['amount']}")
				print(f"Heals {Player_Stats['HP']} {data['type']}")
			else:
				print(f"{item}(s): {data['amount']}")
				print(f"Restores {data['effect']}")
	
	say("\nEnergy items", 1)
	for item, data in Bag.items():
		if data["type"] == "Energy":
			print(f"{item}(s): {data['amount']}")
			print(f"Restores {data['effect']} {data['type']}")

def fighting():
	global option, item_sel, enemy, tutorial
	
	if tutorial:
		enemy = "shadow"
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

		say(f"A shadowy figure appears... ", 1)
	
		# **Basic Attack Tutorial**
		say("Hint: Try attacking! (Press 'A')", 1)
		while True:
			option = fight_options()
			if option == "A":
				say(f"You strike the {enemy}!", 1)
				Engy -= 4  # Energy deduction
				F_HP -= DMG
				break
			else:
				say("Hint: You should attack.", 1)
	
		# **Enemy Counterattack**
		say(f"The {enemy} strikes back!", 1)
		HP -= E_dmg
		say("Hint: After every round, you restore 2 energy.", 1)
		Engy = min(Engy + 2, max_Engy)
	
		# **Dodge Tutorial**
		say("\nHint: The enemy is attacking, try dodging! (Press 'C')", 1)
		while True:
			option = fight_options()
			if option == "C":
				say(f"The {enemy} attacks...", 1)
				say("But you dodged it!", 1)
				Engy = min(Engy + 2, max_Engy)
				break
			else:
				say("Hint: You should dodge.", 1)
	
		# **Healing Tutorial**
		say("Hint: You're injured, try healing using an item (Press 'B')", 1)
		while True:
			option = fight_options()
			if option == "B":
				say("You open your bag:", 1)
				open_bag()
				while True:
					item_sel = input("Use -->  ").lower()
					if item_sel in Bag and Bag[item_sel]["amount"] > 0:
						if Bag[item_sel]["type"] == "HP":
							HP += int(Bag[item_sel]["effect"])  # Ensure healing is an integer
							HP = min(HP, max_HP)  # Prevent overhealing
							say(f"Used {item_sel}.", 1)
							Bag[item_sel]["amount"] -= 1
							if Bag[item_sel]["amount"] == 0:
								del Bag[item_sel]  # Remove item if used up
							break
						else:
							say("Hint: That item isn't for healing.", 1)
					else:
						say("Hint: Type the exact item name.", 1)
				break
			else:
				say("Hint: You should heal.", 1)
	
		# **Finishing the Fight**
		say("Hint: Finish off the enemy!", 1)
		Engy = min(Engy + 2, max_Engy)
	
		while F_HP > 0:
			option = fight_options()
	
			if option == "A":
				Engy -= 4
				say(f"You strike the {enemy}!", 1)
				Engy = min(Engy + 2, max_Engy)
				F_HP -= DMG
				if F_HP <= 0:
					break
				if random.randint(1, 2) == 1:
					say(f"The {enemy} heals itself!", 1)
					F_HP = min(F_HP + E_heal[enemy], max_EHP)
				else:
					say(f"the {enemy} does nothing", 1)
			elif option == "B":
				say("Hint: There are no more tutorial items, try another option.", 1)
	
			elif option == "C":
				say(f"You hesitate...", 1)
				Engy = min(Engy + 2, max_Engy)
				if random.randint(1, 2) == 1:
					say(f"The {enemy} heals itself!", 1)
					F_HP = min(F_HP + E_heal[enemy], max_EHP)
				else:
					say("you both do nothing", 1)
	
			elif option == "D":
				say("Hint: You cannot run in the tutorial.", 1)
	
		say(f"\nYou defeated the {enemy}!", 1)
		say(f"The {enemy} dropped a sword!", 1)
		say("Obtained sword! \n+5 DMG!", 1)
		Player_Stats["DMG"] += 5
		tutorial = False
		wait(3)
		return
	
	def drop_loot():
		global enemy
		if enemy == "fish":
			final_cutscene()

		def cash_drop():
			global bells
			if random.randint(1, 2) == 1:
				M_drop = random.randint(1, 25)
				say(f"the {enemy} also dropped {M_drop} bells!", 1)
				bells += M_drop
		
		global max_Space
		loot_roll = random.randint(1, 6)
		if loot_roll <= 5:
			chance = "drop"
		else:
			chance = "no drop"
	
		if chance == "drop":
			item = random.choice(Loot[enemy])
			if item in Consumable_info:
				if bag_check() >= max_Space:
					say(f"you leave the {item} because you have no space", 1)
					cash_drop()
					return
				if item in Bag:
					Bag[item]["amount"] += 1
				else:
					if item == "full heal":
						Bag[item] = {"type": Consumable_info[item]["type"], "amount": 1}
					else:
						Bag[item] = {"type": Consumable_info[item]["type"], "amount": 1, "effect": Consumable_info[item]["restoration"]}
			else:
				if item in Loot_Bag:
					Loot_Bag[item] += 1
				else:
					Loot_Bag[item] = 1
			say(f"You received a {item}!", 1)
			cash_drop()
			
	def fight_options():
		nonlocal HP, Engy, F_HP
		global option
		option = "null"
		print("\nYour HP:", HP, "\n"  
			+ "Your Energy:", Engy, "\n"  
			+ "Enemy HP:", F_HP, "\n"  
			+ "----------------------------\n"  
			+ "[A] Strike: 4 energy\n"  
			+ "[B] Use item\n"  
			+ "[C] Dodge\n"  
			+ "[D] Run")
		return input("--> ").upper()
		
	def boss_ai():
		global option
		nonlocal Blk_chance, F_HP, HP, Engy, max_Engy, DMG, max_HP, max_EHP
		B_atk1 = E_str[enemy][0]
		B_atk2 = E_str[enemy][1]
		B_atk3 = E_str[enemy][2]
		enemy_act = random.randint(1, 5)
		if enemy_act == 1:
			Engy = min(Engy + 2, max_Engy)
			say(f"The {enemy} slaps you!", 1)
			if option == "C":
				say("But you dodged it!", 1)
				return            
			block = random.randint(1, Blk_chance)
			if block == 1:
				say("But you blocked it!", 1)
			else:
				say("You were hit!", 1)
				HP -= B_atk1   
		elif enemy_act == 2:
			say(f"The {enemy} spawns a tsunami!", 1)
			Engy = min(Engy + 2, max_Engy)
			if option == "C":
				say("But you dodged it!", 1)
				return            
			block = random.randint(1, Blk_chance)
			if block == 1:
				say("But you blocked it!", 1)
			else:
				say("You were hit!", 1)
				HP -= B_atk2
		elif enemy_act == 3:
			say(f"The {enemy} bites you!", 1)
			Engy = min(Engy + 2, max_Engy)
			if option == "C":
				say("But you dodged it!", 1)
				return            
			block = random.randint(1, Blk_chance)
			if block == 1:
				say("But you blocked it!", 1)
			else:
				say("You were hit!", 1)
				HP -= B_atk3
		elif enemy_act == 2:
			Engy = min(Engy + 2, max_Engy)
			if F_HP < max_EHP:
				say(f"The {enemy} heals!", 1)
				F_HP = min(F_HP + E_heal[enemy], max_EHP)
		else:
			say(f"The {enemy} flops around.", 1)  
			
	def enemy_ai():
		global option
		nonlocal Blk_chance, F_HP, HP, Engy, max_Engy, DMG, max_HP, max_EHP, E_dmg
		if enemy == "fish":
			boss_ai()
			return
		enemy_act = random.randint(1, 5)
		if enemy_act <= 3:
			Engy = min(Engy + 2, max_Engy)

	def enemy_ai():
		global option
		nonlocal Blk_chance, F_HP, HP, Engy, max_Engy, DMG, max_HP, max_EHP, E_dmg
	
		if enemy == "fish":
			boss_ai()
			return
	
		enemy_act = random.randint(1, 5)
		if enemy_act <= 3:
			Engy = min(Engy + 2, max_Engy)
			say(f"The {enemy} attacks!", 1)
			if option == "C":
				say("But you dodged it!", 1)
				return			
			block = random.randint(1, Blk_chance)
			if block == 1:
				say("But you blocked it!", 1)
			else:
				say("You were hit!", 1)
				HP -= E_dmg  
		elif enemy_act == 4:
			Engy = min(Engy + 2, max_Engy)
			if F_HP < max_EHP:
				say(f"The {enemy} heals!", 1)
				F_HP = min(F_HP + E_heal[enemy], max_EHP)
			else:
				say(f"The {enemy} stands still.", 1)  
		else:
			Engy = min(Engy + 2, max_Engy)
			if option == "A":
				enemy_block = random.randint(1, 25)
				if enemy_block == 1:
					say(f"The {enemy} blocked your attack!", 1)
					F_HP += DMG
				else:
					say(f"The {enemy} tried dodging your attack and failed.", 1)
			else:
				say(f"The {enemy} does nothing.", 1)
	
	if tutorial:
		tutorial_fight()
		return
	
	say(f"The {enemy} surprises you!",1)
	
	while True:
		if HP < 1:
			lose_cutscene()
		option = fight_options()
	
		if option == "A":
			if Engy < 4:
				say("You don't have enough energy!", 1)
				fight_options()
			else:
				say(f"You strike the {enemy}!", 1)
				Engy -= 4
				F_HP -= DMG
				if F_HP <= 0:
					say(f"You defeated the {enemy}!", 1)
					Player_Stats["enemies killed"] += 1
					drop_loot()
					return
				enemy_ai()
	
		elif option == "B":
			while True:
				if len(Bag) <= 0:
					say("You have nothing in your bag!", 1)
					break
				elif HP == max_HP and Engy == max_Engy:
					say("You don't need to use anything right now!", 1)
					break
				else:
					say("You open your bag.", 1)
					open_bag()
					say("[X] Close bag", 1)
					item_sel = input("--> ").lower()
					wait(1)
					if item_sel == "x":
						break
	
					if item_sel in Bag:
						if Bag[item_sel]["type"] == "HP":
							if HP == max_HP:
								say("You don't need to heal.", 1)
							else:
								if item_sel == "full heal":
									HP = max_HP
								else:
									HP += int(Bag[item_sel]["effect"])
									HP = min(HP, max_HP)
	
						elif Bag[item_sel]["type"] == "Energy":
							if Engy == max_Engy:
								say("You don't need energy.", 1)
							else:
								Engy += int(Bag[item_sel]["effect"])
								Engy = min(Engy, max_Engy)
	
						say(f"Used {item_sel}.", 1)
						Bag[item_sel]["amount"] -= 1
	
						if Bag[item_sel]["amount"] == 0:
							del Bag[item_sel]
						break
	
		elif option == "C":
			say("You prepare to block...", 1)
			Engy = min(Engy + 2, max_Engy)
			enemy_ai()
	
		elif option == "D":
			say("You try to run away...", 1)
			wait(1.5)
			if random.randint(1, 5) == 1:
				say("You ran away!", 1)
				return
			else:
				say("But you failed!", 1)
			enemy_ai()
		else:
			say("Invalid option.", 1)
	
def gameplay():
	global location

	def player_options():
		while True:
			if location == "base":
				say("\nWhat will you do?", 1)
				print("----------------------------\n"
					+ "[A] Talk to weaponsmith\n"
					+ "[B] Talk to armorsmith\n"
					+ "[C] Talk to Tom Nook\n"
					+ "[D] Talk to your crush\n"
					+ "[E] Talk to Gandalf\n"
					+ "[F] Check loot\n"
					+ "[G] Go somewhere else\n"
					+ "[X] Open menu")
			else:
				say("\nWhat will you do?", 1)
				print("----------------------------\n"
					+ f"[A] Explore {location}\n"
					+ "[B] Go somewhere else\n"
					+ "[C] Open bag\n"
					+ "[D] Check loot\n"
					+ "[X] Open menu")

			option = input("--> ").upper()
			if option in ["A", "B", "C", "D", "E", "F", "G", "X"]:
				return option
			say("Invalid input! Please enter a valid option.", 1)

	def travel_menu():
		while True:
			say("\nWhere will you go?", 1)
			print("----------------------------\n"
				+ "[A] Supermarket\n"
				+ "[B] Scrapyard\n"
				+ "[C] Farm\n"
				+ "[D] Base\n"
				+ "[X] Do something else")

			travel_option = input("--> ").upper()
			wait(1)
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
				say("You are already here!", 1)
			else:
				say(f"You go to the {location}", 1)
			break

	while True:
		say(f"\nYou are at the {location}", 1)
		option = player_options()

		if location == "base":
			if option == "A":
				if quest_status["weaponsmith"] == "complete":
					say("\nWeaponsmith: You know, the smell of metal makes me WAKE UP every morning", 1)
					say("...", 1)
					say("A sense of uncertainty washes over you", 1)
				else:
					say("\nWeaponsmith: I can upgrade your sword for 5 scrap", 1)
					while True:
						print("[A] 'I have 5 scrap!'\n"  
							+ "[B] 'Where do I find scrap?'\n"  
							+ "[C] 'Nevermind'")
						dialogue_choice = input("--> ").upper()
						if dialogue_choice == "A":
							if "scrap" not in Loot_Bag or Loot_Bag["scrap"] <= 5:
								say("You don't have enough scrap!", 1)
							else:
								say("Weaponsmith: Here's your new sword, pal!\n+5 DMG", 1)
								Player_Stats["DMG"] += 5
								Loot_Bag["scrap"] -= 5
								if Loot_Bag["scrap"] < 1:
									del Loot_Bag["scrap"]
								quest_status["weaponsmith"] = "complete"
							break
						elif dialogue_choice == "B":
							say("Scrap can be found in the scrapyard or as a random drop from hobos.", 1)
							break
						elif dialogue_choice == "C":
							say("You walk away.", 1)
							break
						say("Invalid input! Please enter A, B, or C.", 1)

			elif option == "B":
				if quest_status["armorsmith"] == "complete":
					say("\nArmorsmith: My dad used shoulder plates to WAKE me UP once", 1)
					say("...", 1)
					say("You feel as if you are forgetting something", 1)
				else:
					say("\nArmorsmith: I can make you some armor for 3 scrap and 5 leather", 1)
					while True:
						print("[A] 'I have 3 scrap and 5 leather!'\n"  
							+ "[B] 'Where do I find scrap and leather?'\n"  
							+ "[C] 'Nevermind'")
						dialogue_choice = input("--> ").upper()
						if dialogue_choice == "A":
							if "scrap" not in Loot_Bag or "leather" not in Loot_Bag:
								say("You don't have enough materials!", 1)
								break
							else:
								if Loot_Bag["scrap"] < 3 or Loot_Bag["leather"] < 5:
									say("You don't have enough materials!", 1)
									break
								else:
									say("Armorsmith: Here's your new armor, pal!\n+5 Armor\n+25 HP", 1)
									Player_Stats["Armor"] += 5
									Player_Stats["HP"] += 25
									Loot_Bag["scrap"] -= 3
									if Loot_Bag["scrap"] < 1:
										del Loot_Bag["scrap"]
									Loot_Bag["leather"] -= 5
									if Loot_Bag["leather"] < 1:
										del Loot_Bag["leather"]
									quest_status["armorsmith"] = "complete"
								break
						elif dialogue_choice == "B":
							say("Scrap can be found at the scrapyard, while leather can be found at the farm. Hobos have a chance of dropping either item though.", 1)
							break
						elif dialogue_choice == "C":
							say("You walk away.", 1)
							break
						say("Invalid input! Please enter A, B, or C.", 1)

			elif option == "C":
				while True:
					print("\nTom Nook: Feel free to buy or sell anything at my shop!\n"
						+ "[A] Open shop\n"
						+ "[B] Walk away")
					dialogue_choice = input("--> ").upper()
					if dialogue_choice == "A":
						shop()
						break
					elif dialogue_choice == "B":
						say("You walk away.", 1)
						break
					say("Invalid input! Please enter A or B.", 1)

			elif option == "D":
				if quest_status["crush"] == "complete":
					say("\nCrush: These chocolates give me a reason to WAKE UP every morning", 1)
					say("...", 1)
					say("This can't be real. Why are they here?", 1)
				else:
					while True:
						say("\nCrush: Do you have chocolates for me?", 1)
						print("[A] 'Sure!'"
							+ "[B] 'Where do I find chocolates?'"
							+ "[C] 'Nah'", 1)
						dialogue_choice = input("--> ").upper()
						if dialogue_choice == "A":
							if "chocolates" not in Loot_Bag:
								say("Crush: You liar!", 1)
								say("She slaps you\n-5 HP", 1)
								Player_Stats["HP"] -= 5
							else:
								del Loot_Bag["chocolates"]
								Player_Stats["HP"] += 25
								say("Crush: Thank you so much!\n+25 HP!", 1)
								quest_status["crush"] = "complete"
							break
						elif dialogue_choice == "B":
							say("Oh, you can find them at the supermarket.", 1)
							break
						elif dialogue_choice == "C":
							say("You walk away.", 1)
							break
						say("Invalid input! Please enter A, B, or C.", 1)
			elif option.upper() == "E":  # Talking to Gandalf
				if quest_status["gandalf"] == "1st":
					if quest_status["weaponsmith"] == "complete":
						say("\nGandalf: Ah, I see you have strengthened your sword. Your first task is to find a map at the farm.", 1)
						while True:
							print("[A] 'I'll find it!'\n"  
								+ "[B] 'Maybe later.'")
							dialogue_choice = input("--> ").upper()
							if dialogue_choice == "A":
								say("Gandalf: Good! Return to me once you have the map.", 1)
								quest_status["gandalf"] = "map quest"
								break
							elif dialogue_choice == "B":
								say("Gandalf: Very well, return when you are ready.", 1)
								break
							else:
								say("Invalid choice! Please select A or B.", 1)
					else:
						say("\nGandalf: You are not ready. Strengthen your sword first.", 1)
			
				elif quest_status["gandalf"] == "map quest":
					if Loot_Bag["map"] > 0:
						say("\nGandalf: Ah, you found the map! But you are still too vulnerable. You must upgrade your armor.", 1)
						del Loot_Bag["map"]
						quest_status["gandalf"] = "armor requirement"
					else:
						say("\nGandalf: You haven't found the map yet. Seek it at the farm.", 1)
			
				elif quest_status["gandalf"] == "armor requirement":
					if quest_status["armorsmith"] == "complete":
						say("\nGandalf: You are ready for this next task, but are you ready for the foes you will fight within?", 1)
						while True:
							print("[A] 'I am ready'\n"  
								+ "[B] 'I'll do this later'")
							dialogue_choice = input("--> ").upper()
							if dialogue_choice == "A":
								say("Gandalf: Very well, I shall bring you there.", 1)
								say("Gandalf brings you to the cave.", 1)
								say("Gandalf: Return when you have the artifact.", 1)
								quest_status["gandalf"] = "artifact quest"
								location = "cave"
								break
							elif dialogue_choice == "B":
								say("Gandalf: Return when you are ready.", 1)
								break
							else:
								say("Invalid choice! Please select A or B.", 1)
					else:
						say("\nGandalf: You need stronger armor before continuing. Speak to the armorsmith.", 1)
			
				elif quest_status["gandalf"] == "artifact quest":
					if Loot_Bag["artifact"] > 0:
						say("\nGandalf: You have returned with the artifact. But you must be even stronger for the final challenge.", 1)
						del Loot_Bag["artifact"]
						quest_status["gandalf"] = "health requirement"
					else:
						say("\nGandalf: You haven't found the artifact yet. Seek it in the cave.", 1)
			
				elif quest_status["gandalf"] == "health requirement":
					if quest_status["crush"] == "complete":
						say("Gandalf: You have gained the strength you need, but are you prepared to come with me to fix this?", 1)
						while True:
							print("[A] 'Let's do this!'\n"  
								+ "[B] 'Let me prepare first'")
							dialogue_choice = input("--> ").upper()
							if dialogue_choice == "A":
								say("Gandalf: Very well, let us set off to the rift zone to patch the rift and fix this mess.", 1)
								say("You and the whole group journey to the rift zone.", 1)
								boss_cutscene()
								break
							elif dialogue_choice == "B":
								say("Gandalf: Return when you are ready.", 1)
								break
							else:
								say("Invalid choice! Please select A or B.", 1)
					else:
						say("\nGandalf: You are not yet strong enough. Perhaps there is someone who can make you stronger?", 1)

			elif option == "F":
				for item, amount in Loot_Bag.items():
					say(f"{item}: {amount}", 1)
				say(f"bells: {bells}", 1)
			elif option == "G":
				travel_menu()

			elif option == "X":
				menu()

		else:
			if option == "A":
				say(f"You explore the {location}.", 1)
				if location == "rift zone":
					boss_cutscene()
				else:
					event = random.randint(1, 6)
					if event <= 4:
						fighting()
					elif event == 5:
						if random.randint(1, 3) == 1:
							rand_encounters()
					if location == "supermarket" and quest_status["crush"] == "incomplete":
						if random.randint(1, 15) == 1 and "chocolates" not in Loot_Bag:
							say("You found chocolates!", 1)
							Loot_Bag["chocolates"] = 1
					if location == "farm" and quest_status["gandalf"] == "map quest":
						if random.randint(1, 20) == 1 and "map" not in Loot_Bag:
							say("You found a map!", 1)
							Loot_Bag["map"] = 1

			elif option == "B":
				if location in ["cave", "rift zone"] and "artifact" not in Bag:
					say("You can't leave until you get an artifact", 1)
				else:
					travel_menu()
			elif option == "C":
				open_bag()
			elif option == "D":
				for item, amount in Loot_Bag.items():
					say(f"{item}: {amount}", 1)
				say(f"bells: {bells}", 1)
			elif option == "X":
				menu()

def game():
	title_screen()
	gameplay()


game()
