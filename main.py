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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?:")) * 0.25
    total += int(input("How many dimes?:")) * 0.1
    total += int(input("How many nickels?:")) * 0.05
    total += int(input("How many pennies?:")) * 0.01
    return total


def transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} is change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredient):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink_name} ☕")
# TODO: 1. Prompt user by asking What would you like? (espresso/latte/cappuccino):
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if choice == "off":
        is_on = False
# TODO: 3. Print report
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
# TODO: 4. Check resources sufficient
    else:
        drink = MENU[choice]
        # print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            # TODO: 5. Process coins
            payment = process_coins()
            # TODO: 6. Check transaction successful
            if transaction_successful(payment, drink["cost"]):
                # TODO: 7. Make Cofffee
                make_coffee(choice, drink["ingredients"])


