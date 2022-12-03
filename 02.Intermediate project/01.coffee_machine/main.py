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


def check_resource_sufficient(order_ingredient):
  for item in order_ingredient:
    if resources[item] < order_ingredient[item]:
      print(f"Sorry there is not enough {item}")
      return False
  return True


def process_coins():
  print("please insert coins")
  coins = int(input("How many quarters: ")) * 0.25
  coins += int(input("How many dimes: ")) * 0.10
  coins += int(input("How many nickles: ")) * 0.05
  coins += int(input("How many pennis: ")) * 0.01
  return coins


def transaction(cost_coin, drink_cost):
  if cost_coin < drink_cost:
    print("Sorry you don't have enough money")
    return False
  elif cost_coin > drink_cost:
    change = round(cost_coin - drink_cost, 2)
    print(f"Here is your ${change}")
    global profit
    profit += drink_cost
    return True


def make_coffee(drink, order_ingredient):
  for item in order_ingredient:
    resources[item] -= order_ingredient[item]
  print(f"Here is your {drink}")


is_on = True

while is_on:
  choice = input("What would you like? (espresso/latte/cappuccino): ")
  if choice == "off":
    is_on = False
  elif choice == "report":
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")
  else:
    drink = MENU[choice]
    ingredients = drink["ingredients"]
    if check_resource_sufficient(drink['ingredients']):
      payment = process_coins()
      if transaction(payment, drink['cost']):
        make_coffee(choice, ingredients)
