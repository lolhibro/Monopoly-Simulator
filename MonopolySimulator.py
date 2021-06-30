import random

class Property:
    def __init__(self, rents, price, building_cost, position, color):
        self.rents = rents
        self.price = price
        self.building_cost = building_cost
        self.position = position
        self.num_houses = 0
        self.owner = -1
        self.mortgaged = False
        self.color = color

class Railroad:
    def __init__(self, position):
        self.rents = [25, 50, 100, 200]
        self.price = 200
        self.position = position
        self.owner = -1
        self.num_owned_by_owner = -1
        self.mortgaged = False

class Utility:
    def __init__(self, position):
        self.price = 150
        self.position = position
        self.owner = -1
        self.num_owned_by_owner = -1
        self.mortgaged = False

class Player:
    def __init__(self, number):
        self.number = number
        self.pos = 0
        self.money = 1500
        self.props = set()
        self.in_jail = False
        self.jail_count = 0
        self.jail_free = False
        self.railroads = set()
        self.utilities = set()
        self.defeated = False

while True:
    print("Would you like to play, or simulate a game?")
    playsim = input("{press 's' and enter for simulate and anything else for play} ")
    print("")
    num_players = None

    if playsim == 's':
        print("How many players do you want to simulate? (Honestly more than 8 is really no fun).")
        playerchar = input("{enter a number between 2-8. Invalid entry gets the default 4 players} ")
        print("")

        if len(playerchar) == 1 and int(playerchar) >= 2 and int(playerchar) <= 8:
            num_players = int(playerchar)
        else:
            num_players = 4
        print("{} bot players will be randomly assigned properties and they'll be furnished with a random number of houses/hotel each.".format(num_players))
        print("Continue?")
        response = input("{enter 'y' if yes and anything else if no} ")
        print("")

        if response != 'y':
            continue
    else:
        print("How many players want to play? (Honestly more than 8 is really no fun).")
        playerchar = input("{enter a number between 2-8. Invalid entry gets the default 4 players} ")
        print("")

        if len(playerchar) == 1 and int(playerchar) >= 2 and int(playerchar) <= 8:
            num_players = int(playerchar)
        else:
            num_players = 4

    print("Start game with {} players?".format(num_players))
    start = input("{'y' for yes! Anything else for no} ")
    print("")

    if start == 'y':
        break

board = ['Go',
        'Mediterranean avenue',
        'Community Chest',
        'Baltic avenue',
        'Income Tax',
        'Reading railroad',
        'Oriental avenue',
        'Chance',
        'Vermont avenue',
        'Connecticut avenue',
        'Jail/Just Visiting',
        'St. charles place',
        'Electric company',
        'States avenue',
        'Virginia avenue',
        'Pennsylvania railroad',
        'St. james place',
        'Community Chest',
        'Tennessee avenue',
        'New york avenue',
        'Free Parking',
        'Kentucky avenue',
        'Chance',
        'Indiana avenue',
        'Illinois avenue',
        'B. & o. railroad',
        'Atlantic avenue',
        'Ventnor avenue',
        'Water works',
        'Marvin gardens',
        'Go to Jail',
        'Pacific avenue',
        'North carolina avenue',
        'Community Chest',
        'Pennsylvania avenue',
        'Short line',
        'Chance',
        'Park place',
        'Luxury Tax',
        'Boardwalk']

properties = {'Mediterranean avenue':Property([2,10,30,90,160,250], 60, 50, 1, 1),
        'Baltic avenue':Property([4,20,60,180,320,450], 60, 50, 3, 1),
        'Oriental avenue':Property([6,30,90,270,400,550], 100, 50, 6, 2),
        'Vermont avenue':Property([6,30,90,270,400,550], 100, 50, 8, 2),
        'Connecticut avenue':Property([8,40,100,300,450,600], 120, 50, 9, 2),
        'St. charles place':Property([10,50,150,450,625,750], 140, 100,11, 3),
        'States avenue':Property([10,50,150,450,625,750], 140, 100,13, 3),
        'Virginia avenue':Property([12,60,180,500,700,900], 160, 100,14, 3),
        'St. james place':Property([14,70,200,550,750,950], 180, 100,16, 4),
        'Tennessee avenue':Property([14,70,200,550,750,950], 180, 100,18, 4),
        'New york avenue':Property([16,80,220,600,800,1000], 200, 100,19,4),
        'Kentucky avenue':Property([18,90,250,700,875,1050], 220, 150,21,5),
        'Indiana avenue':Property([18,90,250,700,875,1050], 220, 150,23,5),
        'Illinois avenue':Property([20,100,300,750,925,1100], 240, 150, 24,5),
        'Atlantic avenue':Property([22,110,330,800,975,1150], 260, 150,26,6),
        'Ventnor avenue':Property([22,110,330,800,975,1150], 260, 150,27,6),
        'Marvin gardens':Property([24,120,360,850,1025,1200], 280, 150,29,6),
        'Pacific avenue':Property([26,130,390,900,1100,1275], 300, 200,31,7),
        'North carolina avenue':Property([26,130,390,900,1100,1275], 300, 200,32,7),
        'Pennsylvania avenue':Property([28,150,450,1000,1200,1400], 320, 200,34,7),
        'Park place':Property([35,175,500,1100,1300,1500], 350, 200,37,8),
        'Boardwalk':Property([50,200,600,1400,1700,200], 400, 200,39,8)}

railroads = {'Reading railroad':Railroad(5),
            'Pennsylvania railroad':Railroad(15),
            'B. & o. railroad':Railroad(25),
            'Short line':Railroad(35)}

utilities = {'Electric company':Utility(12),
            'Water works':Utility(28)}

houses_num = 32
hotels_num = 12

players_dict = {}
curr_players = []

for i in range(num_players):
    new_player = Player(i+1)
    curr_players.append(new_player)
    players_dict[i+1] = new_player


# Change this
if playsim == 's':
    for prop in properties:
        player = random.randint(1, num_players)
        curr_players[player-1].props.add(prop)
        properties[prop].owner = player

    for railroad in railroads:
        player = random.randint(1, num_players)
        curr_players[player-1].railroads.add(railroad)
        railroads[railroad].owner = player

        for railroad_name in curr_players[player-1].railroads:
            railroads[railroad_name].num_owned_by_owner += 1

    for utility in utilities:
        player = random.randint(1, num_players)
        curr_players[player-1].utilities.add(utility)
        utilities[utility].owner = player

        for utility_name in curr_players[player-1].utilities:
            utilities[utility_name].num_owned_by_owner += 1

    props_to_deck = list(properties.keys())

    while hotels_num > 0:
        i = random.randrange(len(props_to_deck))
        properties[props_to_deck[i]].num_houses += 5
        props_to_deck.pop(i)
        hotels_num -= 1

    while houses_num > 0:
        i = random.randrange(len(props_to_deck))
        properties[props_to_deck[i]].num_houses += 1

        if properties[props_to_deck[i]].num_houses == 4:
            props_to_deck.pop(i)

        houses_num -= 1
    print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-")
    for other_player in curr_players:
        print("\nPlayer {}".format(other_player.number))
        print("\tAt {}".format(board[other_player.pos]))
        print("\tMoney: ${}".format(other_player.money))
        if other_player.in_jail:
            print("\tJailed")
        if other_player.jail_free:
            print("\tGet Out of Jail Free Card")
        print("\nProperties:")
        for prop in other_player.props:
            print(prop)
            print("\tColor: {}".format(properties[prop].color))
            if properties[prop].num_houses != 0:
                if properties[prop].num_houses == 1:
                    print("\t1 house")
                elif properties[prop].num_houses < 5:
                    print("\t{} houses".format(properties[prop].num_houses))
                else:
                    print("\tHotel")
            if properties[prop].mortgaged:
                print("\tMortgaged")
        print("\nRailroads:")
        for railroad in other_player.railroads:
            print(railroad)
            if railroads[railroad].mortgaged:
                print("\tMortgaged")
        print("\nUtilities:")
        for utility in other_player.utilities:
            print(utility)
            if utilities[utility].mortgaged:
                print("\tMortgaged")
        print("")
    print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-\n")
# Change this

i = random.randrange(num_players)
doubles = 0

while len(curr_players) > 1:
    print("-------------------------------------")
    railroad_twice = False
    util_tenx = False
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    player = curr_players[i]
    if player.in_jail:
        print("Player {} is in jail\n".format(player.number))
        if player.jail_free:
            print("Player {} uses Get Out of Jail Free card".format(player.number))
            print("Player {} is not longer in jail\n".format(player.number))
            player.jail_free = False
            player.in_jail = False
        else:
            player.jail_count += 1
            if player.jail_count != 3 and player.money > 50:
                response = None
                if playsim == 's':
                    response = 'y'
                else:
                    print("Get bail for $50?")
                    response = input("{'y' for yes, anything else for no} ")
                    print("")

                if response == 'y':
                    print("Player {} bails out\n".format(player.number))
                    player.money -= 50
                    player.in_jail = False
                    player.jail_count = 0

    print("Player {} rolls {}, {}\n".format(player.number, die1, die2))
    if player.in_jail:
        if die1 == die2:
            print("Player {} rolls doubles and gets out of jail\n".format(player.number))
            player.in_jail = False
            player.jail_count = 0
        elif player.jail_count == 3:
            print("Player {} pays $50 and gets out of jail\n".format(player.number))
            player.money -= 50
            player.in_jail = False
            player.jail_count = 0
        else:
            print("Player {} fails to roll doubles".format(player.number))
            print("Player {} stays in jail\n".format(player.number))
            i = (i + 1) % len(curr_players)
            continue

    if die1 == die2 and doubles == 2:
        doubles = 0
        print("Player {} rolled doubles 3 times".format(player.number))
        print("Player {} goes to jail\n")
        player.pos = 10
        player.in_jail = True
        i = (i + 1) % len(curr_players)
        continue

    player.pos += die1 + die2

    if player.pos >= 40:
        print("Player {} passes Go".format(player.number))
        print("Player {} collects $200 from the bank\n".format(player.number))
        player.pos -= 40
        player.money += 200

    if board[player.pos] == 'Chance':
        print("Player {} lands on Chance\n".format(player.number))
        chance = random.randrange(16)

        if chance == 0:
            print("Chance: Advance to Boardwalk")
            print("Player {} advances to Boardwalk\n".format(player.number))
            player.pos = 39
        elif chance == 1:
            print("Chance: Advance to Go (Collect $200)")
            print("Player {} advances to Go".format(player.number))
            print("Player {} collects $200 from the bank\n".format(player.number))
            player.pos = 0
            player.money += 200
        elif chance == 2:
            print("Chance: Advance to Illinois Avenue. If you pass Go, collect $200")
            print("Player {} advances to Illinois Avenue\n".format(player.number))

            if player.pos > 24:
                print("Player {} passes Go".format(player.number))
                print("Player {} collects $200 from the bank\n".format(player.number))
                player.money += 200
            player.pos = 24
        elif chance == 3:
            print("Chance: Advance to St. Charles Place. If you pass Go, collect $200")
            print("Player {} advances to St. Charles Place\n".format(player.number))

            if player.pos > 11:
                print("Player {} passes Go".format(player.number))
                print("Player {} collects $200 from the bank\n".format(player.number))
                player.money += 200
            player.pos = 11
        elif chance == 4 or chance == 5:
            print("Chance: Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay owner twice the rental to which they are otherwise entitled")
            railroad_twice = True

            if player.pos < 5:
                print("Player {} advances to Reading Railroad\n".format(player.number))
                player.pos = 5
            elif player.pos < 15:
                print("Player {} advances to Pennsylvania Railroad\n".format(player.number))
                player.pos = 15
            elif player.pos < 25:
                print("Player {} advances to B. & O. Railroad\n".format(player.number))
                player.pos = 25
            elif player.pos < 35:
                print("Player {} advances to Short Line\n".format(player.number))
                player.pos = 35
            else:
                print("Player {} advances to Reading Railroad".format(player.number))
                print("Player {} passes Go".format(player.number))
                print("Player {} collects $200 from the bank\n".format(player.number))
                player.money += 200
                player.pos = 5
        elif chance == 6:
            print("Chance: Advance to the nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown")
            util_tenx = True

            if player.pos < 12:
                print("Player {} advances to Electric Company\n".format(player.number))
                player.pos = 12
            elif player.pos < 28:
                print("Player {} advances to Water Works\n".format(player.number))
                player.pos = 28
            else:
                print("Player {} advances to Electric Company".format(player.number))
                print("Player {} passes Go".format(player.number))
                print("Player {} collects $200 from the bank\n".format(player.number))
                player.money += 200
                player.pos = 12
        elif chance == 7:
            print("Chance: Bank pays you dividend of $50")
            print("Player {} collects $50 from the bank\n".format(player.number))
            player.money += 50
        elif chance == 8:
            print("Chance: Get Out of Jail Free")
            print("Player {} gets a Get Out of Jail Free card\n".format(player.number))
            player.jail_free = True
        elif chance == 9:
            print("Chance: Go back 3 spaces")
            print("Player {} backtracks 3 spaces\n".format(player.number))
            player.pos -= 3
        elif chance == 10:
            print("Chance: Go to Jail. Go directly to Jail, do not pass Go, do not collect $200")
            print("Player {} goes to jail\n".format(player.number))
            player.in_jail = True
            player.pos = 10
            i = (i + 1) % len(curr_players)
            doubles = 0
            continue
        elif chance == 11:
            print("Chance: Make general repairs on all your property. For each house pay $25. For each hotel pay $100")
            total = 0

            for prop in player.props:
                if properties[prop].num_houses < 5:
                    total += 25*properties[prop].num_houses
                else:
                    total += 100

            print("Player {} pays ${} to the bank\n".format(player.number, total))
            player.money -= total
        elif chance == 12:
            print("Chance: Speeding fine $15")
            print("Player {} pays $15 to the bank\n".format(player.number))
            player.money -= 15
        elif chance == 13:
            print("Chance: Take a trip to Reading Railroad. If you pass Go, collect $200")
            print("Player {} advances to Reading Railroad\n".format(player.number))

            if player.pos > 5:
                print("Player {} passes Go".format(player.number))
                print("Player {} collects $200 from the bank\n".format(player.number))
                player.money += 200

            player.pos = 5
        elif chance == 14:
            print("Chance: You have been elected Chairman of the Board. Pay each player $50")
            print("Player {0} pays $50 to each player. Player {0} pays ${1} in total\n".format(player.number, 50*(len(curr_players)-1)))
            player.money -= 50*len(curr_players)

            for other_player in curr_players:
                other_player.money += 50
        else:
            print("Chance: Your building loan matures. Collect $150")
            print("Player {} collects $150 from the bank\n".format(player.number))
            player.money += 150

    if board[player.pos] == 'Community Chest':
        print("Player {} lands on Community Chest".format(player.number))
        comchest = random.randrange(16)

        if comchest == 0:
            print("Community Chest: Advance to Go (Collect $200)")
            print("Player {} advances to Go".format(player.number))
            print("Player {} collects $200 from the bank\n".format(player.number))
            player.pos = 0
            player.money += 200
        elif comchest == 1:
            print("Community Chest: Bank error in your favor. Collect $200")
            print("Player {} collects $200 from the bank\n".format(player.number))
            player.money += 200
        elif comchest == 2:
            print("Community Chest: Doctor's fee. Pay $50")
            print("Player {} pays $50 to the bank\n".format(player.number))
            player.money -= 50
        elif comchest == 3:
            print("Community Chest: From sale of stock you get $50")
            print("Player {} collects $50 from the bank\n".format(player.number))
            player.money += 50
        elif comchest == 4:
            print("Community Chest: Get Out of Jail Free")
            print("Player {} gets a Get Out of Jail Free card\n".format(player.number))
            player.jail_free = True
        elif comchest == 5:
            print("Community Chest: Go to Jail. Go directly to Jail, do not pass Go, do not collect $200")
            print("Player {} goes to Jail\n".format(player.number))
            player.in_jail = True
            player.pos = 10
            i = (i + 1) % len(curr_players)
            doubles = 0
            continue
        elif comchest == 6:
            print("Community Chest: Holiday fund matures. Receive $100")
            print("Player {} collects $100 from the bank\n".format(player.number))
            player.money += 100
        elif comchest == 7:
            print("Community Chest: Income tax refund. Collect $20")
            print("Player {} collects $20 from the bank\n".format(player.number))
            player.money += 20
        elif comchest == 8:
            print("Community Chest: It is your birthday. Collect $10 from every player")
            print("Player {0} collects $10 from every player. Player {0} collects ${1} in total\n".format(player.number, 10*(len(curr_players)-1)))
            player.money += 10*len(curr_players)

            for other_player in curr_players:
                other_player.money -= 10
        elif comchest == 9:
            print("Community Chest: Life insurance matures. Receive $100")
            print("Player {} collects $100 from the bank\n".format(player.number))
            player.money += 100
        elif comchest == 10:
            print("Community Chest: Pay hospital fees of $100")
            print("Player {} pays $100 to the bank\n".format(player.number))
            player.money -= 100
        elif comchest == 11:
            print("Community Chest: Pay school fees of $50")
            print("Player {} pays $50 to the bank\n".format(player.number))
            player.money -= 50
        elif comchest == 12:
            print("Community Chest: Receive $25 consultancy fee")
            print("Player {} collects $25 from the bank\n".format(player.number))
            player.money += 25
        elif comchest == 13:
            print("Community Chest: You are assessed from street repair. $40 per house. $115 per house")
            total = 0

            for prop in player.props:
                if properties[prop].num_houses < 5:
                    total += 40*properties[prop].num_houses
                else:
                    total += 115

            print("Player {} pays ${} to the bank\n".format(player.number, total))
            player.money -= total
        elif comchest == 14:
            print("Community Chest: You have won second place in a beauty contest. Collect $10")
            print("Player {} collects $10 from the bank\n".format(player.number))
            player.money += 10
        else:
            print("Community Chest: You inherit $100")
            print("Player {} collects $100 to the bank\n".format(player.number))
            player.money += 100

    elif board[player.pos] == 'Income Tax':
        print("Player {} lands on Income Tax".format(player.number))
        print("Player {} pays $200 to the bank\n".format(player.number))
        player.money -= 200
    elif board[player.pos] == 'Go to Jail':
        print("Player {} lands on Go to Jail".format(player.number))
        print("Player {} goes to Jail\n".format(player.number))
        player.in_jail = True
        player.pos = 10
        i = (i + 1) % len(curr_players)
        doubles = 0
        continue
    elif board[player.pos] == 'Luxury Tax':
        print("Player {} lands on Luxury Tax".format(player.number))
        print("Player {} pays $75 to the bank\n".format(player.number))
        player.money -= 75
    elif board[player.pos] in properties:
        print("Player {} lands on {}\n".format(player.number, board[player.pos]))
        prop = properties[board[player.pos]]
        if prop.owner == -1:
            if playsim == 's':
                print("Player {} buys {} for ${}\n".format(player.number, board[player.pos], prop.price))
                prop.owner = player.number
                player.props.add(board[player.pos])
                player.money -= prop.price
            else:
                print("Buy {} for ${}?".format(board[player.pos], prop.price))
                print("You currently have ${}\n".format(player.money))
                response = input("{'y' for yes, anything else for no} ")
                print("")

                if response == 'y':
                    print("Player {} bought {}\n".format(player.number, board[player.pos]))
                    prop.owner = player.number
                    player.props.add(board[player.pos])
                    player.money -= prop.price
                else:
                    print("Player {} decided not to buy {}\n".format(player.number, board[player.pos]))
        elif prop.owner == player.number:
            print("Player {} already owns {}\n".format(player.number, board[player.pos]))
        else:
            print("{} is owned by Player {}".format(board[player.pos], prop.owner))
            if prop.mortgaged:
                print("But {} is mortgaged! Player {} does not get paid\n".format(board[player.pos], prop.owner))
            else:
                cost = prop.rents[prop.num_houses]
                print("Player {} pays ${} to Player {}\n".format(player.number, cost, prop.owner))
                player.money -= cost
                players_dict[prop.owner].money += cost
    elif board[player.pos] in railroads:
        print("Player {} lands on {}\n".format(player.number, board[player.pos]))
        prop = railroads[board[player.pos]]
        if prop.owner == -1:
            if playsim == 's':
                print("Player {} buys {} for ${}\n".format(player.number, board[player.pos], prop.price))
                prop.owner = player.number
                num_owned = 0
                for railroad_name in player.railroads:
                    if not railroads[railroad_name].mortgaged:
                        num_owned += 1
                    railroads[railroad_name].num_owned_by_owner += 1
                railroads[board[player.pos]].num_owned_by_owner = num_owned
                player.railroads.add(board[player.pos])
                player.money -= prop.price
            else:
                print("Buy {} for ${}?".format(board[player.pos], prop.price))
                print("You currently have ${}\n".format(player.money))
                response = input("{'y' for yes, anything else for no} ")
                print("")

                if response == 'y':
                    print("Player {} bought {}\n".format(player.number, board[player.pos]))
                    prop.owner = player.number
                    num_owned = 0
                    for railroad_name in player.railroads:
                        if not railroads[railroad_name].mortgaged:
                            num_owned += 1
                        railroads[railroad_name].num_owned_by_owner += 1
                    railroads[board[player.pos]].num_owned_by_owner = num_owned
                    player.railroads.add(board[player.pos])
                    player.money -= prop.price
                else:
                    print("Player {} decided not to buy {}\n".format(player.number, board[player.pos]))
        elif prop.owner == player.number:
            print("Player {} already owns {}\n".format(player.number, board[player.pos]))
        else:
            print("{} is owned by Player {}".format(board[player.pos], prop.owner))
            if prop.mortgaged:
                print("But {} is mortgaged! Player {} does not get paid\n".format(board[player.pos], prop.owner))
            else:
                cost = prop.rents[prop.num_owned_by_owner]
                if railroad_twice:
                    cost *= 2
                print("Player {} pays ${} to Player {}\n".format(player.number, cost, prop.owner))
                player.money -= cost
                players_dict[prop.owner].money += cost
    elif board[player.pos] in utilities:
        print("Player {} lands on {}\n".format(player.number, board[player.pos]))
        prop = utilities[board[player.pos]]
        if prop.owner == -1:
            if playsim == 's':
                print("Player {} buys {} for ${}\n".format(player.number, board[player.pos], prop.price))
                prop.owner = player.number
                num_owned = 0
                for utility_name in player.utilities:
                    if not utilities[utility_name].mortgaged:
                        num_owned += 1
                    utilities[utility_name].num_owned_by_owner += 1
                utilities[board[player.pos]].num_owned_by_owner = num_owned
                player.utilities.add(board[player.pos])
                player.money -= prop.price
            else:
                print("Buy {} for ${}?\n".format(board[player.pos], prop.price))
                print("You currently have ${}\n".format(player.money))
                response = input("{'y' for yes, anything else for no} ")
                print("")

                if response == 'y':
                    print("Player {} bought {}\n".format(player.number, board[player.pos]))
                    prop.owner = player.number
                    num_owned = 0
                    for utility_name in player.utilities:
                        if not utilities[utility_name].mortgaged:
                            num_owned += 1
                        utilities[utility_name].num_owned_by_owner += 1
                    utilities[board[player.pos]].num_owned_by_owner = num_owned
                    player.utilities.add(board[player.pos])
                    player.money -= prop.price
                else:
                    print("Player {} decided not to buy {}\n".format(player.number, board[player.pos]))
        elif prop.owner == player.number:
            print("Player {} already owns {}\n".format(player.number, board[player.pos]))
        else:
            print("{} is owned by Player {}".format(board[player.pos], prop.owner))
            if prop.mortgaged:
                print("But {} is mortgaged! Player {} does not get paid\n".format(board[player.pos], prop.owner))
            else:
                cost = None
                if util_tenx or prop.num_owned_by_owner == 1:
                    cost = 10*(die1+die2)
                else:
                    cost = 4*(die1+die2)
                print("Player {} pays ${} to Player {}\n".format(player.number, cost, prop.owner))
                player.money -= cost
                players_dict[prop.owner].money += cost
    elif board[player.pos] != 'Chance':
        print("Player {} lands on {}\n".format(player.number, board[player.pos]))

    if playsim == 's':
        if player.money < 0:
            print("Player {} goes bankrupt!".format(player.number))
            print("Player {} loses\n".format(player.number))
            curr_players.pop(i)
            if i == len(curr_players):
                i = 0
        else:
            if die1 == die2:
                print("Player {} rolled doubles".format(player.number))
                print("Player {} rolls again\n".format(player.number))
                doubles += 1
            else:
                i = (i + 1) % len(curr_players)
                doubles = 0
    else:
        while True:
            print("Would Player {} like to do anything else?\n".format(player.number))
            if player.money < 0:
                print("ATTENTION! Your money is currently below 0. Sell or trade to get it above 0, or enter 'q' to declare bankcruptcy and quit the game.\n")
            response = input("{press 't' to trade, 'b' to buy houses, 's' to sell houses, 'v' to view all active players' status, 'm' to mortgage or reverse, 'q' to quit or declare bankcruptcy, anything else to continue} ")
            print("")
            if response == 't':
                print("Who would you like to trade with?")
                to_trade = input("{enter player number} ")
                print("")
                if ord(to_trade) < ord('1') or ord(to_trade) > ord(str(len(players_dict))):
                    print("Player {} doesn't exist".format(to_trade))
                else:
                    other_player = players_dict[int(to_trade)]
                    if other_player.defeated:
                        print("Player {} is no longer in the game".format(other_player.number))
                    else:
                        print("What will you offer?")
                        response = input("{remember to place commas between your items, to spell correctly, and to place a $ sign before any money you're offering} ")
                        print("")
                        items_to_give = [item.strip().capitalize() for item in response.split(',')]
                        fail = False
                        dollar_encountered = False
                        for item in items_to_give:
                            if item[0] == '$':
                                if dollar_encountered:
                                    print("You already added money to your trade. Balance it out")
                                elif not item[1:].isdigit():
                                    print("{} is not a number".format(item[1:]))
                                elif int(item[1:]) > player.money:
                                    print("You only have ${} left to trade".format(player.money))
                                else:
                                    dollar_encountered = True
                                    continue
                            elif item not in properties and item not in railroads and item not in utilities:
                                print("{} does not exist".format(item))
                            elif item not in player.props and item not in player.railroads and item not in player.utilities:
                                print("You do not own {}".format(item))
                            else:
                                continue
                            fail = True
                            break
                        if fail:
                            continue

                        print("What do you want in return?")
                        response = input("{remember to place commas between your items, to spell correctly, and to place a $ sign before any money you're offering} ")
                        print("")
                        items_to_take = [item.strip().capitalize() for item in response.split(',')]
                        for item in items_to_take:
                            if item[0] == '$':
                                if dollar_encountered:
                                    print("You already added money to your trade. Balance it out")
                                elif not item[1:].isdigit():
                                    print("{} is not a number".format(item[1:]))
                                elif int(item[1:]) > other_player.money:
                                    print("Player {} only has ${} left to trade".format(other_player.number, other_player.money))
                                else:
                                    dollar_encountered = True
                                    continue
                            elif item not in properties and item not in railroads and item not in utilities:
                                print("{} does not exist".format(item))
                            elif item not in other_player.props and item not in other_player.railroads and item not in other_player.utilities:
                                print("Player {} does not own {}".format(other_player.number, item))
                            else:
                                continue
                            fail = True
                            break
                        if fail:
                            continue

                        print("Does Player {} accept this deal?".format(other_player.number))
                        response = input("{input 'y' for yes and anything else for no} ")
                        print("")
                        if response == 'y':
                            for item in items_to_give:
                                if item in properties:
                                    player.props.remove(item)
                                    other_player.props.add(item)
                                    properties[item].owner = other_player.number
                                elif item in railroads:
                                    player.railroads.remove(item)
                                    for railroad in player.railroads:
                                        railroads[railroad].num_owned_by_owner -= 1
                                    num_owned = 0
                                    for railroad in other_player.railroads:
                                        if not railroads[railroad].mortgaged:
                                            num_owned += 1
                                        railroads[railroad].num_owned_by_owner += 1
                                    railroads[item].num_owned_by_owner = num_owned
                                    other_player.railroads.add(item)
                                elif item in utilities:
                                    player.utilities.remove(item)
                                    for utility in player.utilities:
                                        utilities[utility].num_owned -= 1
                                    num_owned = 0
                                    for utility in other_player.utilities:
                                        if not utilities[utility].mortgaged:
                                            num_owned += 1
                                        utilities[utility].num_owned += 1
                                    utilities[item].num_owned_by_owner = num_owned
                                    other_player.utilities.add(item)
                                else:
                                    money = int(item[1:])
                                    player.money -= money
                                    other_player.money += money

                            for item in items_to_take:
                                if item in properties:
                                    other_player.props.remove(item)
                                    player.props.add(item)
                                    properties[item].owner = player.number
                                elif item in railroads:
                                    other_player.railroads.remove(item)
                                    for railroad in other_player.railroads:
                                        railroads[railroad].num_owned_by_owner -= 1
                                    num_owned = 0
                                    for railroad in player.railroads:
                                        if not railroads[railroad].mortgaged:
                                            num_owned += 1
                                        railroads[railroad].num_owned_by_owner += 1
                                    railroads[item].num_owned_by_owner = num_owned
                                    player.railroads.add(item)
                                elif item in utilities:
                                    other_player.utilities.remove(item)
                                    for utility in other_player.utilities:
                                        utilities[utility].num_owned -= 1
                                    num_owned = 0
                                    for utility in player.utilities:
                                        if not utilities[utility].mortgaged:
                                            num_owned += 1
                                        utilities[utility].num_owned += 1
                                    utilities[item].num_owned_by_owner = num_owned
                                    player.utilities.add(item)
                                else:
                                    money = int(item[1:])
                                    other_player.money -= money
                                    player.money += money
                        else:
                            print("Player {} rejected the deal".format(other_player.number))
            # elif response == 'b':
            #     print("Which property would you like to develop?")
            #     prop = input("{remember to spell correctly} ").strip().capitalize()
            #     print("")
            #     if prop not in properties:
            #         print("{} is not a valid property".format(prop))
            #     elif prop not in player.props:
            #         print("You do not own {}".format(prop))
            #     else:
            #         propcolor = properties[prop].color
            #         colorprops = []
            #         for item in player.props:
            #             if properties[item].color == propcolor:
            #                 colorprops.append(item)
            #         if ((propcolor == 1 or propcolor == 8) and len(colorprops) != 2) or len(colorprops) != 3:
            #             print("You do not own all the properties required to build houses")
            #         else:
            #             houses_required = 0
            #             hotels_required = 0
            #             for item in colorprops:
            #                 if properties[item].num_houses < 4:
            #                     houses_required += 1
            #                 elif properties[item].num_houses == 4:
            #                     hotels_required += 1
            #             if houses_required == 0 and hotels_required == 0:
            #                 print("Properties of this color are already fully developed")
            #             else:
            #                 print("Would you like to build on just {} or all properties of the same color?".format(prop))
            #                 response = input("{enter 'a' for all and anything else for the single property} ")
            #                 print("")
            #                 if response == 'a':
            #                     if houses_required > houses_num:
            #                         print("There are only {} houses left to buy".format(houses_num))
            #                     elif hotels_required > hotels_num:
            #                         print("There are only {} hotels left to buy".format(hotels_num))
            #                     else:
            #                         cost = 0
            #                         for item in colorprops:
            #                             if properties[item].num_houses < 5:
            #                                 cost += properties[item].building_cost
            #                         if cost > player.money:
            #                             print("You need a total of ${} but you only have ${}".format(cost, player.money))
            #                         else:
            #                             print("Buy development for ${}?".format(cost))
            #                             response = input("{'y' for yes, anything else for no} ")
            #                             print("")
            #                             if response == 'y':
            #                                 player.money -= cost
            #                                 for item in colorprops:
            #                                     if properties[item].num_houses < 5:
            #                                         properties[item].num_houses += 1
            #                             else:
            #                                 print("You decided not to buy development")
            # elif response == 's':
            #     print("Which house would you like to sell?")
            #     prop = input("{remember to spell correctly} ").strip().capitalize()
            #     print("")
            #     if prop not in properties:
            #         print("{} is not a valid property".format(prop))
            #     elif prop not in player.props:
            #         print("You do not own {}".format(prop))
            #     else:
            #         propcolor = properties[prop].color
            #         colorprops = []
            #         for item in player.props:
            #             if properties[item].color == propcolor:
            #                 colorprops.append(item)
            #         if ((propcolor == 1 or propcolor == 8) and len(colorprops) != 2) or len(colorprops) != 3:
            #             print("You do not own all the properties required to sell houses")
            #         else:
            #             houses_required = 0
            #             hotels_required = 0
            #             for item in colorprops:
            #                 if properties[item].num_houses == 4:
            #                     hotels_required += 1
            #                 elif properties[item].num_houses > 0:
            #                     houses_required += 1
            #             if houses_required == 0 and hotels_required == 0:
            #                 print("Properties of this color don't have any houses")
            #             else:
            #                 print("Would you like to sell on just {} or all properties of the same color?".format(prop))
            #                 response = input("{enter 'a' for all and anything else for the single property} ")
            #                 print("")
            #                 if response == 'a':
            #                     if
            #                         cost = 0
            #                         for item in colorprops:
            #                             if properties[item].num_houses < 5:
            #                                 cost += properties[item].building_cost
            #                         if cost > player.money:
            #                             print("You need a total of ${} but you only have ${}".format(cost, player.money))
            #                         else:
            #                             print("Buy development for ${}?".format(cost))
            #                             response = input("{'y' for yes, anything else for no} ")
            #                             print("")
            #                             if response == 'y':
            #                                 player.money -= cost
            #                                 houses_num -= houses_required + 4*hotels_required
            #                                 hotels_num -= hotels_required
            #                                 for item in colorprops:
            #                                     if properties[item].num_houses < 5:
            #                                         properties[item].num_houses += 1
            #                             else:
            #                                 print("You decided not to buy development")
            elif response == 'v':
                print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-")
                for other_player in curr_players:
                    print("\nPlayer {}".format(other_player.number))
                    print("\tAt {}".format(board[other_player.pos]))
                    print("\tMoney: ${}".format(other_player.money))
                    if other_player.in_jail:
                        print("\tJailed")
                    if other_player.jail_free:
                        print("\tGet Out of Jail Free Card")
                    print("\nProperties:")
                    for prop in other_player.props:
                        print(prop)
                        print("\tColor: {}".format(properties[prop].color))
                        if properties[prop].num_houses != 0:
                            if properties[prop].num_houses == 1:
                                print("\t1 house")
                            elif properties[prop].num_houses < 5:
                                print("\t{} houses".format(properties[prop].num_houses))
                            else:
                                print("\tHotel")
                        if properties[prop].mortgaged:
                            print("\tMortgaged")
                    print("\nRailroads:")
                    for railroad in other_player.railroads:
                        print(railroad)
                        if railroads[railroad].mortgaged:
                            print("\tMortgaged")
                    print("\nUtilities:")
                    for utility in other_player.utilities:
                        print(utility)
                        if utilities[utility].mortgaged:
                            print("\tMortgaged")
                    print("")
                print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-\n")
            elif response == 'm':
                print("What property would you like to mortgage/reverse?")
                prop = input("{input property name. Make sure you spell it correctly} ").strip().capitalize()
                print("")
                if prop in player.props:
                    if properties[prop].mortgaged:
                        if player.money < properties[prop].price // 2:
                            print("You only have ${}. Reversing costs ${}".format(player.money, properties[prop].price // 2))
                        else:
                            print("Reverse for ${}?".format(properties[prop].price // 2))
                            response = input("{'y' for yes, anything else for no} ")
                            print("")
                            if response == 'y':
                                print("{} reversed".format(prop))
                                properties[prop].mortgaged = False
                                player.money -= properties[prop].price // 2
                            else:
                                print("You decided not to reverse")
                    else:
                        print("Mortgage and get ${}?".format(properties[prop].price // 2))
                        response = input("{'y' for yes, anything else for no} ")
                        print("")
                        if response == 'y':
                            print("{} mortgaged".format(prop))
                            properties[prop].mortgaged = True
                            player.money += properties[prop].price // 2
                        else:
                            print("You decided not to mortgage")
                elif prop in player.railroads:
                    if railroads[prop].mortgaged:
                        if player.money < railroads[prop].price // 2:
                            print("You only have ${}. Reversing costs ${}".format(player.money, railroads[prop].price // 2))
                        else:
                            print("Reverse for ${}?".format(railroads[prop].price // 2))
                            response = input("{'y' for yes, anything else for no} ")
                            print("")
                            if response == 'y':
                                print("{} reversed".format(prop))
                                railroads[prop].mortgaged = False
                                player.money -= railroads[prop].price // 2
                                for railroad in player.railroads:
                                    railroads[railroad].num_owned_by_owner += 1
                            else:
                                print("You decided not to reverse")
                    else:
                        print("Mortgage and get ${}?".format(railroads[prop].price // 2))
                        response = input("{'y' for yes, anything else for no} ")
                        print("")
                        if response == 'y':
                            print("{} mortgaged".format(prop))
                            railroads[prop].mortgaged = True
                            player.money += railroads[prop].price // 2
                            for railroad in player.railroads:
                                railroads[railroad].num_owned_by_owner -= 1
                        else:
                            print("You decided not to mortgage")
                elif prop in player.utilities:
                    if utilities[prop].mortgaged:
                        if player.money < utilities[prop].price // 2:
                            print("You only have ${}. Reversing costs ${}".format(player.money, utilities[prop].price // 2))
                        else:
                            print("Reverse for ${}?".format(utilities[prop].price // 2))
                            response = input("{'y' for yes, anything else for no} ")
                            print("")
                            if response == 'y':
                                print("{} reversed".format(prop))
                                utilities[prop].mortgaged = False
                                player.money -= utilities[prop].price // 2
                                for utility in player.utilities:
                                    utilities[utility].num_owned_by_owner += 1
                            else:
                                print("You decided not to reverse")
                    else:
                        print("Mortgage and get ${}?".format(utilities[prop].price // 2))
                        response = input("{'y' for yes, anything else for no} ")
                        print("")
                        if response == 'y':
                            print("{} mortgaged".format(prop))
                            utilities[prop].mortgaged = True
                            player.money += utilities[prop].price // 2
                            for utility in player.utilities:
                                utilities[utility].num_owned_by_owner -= 1
                        else:
                            print("You decided not to mortgage")
                elif prop not in properties and prop not in railroads and prop not in utilities:
                    print("{} doesn't exist".format(prop))
                else:
                    print("You do not own {}".format(prop))
            elif response == 'q':
                if player.money < 0:
                    print("Declare bankruptcy?")
                    response = input("{'y' for yes, anything else for no}")
                    if response == 'y':
                        print("Player {} declares bankruptcy".format(player.number))
                        print("Player {} loses".format(player.number))
                    else:
                        print("Player {} decides to continue".format(player.number))
                        continue
                else:
                    print("Decide to quit?")
                    response = input("{'y' for yes, anything else for no}")
                    if response == 'y':
                        print("Player {} decides to quit".format(player.number))
                        print("Player {} loses".format(player.number))
                    else:
                        print("Player {} decides to continue".format(player.number))
                        continue
                player.defeated = True
                for prop in player.props:
                    properties[prop].num_houses = 0
                    properties[prop].owner = -1
                    properties[prop].mortgaged = False
                for prop in player.railroads:
                    railroads[prop].num_owned_by_owner = -1
                    railroads[prop].owner = -1
                    railroads[prop].mortgaged = False
                for prop in player.utilities:
                    utilities[prop].num_owned_by_owner = -1
                    utilities[prop].owner = -1
                    utilities[prop].mortgaged = False
                curr_players.pop(i)
                i -= 1
                break
            else:
                break

        if die1 == die2 and not player.defeated:
            print("Player {} rolled doubles".format(player.number))
            print("Player {} rolls again".format(player.number))
            doubles += 1
        else:
            i = (i + 1) % len(curr_players)
            doubles = 0


print("End of game.")
print("Player {} wins!".format(curr_players[0].number))