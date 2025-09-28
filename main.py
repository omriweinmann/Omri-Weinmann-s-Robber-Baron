import random
import math

# Amir Weinmann was here.

print("\nWelcome to Omri Weinmann's Robber Baron!")

print("\n\nThe Guilded Age, an era of rapid economic growth and heightened prosperity")
print("But behind the scenes, greedy robber barons do anything they can to make that extra buck")
print("You are one of these robber barons, do whatever it takes to rise to the tops.\n")

first_name = input("What is your name? ")
company_name = input("What is your company name? ")

money:int = 100000

quarter = 0

iron_prospect = 25000
oil_prospect = 25000
timber_prospect = 5000

raw_land_cost = 10000
factory_land_cost = 20000

labor1_cost = 20000
labor2_cost = 300000
labor3_cost = 1000000

cost_to_gerrymand = 5000

market = {
    "Oil": 1000,
    "Timber": 250,
    "Iron": 750,
    "Grain": 100,
    "Refined Oil": 3500,
    "Planks": 350,
    "Steel": 2000,
    "Housing": 15000,
    "Railroad": 35000,
    "Foodstuffs": 2000,
    "Processed Foodstuffs": 7500,
    "Automobiles": 10000,
    "Ships": 100000,
    "Paper": 2000,
    "Newspapers": 5000,
    "Books": 7500,
    "Appliances": 10000,
    "Tools": 2500,
    "Gunpowder": 10000,
    "Machine Guns": 20000,
    "Bombs": 5000,
    "Rifles": 10000,
    "Gunpowder": 100,
}

deaths = 0

list_of_raw_goods = set(["Iron","Oil","Timber"])

list_of_prospects = []

list_of_properties = []

print("")
print("\nWelcome, '"+str(first_name)+"' of '"+str(company_name)+".' This is the start of your greedy journey to rise to the top.")

game_over = False

def fluctuate_market():
    global iron_prospect
    global oil_prospect
    global timber_prospect
    global raw_land_cost
    global factory_land_cost
    global labor1_cost
    global labor2_cost
    global labor3_cost
    global market
    global cost_to_gerrymand
    iron_prospect += max(0,int(iron_prospect * float(random.randint(-15,25))/100))
    oil_prospect += max(0,int(oil_prospect * float(random.randint(-15,25))/100))
    timber_prospect += max(0,int(timber_prospect * float(random.randint(-15,25))/100))
    raw_land_cost += max(0,int(oil_prospect * float(random.randint(-15,25))/100))
    factory_land_cost += max(0,int(timber_prospect * float(random.randint(-15,25))/100))
    labor1_cost += max(0,int(labor1_cost * float(random.randint(-15,25))/100))
    labor2_cost += max(0,int(labor2_cost * float(random.randint(-15,25))/100))
    labor3_cost += max(0,int(labor3_cost * float(random.randint(-15,25))/100))
    cost_to_gerrymand += max(0,int(cost_to_gerrymand * float(random.randint(-15,35))/100))
    for m in market:
        market[m] += max(0,int(market[m] * float(random.randint(-5,10))/100))

def convert_to_year_quarter():
    global quarter
    quarter_s = quarter % 4
    year = math.floor(quarter/4)
    if quarter_s == 0:
        quarter_s = 4
        year -= 1
    return "Year "+str(year)+", Quarter "+str(quarter_s)

class Prospect:
  def __init__(self, good, plot_id, goods_yield):
    self.good = good
    self.plot_id = plot_id
    self.goods_yield = goods_yield

  def __str__(self):
    return f"Your prospect for {self.good}, which has a yield of {self.goods_yield} {self.good} per quarter"

street_names = [
    "John",
    "Johnson",
    "Johnman",
    "Johnathan",
    "Jack",
    "Jackman",
    "Jackson",
    "Jackingthon",
    "Peter",
    "Peterson",
    "Peteria",
    "Stark",
    "Tony",
    "Aaron",
    "Paul",
    "Omri",
    "Weinmann",
    "David",
    "Davidson",
    "Sarah",
    "Lopsided",
    "Narnia",
    "McStreet",
    "McDonald",
    "Fairweather",
    "Utterson",
    "Jekyll",
    "Shadowfax",
    "Frodo",
    "Sam",
    "Samwise",
    "Gamgee",
    "Baggins",
    "Bilbo",
    "Oakenshield",
    "Churchill",
    "Roosevelt",
    "Gandalf",
    "Sauron",
    "Boromir",
    "Gimli",
    "Thorin",
    "Bruce",
    "Banner",
    "Wayne",
    "Kevin",
    "Luca",
    "Streety",
    "McStreety",
    "Abraham",
    "Lincoln",
    "America",
    "Canada",
    "Rehovot",
    "Tel Aviv",
    "Paris",
    "London",
    "Beijing",
    "Cairo",
    "Damascus",
    "Galil",
    "Kibbutz",
    "Vin",
    "Elend",
    "Kelsier",
    "Sazed"
]

street_endings = [
    "Road",
    "Street",
    "Way",
    "Avenue",
    "Drive",
    "Lane",
    "Grove",
    "Gardens",
    "Place",
    "Circus",
    "Crescent",
    "Bypass",
    "Close",
    "Square",
    "Hill",
    "Mews",
    "Vale",
    "Rise",
    "Mead",
]

factory_types = {
    "Refined Oil": {"Oil": 3},
    "Planks": {"Timber": 1},
    "Steel": {"Iron": 2},
    "Housing": {"Steel": 3, "Planks": 5},
    "Railroad": {"Steel": 10},
    "Foodstuffs": {"Grain": 5},
    "Processed Foodstuffs": {"Foodstuffs": 5},
    "Automobiles": {"Steel": 2, "Refined Oil": 1},
    "Ships": {"Steel": 20, "Refined Oil": 5},
    "Paper": {"Timber": 1},
    "Newspapers": {"Paper": 1},
    "Books": {"Paper": 1},
    "Appliances": {"Paper": 1},
    "Tools": {"Planks": 1},
    "Gunpowder": {"Paper": 1},
    "Machine Guns": {"Gunpowder": 10, "Steel": 10},
    "Bombs": {"Gunpowder": 10,"Steel": 2},
    "Rifles": {"Gunpowder": 5,"Steel": 10},
}

class Property:
    def __init__(self):
        self.cost = int(random.randint(int(factory_land_cost/2), int(factory_land_cost*2)))
        print(len(street_names))
        self.name = str(random.randint(111,9999))+" "+street_names[random.randint(1,len(street_names))-1]+" "+street_endings[random.randint(1,len(street_endings))-1]

    def __str__(self):
        return f"Your property on {self.name}"
    
list_of_factories = []

class Factory:
  def __init__(self, good, plot_id, goods_yield, min_deaths, max_deaths, needs):
    self.good = good
    self.plot_id = plot_id
    self.goods_yield = goods_yield
    self.min_deaths = min_deaths
    self.max_deaths = max_deaths
    self.needs = needs

  def __str__(self):
    if self.needs == {}:
        string = f"Your factory for {self.good}, which has a yield of {self.goods_yield} {self.good} per quarter. {str(max(0,random.randint(self.min_deaths,self.max_deaths)))} workers are projected to die."
        return string
    else:
        string = f"Your factory for {self.good}, which has a yield of {self.goods_yield*3} {self.good} when its input needs are fully met. {str(max(0,random.randint(self.min_deaths,self.max_deaths)))} workers are projected to die."
        extrastring = "\n - To produce this, the factory requires a minimum input of "
        x = 0
        for need in self.needs:
            x += 1
            extrastring = extrastring + f"{self.needs[need]} {need}"
            if not x == len(self.needs):
                extrastring = extrastring + ", "
        return string + extrastring
        

prospect_id = 1

political_standing = 10

conservatives = 0
liberals = 0
reactionaries = 0

bailout = False

goods = {}

while True:
    if money < 0:
        print(f"\n\n\nYou are in insurmountable amounts of debt! Game over.\n\nYour actions caused the deaths of {deaths} people.\n\nGame Over! You ended with ${money}\n\n\n")
        break
    political_standing = max(10,political_standing-5)
    conservatives = max(0,conservatives-5)
    liberals = max(0,liberals-5)
    reactionaries = max(0,reactionaries-5)
    for factory_raw in list_of_factories:
        factory:Factory = factory_raw
        go = True
        while True:
            once = 0
            if not factory.needs == {}:
                once += 1
                for need in factory.needs:
                    if need in goods:
                        if not goods[need] >= factory.needs[need]:
                            go = False
                            once = 3
                            break
                        else:
                            goods[need] -= factory.needs[need]
                    else:
                        go = False
                        once = 3
                        break
            else:
                once = 3
            if go == True:
                if factory.good in goods:
                    goods[factory.good] += factory.goods_yield
                else:
                    goods[factory.good] = factory.goods_yield
                deaths += max(0,random.randint(factory.min_deaths,factory.max_deaths))
            print(once)
            if once >= 3:
                break
            

    fluctuate_market()
    quarter += 1
    print("\n"+convert_to_year_quarter())
    if not quarter == 1 and quarter % 4 == 1:
        tax = int((max(money,0) * 0.07) + (15000 * ((400-(political_standing+conservatives+liberals+reactionaries))/800+0.5)))
        print(f"\nYou have lost ${tax} due to taxes and other miscellaneous costs.")
        money -= tax
    print("\nGood morning, '"+str(first_name)+".' Your company, '"+str(company_name)+"', currently has $"+str(money)+".\n")

    if quarter == 1:
        print("I suggest you prospect for resources; you cant make a factory if you dont know where to place one!")
    if quarter == 2:
        print("If you have not already, I suggest you build a factory on your prospect to start making goods")
    if quarter == 3:
        print("Export your goods to start making money!")
    if quarter == 4:
        print("At the start of every year you are taxed.")
    if quarter == 5:
        print("Buy properties to build new types of factories and eventually make elaborate industry chains!")
    xxx = 0
    while True:
        if not xxx == 0:
            print(f"\nYou have ${money}")
        xxx += 1
        print("\nWhat would you like to do? \n")
        print("0: Proceed to the next quarter")
        print("1: Prospect for resources")
        print("2: Buy a property")
        print("3: Build a factory")
        print("4: Import/Export")
        print("5: Actions")
        print("6: Company information")

        quarterly_choice = input("\n")

        if quarterly_choice == "money":
            money += 9999999

        if quarterly_choice == "1":
            print("Good choice!\n")
            print("0: Go back\n")
            print("Iron: It currently costs $"+str(iron_prospect)+" to prospect for Iron")
            print("Oil: It currently costs $"+str(oil_prospect)+" to prospect for Oil")
            print("Timber: It currently costs $"+str(timber_prospect)+" to prospect for Timber")
            while True:
                prospect_choice = input("\nWhat would you like to prospect for? ")
                if prospect_choice in list_of_raw_goods:
                    cost = 0
                    if prospect_choice == "Timber":
                        cost = timber_prospect
                    elif prospect_choice == "Iron":
                        cost = iron_prospect
                    else:
                        cost = oil_prospect
                    money -= cost
                    potential_prospect = Prospect(prospect_choice, prospect_id, random.randint(1,25))
                    print(f"\nYour surveyors have found a plot of land with a yield of {potential_prospect.goods_yield} {potential_prospect.good} per quarter\n")
                    print(f"You now have ${money}\n")
                    print(f"It costs ${raw_land_cost} to buy this plot of land\n")
                    while True:
                        prospect_accept_choice = input("Y/N: ")
                        if prospect_accept_choice == "Y":
                            money -= raw_land_cost
                            list_of_prospects.append(potential_prospect)
                            prospect_id += 1
                            #print(list_of_prospects)
                            print(f"You now have ${money}")
                            break
                        elif prospect_accept_choice == "N":
                            print(f"You now have ${money}")
                            break
                if prospect_choice == "0":
                    break
        elif quarterly_choice == "0":
            break
        elif quarterly_choice == "3":
            total_list = []
            for p in list_of_prospects:
                total_list.append(p)
            for p in list_of_properties:
                total_list.append(p)
            print("Here is the list of land plots you own:\n")
            
            x = 0
            for p in total_list:
                x+= 1
                print(str(x)+": "+str(p))

            print("\n0: Go back\n")
            while True:
                factory_choice = input("What plot would you like to build on? ")
                inte = -1
                try:
                    inte = int(factory_choice)
                except:
                    print("")
                if factory_choice == "0":
                    break
                elif not inte == -1:
                    continues = False
                    try:
                        #print(total_list[inte-1])
                        continues = True
                    except:
                        print("\nInvalid plot.\n")
                    if continues == True:
                        plot = total_list[inte-1]
                        if plot in list_of_prospects:
                            print("Choose budget: \n")
                            print(f"1: Small (96 hour work week, minimal safety standards, child labor), ${labor1_cost}")
                            print(f"2: Medium (60 hour work week, better safety standards, no child labor), ${labor2_cost}")
                            print(f"3: Large (40 hour work week, best safety standards, no child labor), ${labor3_cost}")
                            print(f"\n0: Cancel")
                            while True:
                                labor_type_choice = input("\nWhat would you like to do? ")

                                if labor_type_choice == "0":
                                    break
                                elif labor_type_choice == "1":
                                    money -= labor1_cost
                                    new_factory = Factory(plot.good,plot.plot_id,plot.goods_yield,-25,25,{})
                                    list_of_factories.append(new_factory)
                                    list_of_prospects.remove(plot)
                                    print(f"\nYou have built a {plot.good} plant that produces {plot.goods_yield} {plot.good} per quarter.")
                                    add_deaths = max(0,random.randint(-250,150))
                                    deaths += add_deaths
                                    print(f"\nIt cost ${labor1_cost}.")
                                    print(f"You now have ${money}.")
                                    print(f"\nAdditionally it cost the lives of {add_deaths} workers.")
                                    input("\nAre you happy with yourself?\nY/N:")
                                    break
                                elif labor_type_choice == "2":
                                    money -= labor2_cost
                                    new_factory = Factory(plot.good,plot.plot_id,plot.goods_yield,-35,10,{})
                                    list_of_factories.append(new_factory)
                                    list_of_prospects.remove(plot)
                                    print(f"\nYou have built a {plot.good} plant that produces {plot.goods_yield} {plot.good} per quarter.")
                                    add_deaths = max(0,random.randint(-350,100))
                                    deaths += add_deaths
                                    print(f"\nIt cost ${labor2_cost}.")
                                    print(f"You now have ${money}.")
                                    print(f"\nAdditionally it cost the lives of {add_deaths} workers.")
                                    input("\nAre you happy with yourself?\nY/N:")
                                    break
                                elif labor_type_choice == "3":
                                    money -= labor3_cost
                                    new_factory = Factory(plot.good,plot.plot_id,plot.goods_yield,-50,2,{})
                                    list_of_factories.append(new_factory)
                                    list_of_prospects.remove(plot)
                                    print(f"\nYou have built a {plot.good} plant that produces {plot.goods_yield} {plot.good} per quarter.")
                                    add_deaths = max(0,random.randint(-350,25))
                                    deaths += add_deaths
                                    print(f"\nIt cost ${labor3_cost}.")
                                    print(f"You now have ${money}.")
                                    print(f"\nAdditionally it cost the lives of {add_deaths} workers.")
                                    input("\nAre you happy with yourself?\nY/N:")
                                    break
                            break
                        if plot in list_of_properties:
                            print("\nHere is the list of factories you can put on this plot:\n\n0: Cancel\n")
                            for f in factory_types:
                                string = " Requires an input of: "
                                for x in factory_types[f]:
                                    string = string + f"{factory_types[f][x]} {x},"
                                print(f"{f}:"+string)
                            while True:
                                property_choice = input("\nWhat would you like to do? ")
                                if property_choice == 0:
                                    break
                                if property_choice in factory_types:
                                    print("Choose budget: \n")
                                    print(f"1: Small (96 hour work week, minimal safety standards, child labor), ${labor1_cost}")
                                    print(f"2: Medium (60 hour work week, better safety standards, no child labor), ${labor2_cost}")
                                    print(f"3: Large (40 hour work week, best safety standards, no child labor), ${labor3_cost}")
                                    print(f"\n0: Cancel")
                                    while True:
                                        labor_type_choice = input("\nWhat would you like to do? ")

                                        if labor_type_choice == "0":
                                            break
                                        elif labor_type_choice == "1":
                                            money -= labor1_cost
                                            new_factory = Factory(property_choice,0,1,-25,25,factory_types[property_choice])
                                            list_of_factories.append(new_factory)
                                            list_of_properties.remove(plot)
                                            print(f"\nYou have built a {new_factory.good} plant that produces {new_factory.goods_yield} {new_factory.good} per quarter.")
                                            add_deaths = max(0,random.randint(-250,150))
                                            deaths += add_deaths
                                            print(f"\nIt cost ${labor1_cost}.")
                                            print(f"You now have ${money}.")
                                            print(f"\nAdditionally it cost the lives of {add_deaths} workers.")
                                            input("\nAre you happy with yourself?\nY/N:")
                                            break
                                        elif labor_type_choice == "2":
                                            money -= labor2_cost
                                            new_factory = Factory(property_choice,0,1,-35,10,factory_types[property_choice])
                                            list_of_factories.append(new_factory)
                                            list_of_properties.remove(plot)
                                            print(f"\nYou have built a {new_factory.good} plant that produces {new_factory.goods_yield} {new_factory.good} per quarter.")
                                            add_deaths = max(0,random.randint(-350,100))
                                            deaths += add_deaths
                                            print(f"\nIt cost ${labor2_cost}.")
                                            print(f"You now have ${money}.")
                                            print(f"\nAdditionally it cost the lives of {add_deaths} workers.")
                                            input("\nAre you happy with yourself?\nY/N:")
                                            break
                                        elif labor_type_choice == "3":
                                            money -= labor3_cost
                                            new_factory = Factory(property_choice,0,1,-50,2,factory_types[property_choice])
                                            list_of_factories.append(new_factory)
                                            list_of_properties.remove(plot)
                                            print(f"\nYou have built a {new_factory.good} plant that produces {new_factory.goods_yield} {new_factory.good} per quarter.")
                                            add_deaths = max(0,random.randint(-350,25))
                                            deaths += add_deaths
                                            print(f"\nIt cost ${labor3_cost}.")
                                            print(f"You now have ${money}.")
                                            print(f"\nAdditionally it cost the lives of {add_deaths} workers.")
                                            input("\nAre you happy with yourself?\nY/N:")
                                            break
                                    break
        elif quarterly_choice == "6":
            while True:
                info_choice = input("\nWhat would you like to look at?\n\n0: Go back\n\n1: List of factories\n2: List of goods\n3: Market \n4: Politics\n\n")

                if info_choice == "0":
                    break
                elif info_choice == "1":
                    print("\nHere are all of your factories:\n")
                    x = 0
                    for factory in list_of_factories:
                        x += 1
                        print(str(x)+": "+str(factory))
                elif info_choice == "2":
                    print("\nHere are your goods:\n")
                    print(f"\n${money}\n")
                    x = 0
                    for good in goods:
                        print(str(good)+": "+str(goods[good]))
                    print(f"\nIt cost the lives of {deaths} people to get you where you are now")
                elif info_choice == "3":
                    print("\nHere is the current market rate for each good:\n")
                    x = 0
                    for good in market:
                        print(str(good)+": $"+str(market[good]))
                elif info_choice == "4":
                    print(f"\nYour political standing is: {political_standing}/100")
                    print(f"\nYour conservative support is: {conservatives}/100")
                    print(f"Your liberal support is: {liberals}/100")
                    print(f"Your reactionary support is: {reactionaries}/100")
                    if bailout == True:
                        print("\nYou have used your government bailout.\n")
                    else:
                        print("\nYou have not used your government bailout.\n")
        elif quarterly_choice == "2":
            while True:
                potential_property = Property()
                print(f"\nYou have the potential to buy a property on {potential_property.name} for ${potential_property.cost}")
                break2 = False
                while True:
                    property_choice = input(f"\n0: Go back\n\nY/N:")
                    if property_choice == "Y":
                        money -= potential_property.cost
                        print(f"\nYou have bought the property on {potential_property.name}")
                        list_of_properties.append(potential_property)
                        break
                    elif property_choice == "N":
                        break
                    elif property_choice == "0":
                        break2 = True
                        break
                if break2 == True:
                    break
        elif quarterly_choice == "4":
            imp_exp_choice = input("What would you like to do?\n\nImport/Export: ")

            if imp_exp_choice == "Import":
                imp_choice = input("What would you like to import? ")

                if imp_choice in market:
                    imp_amount_choice = input(f"How much {imp_choice} would you like to buy? ")
                    try:
                        integer = int(imp_amount_choice)
                        are_you_sure = input(f"It would cost ${market[imp_choice]*integer} to buy {imp_amount_choice} {imp_choice}, are you sure? Y/N: ")
                        if are_you_sure == "Y":
                            money -= market[imp_choice]*integer
                            if imp_choice in goods:
                                goods[imp_choice] += integer
                            else:
                                goods[imp_choice] = integer
                    except:
                        print("\nInvalid amount\n")
                else:
                    print("\nInvalid good\n")
            if imp_exp_choice == "Export":
                imp_choice = input("What would you like to export? ")
                if imp_choice in market:
                    imp_amount_choice = input(f"How much {imp_choice} would you like to sell? ")
                    try:
                        integer = int(imp_amount_choice)
                        if imp_choice in goods and goods[imp_choice] >= integer:
                            are_you_sure = input(f"You will get ${market[imp_choice]*integer} from selling {imp_amount_choice} {imp_choice}, are you sure? Y/N: ")
                            if are_you_sure == "Y":
                                money += market[imp_choice]*integer
                                goods[imp_choice] -= integer
                        else:
                            print(f"\nYou do not have enough {imp_choice}\n")
                    except:
                        print("\nInvalid amount\n")
                else:
                    print("\nInvalid good\n")
        elif quarterly_choice == "5":
            while True:
                print(f"\n0: Cancel\n")
                print("1: Political actions")
                print("2: Bailout (If you are in debt, this will save you depending on your political standings, but this will prevent you from making political actions)")
                print(f"3: Lobby for war (${cost_to_gerrymand*6}) (war related goods will increase in value)")
                print(f"4: Push for reforms (${cost_to_gerrymand*4}) (Political standing and will increase)")
                print(f"5: Roll back reforms (Gain ${cost_to_gerrymand*10} from reactionaries) (Lots of support needed)")
                action_choice = input("\nWhat would you like to do? ")
                if action_choice == "0":
                    break 
                elif action_choice == "1":
                    if bailout == False:
                        while True:
                            print(f"\n0: Go back\n")
                            print("1: Gerrymander (Increases political standing by 20)")
                            print("2: Donate (Increases political standing by 10)")
                            print("3: Increase conservative support (Requires a political standing of 40)")
                            print("4: Increase liberal support (Requires a political standing of 40)")
                            print("5: Increase reactionary support (Requires a political standing of 40)")
                            political_action_choice = input("\nWhat would you like to do? ")
                            if political_action_choice == "0":
                                break
                            elif political_action_choice == "1":
                                p_action_confirm_choice = input(f"\nGerrymandering will cost you ${int(cost_to_gerrymand*2)}, are you sure? Y/N: ")
                                if p_action_confirm_choice == "Y":
                                    political_standing = min(100,political_standing+20)
                                    money -= int(cost_to_gerrymand*2)
                                    print(f"\nYour political standing is now {political_standing}/100")
                            elif political_action_choice == "2":
                                p_action_confirm_choice = input(f"\Donating will cost you ${int(cost_to_gerrymand)}, are you sure? Y/N: ")
                                if p_action_confirm_choice == "Y":
                                    political_standing = min(100,political_standing+10)
                                    money -= int(cost_to_gerrymand)
                                    print(f"\nYour political standing is now {political_standing}/100")
                            elif political_action_choice == "3":
                                if political_standing >= 40:
                                    p_action_confirm_choice = input(f"\Increasing conservative support will cost you ${int(cost_to_gerrymand)}, are you sure? Y/N: ")
                                    if p_action_confirm_choice == "Y":
                                        political_standing = min(100,conservatives+20)
                                        money -= int(cost_to_gerrymand)
                                        print(f"\nYour standing with the conservatives is now {conservatives}/100")
                                else:
                                    print("\nNot enough political standing\n")
                            elif political_action_choice == "4":
                                if political_standing >= 40:
                                    p_action_confirm_choice = input(f"\Increasing liberal support will cost you ${int(cost_to_gerrymand)}, are you sure? Y/N: ")
                                    if p_action_confirm_choice == "Y":
                                        political_standing = min(100,liberals+20)
                                        money -= int(cost_to_gerrymand)
                                        print(f"\nYour standing with the liberals is now {liberals}/100")
                                else:
                                    print("\nNot enough political standing\n")
                            elif political_action_choice == "5":
                                if political_standing >= 40:
                                    p_action_confirm_choice = input(f"\Increasing reactionary support will cost you ${int(cost_to_gerrymand)}, are you sure? Y/N: ")
                                    if p_action_confirm_choice == "Y":
                                        political_standing = min(100,reactionaries+20)
                                        money -= int(cost_to_gerrymand)
                                        print(f"\nYour standing with the reactionaries is now {reactionaries}/100")
                                else:
                                    print("\nNot enough political standing\n")
                    else:
                        print("\nYou have used your bailout, and cannot make anymore political actions.")
                elif action_choice == "2":
                    if money < 0:
                        political_bailout = political_standing*150
                        conservative_bailout = conservatives*100
                        liberal_bailout = liberals*100
                        reactionary_bailout = reactionaries*100
                        print(f"The government has given you ${political_bailout}")
                        print(f"\nIn addition, conservatives have given you ${conservative_bailout}")
                        print(f"In addition, liberals have given you ${liberal_bailout}")
                        print(f"In addition, reactionaries have given you ${reactionary_bailout}")
                    else:
                        print("\nYou are not in debt.")
                elif action_choice == "3":
                    if reactionaries + conservatives > (75-liberals):
                        print("Your country is going to war because of you, war related goods have increased in value")
                        add_deaths = random.randint(100,900000)
                        deaths += add_deaths
                        money -= cost_to_gerrymand*6
                        print(f"\nThe war resulted in {add_deaths} casualties")
                        market["Gunpowder"] += int(market["Gunpowder"] * (random.randint(0,50)/100))
                        market["Rifles"] += int(market["Rifles"] * (random.randint(0,50)/100))
                        market["Machine Guns"] += int(market["Machine Guns"] * (random.randint(0,50)/100))
                        market["Bombs"] += int(market["Bombs"] * (random.randint(0,50)/100))
                    else:
                        print("You need to have more support (especially from conservatists and reactionaries)")
                elif action_choice == "4":
                    if liberals > (150-(conservatives+reactionaries)):
                        print("You have succeeded in pushing for reforms")
                        money -= cost_to_gerrymand*4
                        political_standing = min(100,political_standing+20)
                        print(f"\nYour political standing is now {political_standing}/100")
                    else:
                        print("You need to have more support (especially from liberals)")
                elif action_choice == "5":
                    if reactionaries > (275-(conservatives+liberals+political_standing)):
                        print("You have succeeded in rolling back reforms")
                        money += cost_to_gerrymand*10
                        print(f"\nReactionaries have given you ${cost_to_gerrymand*8}")
                    else:
                        print("You need to have more support (especially from reactionaries)")




