import os
CorUsd = 3.56
dealCost = 6
def calcplz():
    clear = lambda: os.system('cls')
    print("Welcome to the Stock Calculator!")
    print("Buy?\n")
    sumBuy = float(input(">> "))
    clear()
    print("Amount?\n")
    Amount = float(input(">> "))
    clear()
    print("Current price?\n")
    sumSell = float(input(">> "))
    clear()
    Cost = ((((sumSell-sumBuy)*Amount)-dealCost)*CorUsd)*0.75
    print("If you Sell it now, you will get "+ str(Cost))
    input()
    calcplz()
calcplz()

input()