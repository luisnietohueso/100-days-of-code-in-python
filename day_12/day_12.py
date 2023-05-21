import random
print('Welcome to the Number Guessing Game')
print('I am thinking of a number between 1 and 100')

count_easy = 10
count_hard = 5

def play_game():
    choose = random.randint(1, 100)
    lives = 0

    difficulty = input('Choose a difficulty level. Type "easy" or "hard": ')
    if difficulty == 'easy':
        lives = count_easy 
        print(f"You have {lives} attempts")
    elif difficulty == 'hard':
        lives = count_hard
        print(f"You have {lives} attempts")
    else:
        print('Invalid input. Try again.')
        return

    while lives > 0:
        guess = int(input('Make a guess: '))

        if guess == choose:
            print(f'You got it! The answer was {choose}.')
            return
        elif guess > choose:
            lives -= 1 
            print('Too high.')
            print(f"You have {lives} attempts left.")
        elif guess < choose: 
            lives -= 1 
            print('Too low.')
            print(f"You have {lives} attempts left.")
    
    print(f"You have run out of attempts. The answer was {choose}. Game over.")

play_game()







