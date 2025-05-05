class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "coffee": 100,
            "milk": 200,
        }
    
    def report(self):
        for k, j in self.resources.items():
            print(f"{k}: {j}")
    
    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make
    
    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕. Enjoy!")
