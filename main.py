import random
import math

print("\nWelcome to Omri Weinmann's Robber Baron!")

print("\n\nThe Guilded Age, an era of rapid economic growth and heightened prosperity")
print("But behind the scenes, greedy robber barons do anything they can to make that extra buck")
print("You are one of these robber barons, do whatever it takes to rise to the tops.\n")

first_name = input("What is your name? ")
company_name = input("What is your company name? ")

money = 100000

quarter = 0

iron_prospect = 25000
oil_prospect = 25000
timber_prospect = 5000

raw_land_cost = 10000
factory_land_cost = 20000

labor1_cost = 20000
labor2_cost = 300000
labor3_cost = 1000000

deaths = 0

list_of_raw_goods = set(["Iron","Oil","Timber"])

list_of_prospects = []

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
    iron_prospect += max(0,int(iron_prospect * float(random.randint(-15,25))/100))
    oil_prospect += max(0,int(oil_prospect * float(random.randint(-15,25))/100))
    timber_prospect += max(0,int(timber_prospect * float(random.randint(-15,25))/100))
    raw_land_cost += max(0,int(oil_prospect * float(random.randint(-15,25))/100))
    factory_land_cost += max(0,int(timber_prospect * float(random.randint(-15,25))/100))
    labor1_cost += max(0,int(labor1_cost * float(random.randint(-15,25))/100))
    labor2_cost += max(0,int(labor2_cost * float(random.randint(-15,25))/100))
    labor3_cost += max(0,int(labor3_cost * float(random.randint(-15,25))/100))

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

list_of_factories = []
class Factory:
  def __init__(self, good, plot_id, goods_yield, min_deaths, max_deaths):
    self.good = good
    self.plot_id = plot_id
    self.goods_yield = goods_yield
    self.min_deaths = min_deaths
    self.max_deaths = max_deaths

  def __str__(self):
    return f"Your factory for {self.good}, which has a yield of {self.goods_yield} {self.good} per quarter. {str(max(0,random.randint(self.min_deaths,self.max_deaths)))} workers are projected to die."

prospect_id = 1


while True:
    fluctuate_market()
    quarter += 1
    print("\n"+convert_to_year_quarter())
    print("\nGood morning, '"+str(first_name)+".' Your company, '"+str(company_name)+"', currently has $"+str(money)+".\n")

    if quarter == 1:
        print("I suggest you prospect for resources; you cant make a factory if you dont know where to place one!")
    
    while True:
        print("\nWhat would you like to do? \n")
        print("0: Proceed to the next quarter")
        print("1: Prospect for resources")
        print("2: Build a factory")

        quarterly_choice = input("\n")

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
        elif quarterly_choice == "2":
            total_list = []
            for p in list_of_prospects:
                total_list.append(p)
            print("Here is the list of land plots you own:\n")
            
            x = 1
            for p in total_list:
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
                        print(total_list[inte-1])
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
                                    new_factory = Factory(plot.good,plot.plot_id,plot.goods_yield,-25,50)
                                    list_of_factories.append(new_factory)
                                    list_of_prospects.remove(plot)
                                    print(f"\nYou have built a {plot.good} plant that produces {plot.goods_yield}{plot.good} per quarter.")
                                    add_deaths = max(0,random.randint(-250,150))
                                    print(f"\nIt cost ${labor1_cost}")
                                    print(f"\nAdditionally it cost the lives of {add_deaths} workers.")
                                    input("\nAre you happy with yourself?\nY/N:")
                                    break
                                #elif labor_type_choice == "2":
                                    
                                #elif labor_type_choice == "3":
                            break
                                    


