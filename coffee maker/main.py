from resources import MENU, resources

machine_is_working = True
profit = 0


def resources_enough(a, b):
    if MENU[a]["ingredients"]["water"] >= b["water"]:
        return 0
    elif MENU[a]["ingredients"]["milk"] >= b["milk"]:
        return 1
    elif MENU[a]["ingredients"]["coffee"] >= b["coffee"]:
        return 2
    else:
        return 3


def resources_new(a, b):
    milk = b["water"] - MENU[a]["ingredients"]["water"]
    water = b["milk"] - MENU[a]["ingredients"]["milk"]
    coffee = b["coffee"] - MENU[a]["ingredients"]["coffee"]
    return milk, water, coffee


def total_money(a, b, c, d):
    Total = a * 0.25 + b * 0.10 + c * 0.05 + d * 0.01
    return Total


def change(a, b):
    changes = b - MENU[a]["cost"]
    print(f"Here is ${changes} in change")
    print(f"Here is your {a} ☕️. Enjoy!")


while machine_is_working != False:
    orders = input('What would you like? (espresso/latte/cappuccino): ')
    if orders == "report":
        print(resources)
        print(f"Money: ${profit}")
    elif orders == "off":
        print("Machine Turning Off ")
        break
    elif orders == "espresso" or "latte" or "cappuccino":
        contd = resources_enough(orders, resources)
        if contd == 0:
            print("Sorry there is not enough water.")
        if contd == 1:
            print("Sorry there is not enough milk.")
        if contd == 2:
            print("Sorry there is not enough coffee.")
        if contd == 3:
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            all_money = total_money(quarters, dimes, nickles, pennies)
            if all_money < MENU[orders]["cost"]:
                print("Money not enough")
            elif all_money >= MENU[orders]["cost"]:
                change(orders, all_money)
                profit += MENU[orders]["cost"]
                milk, water, coffee = resources_new(orders, resources)
                resources["water"] = water
                resources["milk"] = milk
                resources["coffee"] = coffee
