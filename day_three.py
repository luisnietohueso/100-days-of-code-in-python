def even():
    number = int(input("Which number do you want to check? "))
    if (number %2) :
        print('This is an odd number.')
    else:
        print('This is an even number.')

def bmi():
    height = float(input("enter your height in m: "))
    weight = float(input("enter your weight in kg: "))
    bmi = round(weight / height ** 2)

    if bmi < 18.5:
        print(f"Your BMI is {bmi}, you are underweight.")
    elif bmi < 25:
        print(f"Your BMI is {bmi}, you have a normal weight.")
    elif bmi < 30:
        print(f"Your BMI is {bmi}, you are slightly overweight.")
    elif bmi < 35:
        print(f"Your BMI is {bmi}, you are obese.")
    else:
        print(f"Your BMI is {bmi}, you are clinically obese.")

def leap(): 
    year = int(input("Which year do you want to check? "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
            else:
                print("Not leap year.")
        else:
            print("Leap year.")
    else:
        print("Not leap year.")

def delivery():
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M, or L ")
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    extra_cheese = input("Do you want extra cheese? Y or N ")
    # Initialize variables for pizza price and toppings
    pizza_price = 0
    toppings_price = 0

    # Calculate pizza price based on size
    if size == "S":
        pizza_price = 15
    elif size == "M":
        pizza_price = 20
    elif size == "L":
        pizza_price = 25

    # Calculate toppings price
    if add_pepperoni == "Y":
        if size == "S":
            toppings_price += 2
        else:
            toppings_price += 3

    if extra_cheese == "Y":
        toppings_price += 1

    # Calculate final bill
    total_price = pizza_price + toppings_price

    # Print final bill
    print(f"Your final bill is: ${total_price}.")

def love():
    print("Welcome to the Love Calculator!")
    name1 = input("What is your name? \n")
    name2 = input("What is their name? \n")

    combined_names = name1 + name2
    lower_names = combined_names.lower()
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))

    if (score < 10) or (score > 90):
        print(f"Your score is {score}, you go together like coke and mentos.")
    elif (score >= 40) and (score <= 50):
        print(f"Your score is {score}, you are alright together.")
    else:
        print(f"Your score is {score}.")

def treasure():
    print('''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.") 

    #https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

    # Prompt the player for their choices
    direction = input('You can choose to go left or right: ')
    if direction == 'left':
        waits = input('You can wait or swim: ')
        if waits == 'wait':
            door = input('You can choose between 3 doors: Red, Blue, or Yellow. ')
            if door == 'Yellow':
                print('Congratulations! You found the treasure and won the game!')
            elif door == 'Red':
                print('Burned by fire. Game Over.')
            elif door == 'Blue':
                print('Eaten by beasts. Game Over.')
            else:
                print('Game Over.')
        elif waits == 'swim':
            print('Attacked by trout. Game Over.')
        else:
            print('Game Over.')
    else:
        print('You fall in a hole. Game Over.')

def menu():
    print("Welcome to the menu. Please choose an option:")
    print("1. Check if a number is even or odd")
    print("2. Calculate BMI")
    print("3. Check if a year is a leap year")
    print("4. Calculate pizza delivery cost")
    print("5. Calculate love compatibility")
    print("6. Play Treasure Island game")
    
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        even()
    elif choice == "2":
        bmi()
    elif choice == "3":
        leap()
    elif choice == "4":
        delivery()
    elif choice == "5":
        love()
    elif choice == "6":
        treasure()
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
        menu()
menu()

