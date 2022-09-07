from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
cashier = MoneyMachine()
is_working = True

while is_working != False:
    order = input(f"What would you like? {menu.get_items()}")
    if order == "report":
        coffee_machine.report()
        cashier.report()
    elif order == "off":
        is_working = False
    elif order == "latte" or "espresso" or "cappuccino":
        drink = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink) == True:
            if cashier.make_payment(drink.cost) == True:
                coffee_machine.make_coffee(drink)
