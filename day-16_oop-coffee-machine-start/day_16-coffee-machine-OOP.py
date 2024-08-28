from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffee_machine=CoffeeMaker()
money_machine=MoneyMachine()

is_on=True

while is_on==True:
    drink=input(f"What would you like? {menu.get_items()}\b: ")
    if drink=="report":
        #CoffeeMaker.report(our_coffee_machine)
        coffee_machine.report()
        money_machine.report()
    elif drink=="off":
        is_on=False
    else:
        if menu.find_drink(drink):
            choice=menu.find_drink(drink)
            if coffee_machine.is_resource_sufficient(choice) and money_machine.make_payment(choice.cost):
                coffee_machine.make_coffee(choice)

