import sys

'''
userNum = input('Hello, Please enter your number: ')
result = print("***") if int(userNum) > 10 else print(userNum, userNum, userNum)
'''

'''
num = sys.argv[1]
if int(num) > 10:
    print("***")
else:
    print(num, num, num)
# print((10>2)+(5>1)) # 2
'''
'''
my_list = ["michael", "test"]
for name in my_list:
    print(name.title())
for name in my_list:
    if name.lower().find("m") >=0:
        print("Found 'm' in " + name + " at " + str(name.lower().find("m")))
'''
'''
num1 = int(input('Enter 1st number: '))
op = input('Enter Operator: ')
num2 = int(input('Enter 2nd number: '))
match op:
    case '+':
        print(num1+num2)
    case '-':
        print(num1-num2)
    case '/':
        print(num1/num2)
    case '*':
        print(num1*num2)
    case _:
        print('Wrong input, please try again')
'''
'''
Ask for 2 numbers from the user and an operator (* / - +)
Return the result according to the operator.


while <Condition>:

'''
'''
print("Welcome to calculator! For exit type 'exit'")

while True:
    num1 = input("Please provide first number:\n")
    if num1 == "exit":
        print("Bay-Bay")
        break
    num1 = int(num1)
    op = input("Please provide the operator (+ - * /):\n")
    num2 = int(input("Please provide the second number:\n"))

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else:
        print("Invalid Operator!")
'''
class Animal:
    #Constractor
    def __init__(self,name,numOfLegs,isAggressive):
        self.name = name
        self.numOfLegs = numOfLegs
        self.isAggressive = isAggressive
    def __str__(self):
        return "I am an Animal\nMy name is: " + self.name + "\nI have " +str(self.numOfLegs) + " legs"
    def move (self, toLocation):
        print(self.name + " is moving to " + toLocation)

dog1 = Animal("Chuchu", 4, False)
print(dog1.__str__)