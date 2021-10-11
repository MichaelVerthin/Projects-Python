# let's make a calculator:
# if i will do this:
    # num1 = input("enter a number")
    # num2 = input("enter another number")
    # result = num1 + num2
    # print(result)
# python will convert them to strings and will add as a text..
# if i want to acually add them i can do this:
    # result = int(num1) + int(num2)
# this way it will add both of those num's together, BUT if i enter 3.5 for insctance it will break the code
# so i can do this:
    # result = float(num1) + float(num2)

# arreys!
# if i have an arrey:
    # friends = ["karen", "jim", "yosef", "alice", "alex"]
# if i want i can access all the parts of the arrey with - friends['index of the wanted part']
# i can also access some of the parts:
    # friends[1:] - this will print everything from index 1 till the end.
# i can also chose how much i want:
    # friends[1:3] - this will print from the 1 index till 3 index NON INCLUDING THE 3RD ONE.
# i can also link two strings:
    # another list: nums = [1,3,5,6,7,2,3]
    # friends.extend(nums)
# or add another element to a list:
    # friends.append("kristin")
# or add an element in a chosen index and push all the others by 1
    # friends.insert(1, "kelly")
# i can also remove an element:
    # friends.remove("jim")
# or remove everything:
    # friends.clear()
# oh and pop works too:
    # friends.pop() - this will remove the last element in the arrey
# if i want to change the arrey in alphabetic order:
    # friends.sort()
# oh and there is .copy() which will copy an arrey for another variable for example
# TUPELS - basiclly those are list that cannot be changed
    # nums = (4,5)
    # nums[0] = 1  - this will return error since i cant change a tuple after i set it

# functions:
# like JS i define them by writing: def 'name'():
# all the stuff in the inside of the function (using TAB) are inside and all the things outside are not
    # def sayHi():
        # print("hello")
    # sayHi()
# return:
    # def coub(num)
        # return num*num*num
    # result = coub(4)
    # print(result)
# the print will be 64.
# def print_hello(name):
#     print("Hello " + name + "!")
# get_name = input("please enter your name: ")
# print_hello(get_name)
is_male = True
is_Tall = False
# if is_male and is_Tall: # or\and
#     print("You are a tall male")
# elif is_male and not(is_Tall): # elif = else+if
#     print ("Yo are a short male")
# else:
#     print("You are neither a male or tall")

# Dictionery:
monthConvert = {
    "Jan": "January",
    "Feb": "Febuary",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
# print(monthConvert["Dec"]) # Get Key
# print(monthConvert.get("Mar")) # Another way to get a key
# print(monthConvert.get("luv")) # Will get "none"
# print(monthConvert.get("luv", "Not a valid key")) # Will get "Not a valid key"

# Guessing game!
print("Welcome to the 'Gussing Game!'")
print("Guess the word currectly to win!\n")
sercet_word = "desk"
guess = ""
i = 1
while guess != sercet_word:
    guess = input("Enter your guess: ")
    if guess != sercet_word:
         print("Wrong, Try again!\n")
    i += 1
    if i == 2:
        print("Hint: only use small letters.\n")
    elif i == 4:
        print("Another Hint: it's made of wood.\n")
    elif i == 6:
        print("Another hint: you place your stuff on it.\n")
    elif i == 8:
        print("last hint: it's a desk...\n")
print("\nCorrect!")
print("You Win!\n")
input("Press 'Enter' to exit")

# for loop
for letter in "michael":
    print(letter)

# 2D arrey
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[0][2]) # this will return '3' 

# make a language, kinda
def translate(phrase):
    translation = ""
    for latter in phrase:
        if latter.lower() in "aeiou":
            translation += "g"
        else:
            translation += latter
    return translation
print(translate(input("Enter a phrase: ")))

