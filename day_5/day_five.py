import random
def student():
    student_heights = input("Input a list of student heights ").split()
    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])

    total_height = 0
    for height in student_heights:
        total_height += height
    print(f"total height = {total_height}")

    number_of_students = 0
    for student in student_heights:
        number_of_students += 1
    print(f"number of students = {number_of_students}")
    
    average_height = round(total_height / number_of_students)
    print(average_height)
def high_score():
    student_scores = input("Input a list of student scores ").split()
    for n in range(0, len(student_scores)):
        student_scores[n] = int(student_scores[n])
        print(student_scores)

    the_max_score = 0 
    for scores in student_scores:
        if scores > the_max_score:
            the_max_score = scores  

    print(f'The highest score in the class is: {the_max_score}')
def add():
    n = 0 
    for s in range(1, 101):
        if(s % 2 == 0):
            n += s
    print(n)


def FizzBuzz():
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0: 
            print('FizzBuzz')
        elif number % 5 == 0:
            print('Buzz')
        elif number % 3 == 0:
            print('Fizz')
        else:
            print(number)
    print(number)

def password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    password = ''
    for letra in range(1,nr_letters+1):
        letra = random.choice(letters)
        password += letra 
    symbol = ''
    for x in range(1,nr_symbols+1):
        x = random.choice(symbols)
        symbol += x 
    numb = ''
    for n in range(1, nr_numbers+1):
        n = random.choice(numbers)
        numb += n 
        
    end = numb + symbol + password
    print(f'Your password will be: {end}')

def menu():
    while True:
        print("Please choose an option:")
        print("1. Calculate average height of students")
        print("2. Find the highest score in the class")
        print("3. Add even numbers from 1 to 100")
        print("4. Play FizzBuzz game")
        print("5. Generate a password")
        print("6. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            student()
        elif choice == "2":
            high_score()
        elif choice == "3":
            add()
        elif choice == "4":
            FizzBuzz()
        elif choice == "5":
            password()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

menu()