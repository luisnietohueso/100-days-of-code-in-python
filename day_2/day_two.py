def sum():
    two_digit_number = input("Type a two digit number: ")
    result = int(two_digit_number[0]) + int(two_digit_number[1])
    print(result)


def bmi():
    height = input("Enter your height in meters: ")
    weight = input("Enter your weight in kilograms: ")
    BMI = float(weight) / (float(height) ** 2)
    print("Your BMI is: ", round(BMI, 1))


def age():
    age = input("What is your current age? ")
    new_age = 90 - int(age)
    days = new_age * 365
    weeks = new_age * 52
    months = new_age * 12
    print(f"You have {days} days, {weeks} weeks, and {months} months left until you turn 90.")


def Tip_Calculator():
    bill = float(input("What was the total bill? $"))
    tip_percentage = float(input("What percentage tip would you like to give? "))
    num_people = int(input("How many people to split the bill? "))

    tip_amount = (bill * tip_percentage) / 100
    total_amount = bill + tip_amount
    amount_per_person = total_amount / num_people

    print(f"Each person should pay: ${round(amount_per_person, 2)}")
    print(f"The total tip amount is: ${round(tip_amount, 2)}")


def main():
    print("Welcome to the Health Calculator!\n")

    while True:
        print("Please select an option:")
        print("1. Calculate the sum of a two-digit number")
        print("2. Calculate BMI")
        print("3. Calculate how many days, weeks, and months until turning 90")
        print("4. Calculate the bill and tip for a group of people")
        print("5. Quit\n")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            sum()
        elif choice == '2':
            bmi()
        elif choice == '3':
            age()
        elif choice == '4':
            Tip_Calculator()
        elif choice == '5':
            print("Thank you for using the Health Calculator!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.\n")


if __name__ == "__main__":
    main()
