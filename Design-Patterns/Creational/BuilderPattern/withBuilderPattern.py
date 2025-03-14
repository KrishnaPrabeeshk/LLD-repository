class Burger:
    def __init__(self,bun,patty,cheese=False,lettuce=False,tomato=False,sauce=False):
        self.bun = bun
        self.patty = patty
        self.cheese = cheese
        self.lettuce = lettuce
        self.tomato = tomato
        self.sauce = sauce
    
    def __str__(self):
        ingredients = [self.patty,self.bun]
        
        if self.cheese:
            ingredients.append("Cheese")
        if self.lettuce:
            ingredients.append("Lettuce")
        if self.tomato:
            ingredients.append("Tomato")
        if self.sauce:
            ingredients.append("Sauce")
        
        return f"Burger with: {','.join(ingredients)} "
    
class BurgerBuilder:
    def __init__(self):
        self.burger = Burger("Bun","Patty")
    
    def add_cheese(self):
        self.burger.cheese = True
        return self
    
    def add_lettuce(self):
        self.burger.lettuce = True
        return self

    def add_tomato(self):
        self.burger.tomato = True
        return self

    def add_sauce(self):
        self.burger.sauce = True
        return self

    def build(self):
        return self.burger

# Create a basic burger
basic_burger = BurgerBuilder().build()

# Create a burger with extra cheese and lettuce
deluxe_burger = BurgerBuilder().add_cheese().add_lettuce().build()

# Create a burger with all ingredients
custom_burger = BurgerBuilder().add_cheese().add_lettuce().add_tomato().add_sauce().build()

print(basic_burger)
print(deluxe_burger)
print(custom_burger)