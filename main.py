# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
is_off = False

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

amtPaid = 0

coins = {'quarter': 0.50, 'dime': 0.10, 'penny': 0.01, 'nickel': 0.05}


def get_cost(option):
    """Returns the total cost of an option"""
    return MENU[option]['cost']


def get_coin_price(option):
    return coins[option]


def handle_input():
    """Manages input to the coffee maker machine"""
    option = input("What would you like?(express/latte/cappuccino):  ")
    if option in MENU.keys():
        is_enough = check_resources(option)
        if is_enough:
            get_money(option)
        else:
            print(f"Not enough resources to prepare {option}")

    elif option == "off":
        global is_off
        is_off = True
    elif option == "report":
        generate()
    else:
        print("Invalid entry entered.")


def check_resources(option):
    """Checks if there are enough resources available to prepare the option"""
    ingredients = MENU[option]['ingredients']
    num = 0
    if ingredients['water'] > resources['water']:
        num += 1
    if ingredients['milk'] > resources['milk']:
        num += 1
    if ingredients['coffee'] > resources['coffee']:
        num += 1

    if num > 0:
        return False
    else:
        return True


def get_money(option):
    """Gets the money needed for the coffee"""
    print("Please enter the quantity of coins you have:")
    entered_coins = []
    total = 0
    for coin in coins:
        qty = int(input(f"{coin} : "))
        coin_price = get_coin_price(coin)
        t_coin_price = qty * coin_price
        coin_quantity = {'coin': coin, 'qty': qty, 'cost': coin_price, 'total': "{0:.2f}".format(t_coin_price)}
        total += t_coin_price
        entered_coins.append(coin_quantity)

    print(entered_coins)
    total = "{0:.2f}".format(total)
    item_cost = "{0:.2f}".format(get_cost(option))
    print(f"The total entered is "+total+f" and the {option} costs: {item_cost}")
    difference = float(total) - float(item_cost)


def generate():
    """Generate report on resources left in machine"""
    print("The report is show below:")
    for resource in resources:
        print(resource.title() + "\t" + str(resources[resource]))
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    handle_input()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
