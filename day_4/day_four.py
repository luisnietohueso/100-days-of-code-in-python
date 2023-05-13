import random
def flip():
    Flip_the_coin = random.randint(0,1)
    if Flip_the_coin == 0:
        print('Tails')
    else:
        print('Heads')
def name():
    names_string = input("Give me everybody's names, separated by a comma. ")
    names = names_string.split(", ")
    #Get the total number of items in list.
    num_items = len(names)
    #Generate random numbers between 0 and the last index. 
    random_choice = random.randint(0, num_items - 1)
    #Pick out random person from list of names using the random number.
    person_who_will_pay = names[random_choice]

    print(person_who_will_pay + " is going to buy the meal today!")
def Treasure_Map():
    row1 = ["⬜️","️⬜️","️⬜️"]
    row2 = ["⬜️","⬜️","️⬜️"]
    row3 = ["⬜️️","⬜️️","⬜️️"]
    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    position = input("Where do you want to put the treasure? ")
    horizontal = int(position[0])
    vertical = int(position[1])
    map[vertical - 1][horizontal - 1] = "X"
    print(f"{row1}\n{row2}\n{row3}")

def  Rock_Paper_Scissors():
    
    computer_choices = ['Rock', 'Paper', 'Scissors']
    play_again = True

    while play_again:
        human_choice = int(input("Choose your move: 0 for Rock, 1 for Paper, 2 for Scissors: "))
        computer_choice = random.randint(0, 2)
        
        if human_choice == computer_choice:
            print(f"The computer chose {computer_choices[computer_choice]} and you chose {human_choice}, it's a draw!")
        elif human_choice == 0 and computer_choice == 1:
            print(f"The computer chose {computer_choices[computer_choice]} and you chose {human_choice}, you lose!")
        elif human_choice == 0 and computer_choice == 2:
            print(f"The computer chose {computer_choices[computer_choice]} and you chose {human_choice}, you win!")
        elif human_choice == 1 and computer_choice == 0:
            print(f"The computer chose {computer_choices[computer_choice]} and you chose {human_choice}, you win!")
        elif human_choice == 1 and computer_choice == 2:
            print(f"The computer chose {computer_choices[computer_choice]} and you chose {human_choice}, you lose!")
        elif human_choice == 2 and computer_choice == 0:
            print(f"The computer chose {computer_choices[computer_choice]} and you chose {human_choice}, you lose!")
        elif human_choice == 2 and computer_choice == 1:
            print(f"The computer chose {computer_choices[computer_choice]} and you chose {human_choice}, you win!")
        
        play_again = input('Do you want to play again? (Y/N) ') == 'Y'

print('Thanks for playing!')
# All your functions go here (flip, name, Treasure_Map, Rock_Paper_Scissors)

def main_menu():
    print("Welcome to the Game Collection!")
    print("Please choose a game to play:")
    print("1. Flip a Coin")
    print("2. Who Will Pay?")
    print("3. Treasure Map")
    print("4. Rock, Paper, Scissors")
    print("5. Quit")

    game_choice = int(input("Enter the number of your choice: "))

    if game_choice == 1:
        flip()
    elif game_choice == 2:
        name()
    elif game_choice == 3:
        Treasure_Map()
    elif game_choice == 4:
        Rock_Paper_Scissors()
    elif game_choice == 5:
        print("Thanks for playing!")
        return
    else:
        print("Invalid choice. Please choose a valid option.")
 
 
 # Call the main menu again to allow the user to choose another game or quit
main_menu()