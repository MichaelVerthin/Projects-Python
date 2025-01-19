import os
os.system('color')
CorUsd = 3.56
dealCost = 6

def calcplz():
    clear = lambda: os.system('cls')
    print("Welcome to the Stock Calculator!")
    print("////////////////////////////////")
    print("Current USD to NIS: ")
    usdToNis = float(input(">> "))
    print("Amount of tax for Action: ")
    dealCost = float(input(">> "))
    print("Cost of the Stocks you got:")
    sumBuy = float(input(">> "))
    print("Amount of Stocks you got:")
    Amount = float(input(">> "))
    print("Current cost of the Stock you got:")
    sumSell = float(input(">> "))
    Cost = ((((sumSell-sumBuy)*Amount)-dealCost)*usdToNis)*0.75
    CostBf = ((((sumSell-sumBuy)*Amount)-dealCost)*usdToNis)
    print("////////////////////////////////")
    print("If you sell now, you will get \033[92m" + str(round(Cost)) + "₪\033[0m After TAX")
    print("(\033[93m"+ str(round(CostBf)) +"₪\033[0m before, " + str(round(CostBf-Cost)) + "₪ Goes to the Government, \033[1mDEMOCRACY!\033[0m" + ")")
    input()
    clear()
    calcplz()
calcplz()
input()