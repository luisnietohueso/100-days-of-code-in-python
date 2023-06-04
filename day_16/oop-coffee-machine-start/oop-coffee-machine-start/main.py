from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    off = True
    while off:
        money_machine = MoneyMachine()
        coffee_maker = CoffeeMaker()
        menu = Menu()
        items = menu.get_items()
        print(items)
        coffe = input('What would you like? (espresso/latte/cappuccino/): ')
        if coffe == 'report':
            print(coffee_maker.report())
            print(money_machine.report())
        elif coffe == 'off':
            print('Machine off')
            off = False
        drink = menu.find_drink(coffe)
        if drink:
            # Check if the resources are sufficient
            if coffee_maker.is_resource_sufficient(drink):
                # Process the payment
                cost = drink.cost
                print(cost)
                payment_accepted = money_machine.make_payment(cost)
                if payment_accepted:
                    # Make the coffee
                    coffee_maker.make_coffee(drink)



main()

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        money_machine.process_coins()
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
