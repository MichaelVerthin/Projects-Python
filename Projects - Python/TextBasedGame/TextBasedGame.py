# make a text based game.
# make inventory
# make tutorial

# Functions:
    
def part_2_the_docks():
    print("////////////////////////////////////////////////////////////////////Part-02//\n") # the // between blockes of text
    print("// You go with your mother to the dockes where you should meet your father")
    print("// you see a crowed of people surounding the bay at which his ship need to dock")
    print("// your mother lifts you to her arms and tries to pass through the crowed")
    print("// both of you have good sight of the dock, now you wait for his return")
    print("\n// after a few minutes a ship came, it was greeted with cheers and loud appluse")
    print("// the ship her father was on brough food and marchent from far beyond")
    print(input("// "))

def part_1_search_room(action):
    print("\n////////////////////////////////////////////////////////////////////Part-01//\n") # the // between blockes of text
    if "panties" in action.lower():
        print(part_1_search_room(input("// baka..\n// Search for anything else?\n// ")))
    else:
        print(part_1_search_room(input("// Cant find anything like this in here\n// Search for anything else?\n// ")))

def part_1_stay_in_room(action):
    print("\n////////////////////////////////////////////////////////////////////Part-01//\n") # the // between blockes of text
    if "search" in action.lower():
        print(part_1_search_room(input("// Search for what?\n// ")))
    elif "jump" and "window" in action.lower():
        print(part_1_stay_in_room(input("// ok...let's not do that.\n// Action: ")))
    else:
        print(part_1_stay_in_room(input("// Nah, dont feel like doing that\n// Action: ")))

def part_1_after_mother(action):
    print("\n////////////////////////////////////////////////////////////////////Part-01//\n") # the // between blockes of text
    if "stay" in action.lower():
        print("''sure sweety, you can stay for a while but hurry up so we wont miss dad''")
        print(part_1_stay_in_room(input("\n// you stayed in the room, what would you do now?\n// Action: ")))
    elif "hello" in action.lower():
        print(part_1_after_mother(input("''are you ready to leave?''\n// Action: ")))
    elif "love" in action.lower():
        print(part_1_after_mother(input("''Ohhh, thank you my love, are you ready to leave?''\n// Action: ")))
    elif "yes" in action.lower():
        print("// You left the room with your mother\n")
        part_2_the_docks()
    elif "no" in action.lower():
        print("''sure sweety, you can stay for a while but hurry up so we wont miss dad''")
        print(part_1_stay_in_room(input("\n// you stayed in the room, what would you do now?\n// Action: ")))
    elif "leave" in action.lower():
        print("// You left the room with your mother\n")
        part_2_the_docks()
    elif "said" in action.lower():
        print(part_1_after_mother(input("// Cant say that\n// Action: ")))
    elif "told" in action.lower():
        print(part_1_after_mother(input("// Cant say that\n// Action: ")))
    else:
        print(part_1_after_mother(input("// Cant do that\n// Action: ")))

def part_1_mother_talk():
    print("////////////////////////////////////////////////////////////////////Part-01//\n") # the // between blockes of text
    print("''hello my dear, I hope you slept well,")
    print("  today we are going to the dockes to greet your father,")
    print("  he came back from he's travel to africa, i wonder,")
    print("  what kind of things will he bring us this time?''")
    print("\n////////////////////////////////////////////////////////////////////Part-01//\n") # the // between blockes of text
    print(part_1_after_mother(input("// What do you want to do now?\n// Action: ")))

def part_1_open_door(action, num):
    knock_count = num
    print("\n////////////////////////////////////////////////////////////////////Part-01//\n") # the // between blockes of text
    if "open" in action.lower():
        print("// You open the door and you see you mother.\n")
        part_1_mother_talk()
    elif "answer" in action.lower():
        print("// You open the door and you see you mother.\n")
        part_1_mother_talk()
    elif knock_count > 1:
        print("// You hear the door key hole twist and the door open")
        print("// (Apperently she had a spare key...)")
        print("// The door opens and you see you mother.\n")
        part_1_mother_talk()
    elif knock_count > 0:
        print(part_1_open_door(input("// you hear from outside\n''It's me, your mother, please open the door''\n\n// What to do now?\n// Action: "),knock_count + 1))
    elif "dont" in action.lower():
        print(part_1_open_door(input("// The person outside the door knock again.\n// What to do?\n// Action: "),knock_count + 1))
    elif "do not" in action.lower():
        print(part_1_open_door(input("// The person outside the door knock again.\n// What to do?\n// Action: "),knock_count + 1))
    elif "keep looking" in action.lower():
        print(part_1_open_door(input("// The view look very nice\n// The person outside the door knock again.\n// What to do?\n// Action: "),knock_count + 1))
    elif "keep staring" in action.lower():
        print(part_1_open_door(input("// The view look very nice\n// The person outside the door knock again.\n// What to do?\n// Action: "),knock_count + 1))
    elif "jump" in action.lower():
        print(part_1_open_door(input("// Yeah, let's not do that..\n// Action: "),knock_count))
    elif "who" or "ask" in action.lower():
        print(part_1_open_door(input("// No answer, it's knocking again\n// Action: "),knock_count + 1))
    else:
        print(part_1_open_door(input("// The person outside the door knock again.\n// What to do?\n// Action: "),knock_count + 1))

# Story: 

print("// Welcome to the first text based game:")
print(input("// Would you like to start A new game?\n// Press Enter: "))

print("////////////////////////////////////////////////////////////////////Part-01//\n") # the // between blockes of text

print("''it's the first day of summer, you, a black haired little girl,")
print("  stare out of the window of your room, outside you can see the open,")
print("  the seagulls are flying low above the tall ships that are in the bay.''")
print(part_1_open_door(input("\n// You hear someone knocking on the door,\n// what to do?\n// Action: "),0))


input("Press 'Enter' to exit")