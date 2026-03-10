print("Hello, World!")

print("Welcome to Day 3 - Control Flow and Logical Operators")
# so today is all about making the computer make decisions! 
# basically telling the code "if this happens, do that, otherwise do this"

# ---------------------------------------------------------
# 1. IF / ELSE - The basics
# ---------------------------------------------------------

# Comparison Operators:
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to (remember, = is for assigning variables, == is for checking if they are equal)
# != Not equal to

# Let's try the "Odd or Even" challenge she gives
print("Checking if a number is Odd or Even")
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# ---------------------------------------------------------
# 2. Nested IF and ELIF
# ---------------------------------------------------------

# This is for when you have more than two options. 
# Like the Rollercoaster ticket thing:
print("\nWelcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55: # Added logical operator here for mid-life crisis free tickets lol
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")
        
    # ---------------------------------------------------------
    # 3. Multiple IF statements in succession
    # ---------------------------------------------------------
    # This is different from elif because it checks ALL of them even if one was true
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3 # Adding $3 to the bill
        
    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

# ---------------------------------------------------------
# 4. Pizza Order Challenge
# ---------------------------------------------------------
# I'll try to build this one like you do - thinking about the logic first
print("\nWelcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

pizza_bill = 0

if size == "S":
    pizza_bill += 15
elif size == "M":
    pizza_bill += 20
else:
    pizza_bill += 25

if add_pepperoni == "Y":
    if size == "S":
        pizza_bill += 2
    else:
        pizza_bill += 3

if extra_cheese == "Y":
    pizza_bill += 1

print(f"Your final bill is: ${pizza_bill}.")

# ---------------------------------------------------------
# 5. Logical Operators (AND, OR, NOT)
# ---------------------------------------------------------
# and -> both must be true
# or -> one must be true
# not -> reverses the condition

# The "Love Calculator" project she shows is a bit crazy but fun
print("\nThe Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

combined_names = (name1 + name2).lower()
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")
first_digit = t + r + u + e

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

# ---------------------------------------------------------
# 6. FINAL PROJECT: TREASURE ISLAND
# ---------------------------------------------------------
# This is the big one for Day 3. A text-based adventure game.
# I'm building this from scratch based on the logic she explains.

print('''
*******************************************************************************
          __________
         |  __  __  |
         | |  ||  | |
         | |  ||  | |
         | |__||__| |
         |  __  __  |
         | |  ||  | |
         | |  ||  | |
         | |__||__| |
         |__________|
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")

print("\nDay 3 completed! Decision making is powerful.")

