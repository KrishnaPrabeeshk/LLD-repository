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


myburger = Burger("Sesame Bun","Veg Patty",cheese=True,lettuce=True,tomato=True)
print(myburger)