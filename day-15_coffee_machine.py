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
coffee_options=["cappuccino", "espresso", "latte"]

def report(cash):
    """Provides report on the current state of resources & money"""
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f"Money: ${round(cash,2)}")

def is_enough(drink):
    """Checks if there is enough resources to make a chosen drink"""
    for product in drink["ingredients"]:
        if drink["ingredients"][product]>resources[product]:
            print(f"Sorry, there is not enough {product}.")
            return False
    return True

def paying(coffee_type):
    """Function responsible for paying - returns True if the payment was accepted"""
    print("Please insert coins.")
    quarters=int(input("How many quarters?: "))
    dimes=int(input("How many dimes?: "))
    nickles=int(input("How many nickles?: "))
    pence=int(input("How many pence?: "))
    inserted_money=0.25*quarters+0.10*dimes+0.05*nickles+0.01*pence

    if inserted_money>=MENU[coffee_type]["cost"]:
        print(f'Here\'s your {round(inserted_money-MENU[coffee_type]["cost"], 2)}$ in change.')
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(coffee_type, resources):
    """Making coffee of chosen type"""
    for product in MENU[coffee_type]["ingredients"]:
        resources[product]-=MENU[coffee_type]["ingredients"][product]
    return resources

def ordering(cash):
    coffee_type=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_type=="off":
        return
    elif coffee_type=="report":
        report(cash)
    elif coffee_type in coffee_options:
        if is_enough(MENU[coffee_type]) and paying(coffee_type):
            make_coffee(coffee_type, resources)
            cash+=MENU[coffee_type]["cost"]
            print(f"Here is your {coffee_type} ☕. Enjoy!")
    else:
        print("Invalid choice. Try again.")
    ordering(cash)


ordering(cash=0)