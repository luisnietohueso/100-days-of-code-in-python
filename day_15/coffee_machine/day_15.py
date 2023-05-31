"""
day of today I will create a virtual coffe machine
"""
from optionCoffee import resources, MENU


def off_on():
    """Function to turn on/off the coffee machine."""
    while True:
        on = input('Do you want to turn on the machine? Enter Yes or No: ')
        if on.lower() == 'yes':
            make_coffee()
            return False
        elif on.lower() == 'no':
            print('Thanks for using this machine.')
            return False
        else:
            print('Invalid input. Please enter Yes or No.')


def report():
    """Function to display the current resources and offer to top up."""

    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    top_up = input('Do you want to top up resources? (yes/no) ')
    if top_up == 'yes':
        resources['water'] = 300
        resources['milk'] = 200
        resources['coffee'] = 100
        print("Resources topped up!")
    else:
        print('thanks for check')


def cost(item_name):
    """Function to return the cost of a drink."""

    return MENU[item_name]['cost']


def prepare_coffee(coffee_type):
    ingredients = MENU[coffee_type]['ingredients']
    for ingredient, amount in ingredients.items():
        # Subtract the amount of each ingredient needed to make the coffee
        resources[ingredient] -= amount
    print(f"Your {coffee_type} is Ready Enjoy.!")


def pay(item):
    """Function to process payment for a drink."""

    to_pay = MENU[item]['cost']
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    while True:
        m_quarters = float(input('how many quarter?'))
        m_dimes = float(input('how many dimes?'))
        m_nickles = float(input('how many nickles?'))
        m_pennies = float(input('how many pennies?'))
        total_quarter = quarters * m_quarters
        total_dimes = dimes * m_dimes
        total_nickles = nickles * m_nickles
        total_pennies = pennies * m_pennies
        total = total_pennies + total_dimes + total_nickles + total_quarter
        if total == to_pay:
            print('your payment was successful!')
            prepare_coffee(item)
            break
        elif total > to_pay:
            refund = total - to_pay
            print(f'your payment was successful!This is your change:{refund}!')
            prepare_coffee(item)
            break
        else:
            print('no enough money! your money is back.')


def check_resources(item):
    """Function to check if there are enough resources to make the selected drink."""

    while True:
        ingredients = MENU[item]['ingredients']
        for ingredient, amount in ingredients.items():
            if resources[ingredient] < amount:
                print('no enough ingredients sorry for the inconveniences!')
                return False
            elif resources[ingredient] >= amount:
                pay(item)
                return False
            else:
                print('invalid option try again')


def make_coffee():
    while True:
        start = input('Which of the following coffees do you want: 1. Espresso, 2. Latte, 3. Cappuccino, 4. Turn off? ')
        if start == '1' or start == 'espresso':
            print(f"For espresso, the cost is: {cost('espresso')}")
            check_resources('espresso')
        elif start == '2' or start == 'latte':
            print(f"For latte, the cost is: {cost('latte')}")
            check_resources('latte')
        elif start == '3' or start == 'cappuccino':
            cost('cappuccino')
            check_resources('cappuccino')
        elif start == '4' or start == 'off':
            print(f"For cappuccino, the cost is: {cost('cappuccino')}")
            print('This machine is off.')
            return False
        elif start == '5' or start == 'report':
            report()
            continue
        else:
            print('Invalid input.')
            continue


off_on()
