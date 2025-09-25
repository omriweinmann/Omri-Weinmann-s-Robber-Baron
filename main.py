import random

print("\nWelcome to Omri Weinmann's Robber Baron!")

print("\n\nThe Guilded Age, an era of rapid economic growth and heightened prosperity")
print("But behind the scenes, greedy robber barons do anything they can to make that extra buck")
print("You are one of these robber barons, do whatever it takes to rise to the tops.\n")

first_name = input("What is your name? ")
company_name = input("What is your company name? ")

money = 100000
quarter = 0

iron_prospect = 50000
oil_prospect = 50000
timber_prospect = 10000


print("")
print("\nWelcome, '"+str(first_name)+"' of '"+str(company_name)+".' This is the start of your greedy journey to rise to the top.\n")

game_over = False

def change_prospect():
    global iron_prospect
    iron_prospect += int(iron_prospect * float(random.randint(-10,10))/100)

while True:
    change_prospect()
    quarter += 1
    print("Quarter "+str(quarter))
    print("\nGood morning, '"+str(first_name)+".' Your company, '"+str(company_name)+"', currently has $"+str(money)+".\n\n")
    print("What would you like to do? \n\n0: Prospect for resources")

    quarterlyChoice = input("\n\n")

    if quarterlyChoice == "0":
        print("Good choice! ")
        print(iron_prospect)

