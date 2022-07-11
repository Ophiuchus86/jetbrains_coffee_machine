# Solution a bit more complex that it could be, but I tried to write reusable code
from collections import namedtuple


Unit = namedtuple("Unit", "long short")
ml = Unit("ml", "ml")
grams = Unit("grams", "g")

Ingredient = namedtuple("Ingredient", "name unit")
water = Ingredient("water", ml)
milk = Ingredient("milk", ml)
coffee_beans = Ingredient("coffee beans", grams)


class CoffeeMachine:
    def __init__(self, money, cups, supplies, coffee_ingredients):
        self.money = money
        self.cups = cups
        self.supplies = supplies
        self.coffee_ingredients = coffee_ingredients

    def do_command(self, input_):
        match input_:
            case "buy":
                self.buy()
            case "fill":
                self.fill()
            case "take":
                self.take()
            case "remaining":
                self.remaining()

    def remaining(self):
        print("\nThe coffee machine has:")
        for ingredient, amount in self.supplies.items():
            print(f"{amount} {ingredient.unit.short} of {ingredient.name}")
        print(f"{self.cups} disposable cups")
        print(f"${self.money} of money\n")

    def buy(self):
        match input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n"):
            case "1":
                coffee = coffee_ingredients["espresso"]
            case "2":
                coffee = coffee_ingredients["latte"]
            case "3":
                coffee = coffee_ingredients["cappuccino"]
            case _:
                return

        if self.cups <= 0:
            print("Sorry, not enough disposable cups!\n")
            return

        supplies_c = self.supplies.copy()
        for ingredient, amount in coffee["ingredients"].items():
            if self.supplies[ingredient] - amount >= 0:
                self.supplies[ingredient] -= amount
            else:
                print(f"Sorry, not enough {ingredient}!\n")
                self.supplies = supplies_c
                break
        else:
            print("I have enough resources, making you a coffee!\n")
            self.cups -= 1
            self.money += coffee["cost"]

    def fill(self):
        for ingredient in self.supplies.keys():
            add = int(input(f"Write how many {ingredient.unit.long} of {ingredient.name} you want to add:\n"))
            self.supplies[ingredient] += add

        self.cups += int(input("Write how many disposable cups you want to add:\n"))

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0


coffee_ingredients = {
    "espresso": {
        "ingredients": {
            water: 250,
            coffee_beans: 16
        },
        "cost": 4
    },
    "latte": {
        "ingredients": {
            water: 350,
            coffee_beans: 20,
            milk: 75
        },
        "cost": 7
    },
    "cappuccino": {
        "ingredients": {
            water: 200,
            coffee_beans: 12,
            milk: 100
        },
        "cost": 6
    }
}

machine_supplies = {
    water: 400,
    milk: 540,
    coffee_beans: 120,
}


def main():
    machine = CoffeeMachine(550, 9, machine_supplies, coffee_ingredients)
    while (input_ := input("Write action (buy, fill, take, remaining, exit): \n")) != "exit":
        machine.do_command(input_)


if __name__ == "__main__":
    main()
