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


def get_cost(option):
    """Returns the total cost of an option"""
    return MENU[option]['cost']


def handle_input():
    """Manages input to the coffee maker machine"""
    option = input("What would you like?(express/latte/cappuccino")
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


def generate():
    """Generate report on resources left in machine"""
    print("The report is show below:")
    for resource in resources:
        print(resource.title() + "\t"+str(resources[resource]))
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    handle_input()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
