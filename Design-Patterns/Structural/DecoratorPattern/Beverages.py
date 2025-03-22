from abc import ABC, abstractmethod

class Beverage(ABC):

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

class Coffee(Beverage):
    def cost(self):
        return 5
    def description(self):
        return "Plain Coffee"

class AddOnDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

class Milk(AddOnDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)
    def cost(self):
        return self.beverage.cost() + 2
    def description(self):
        return self.beverage.description() + " with Milk"

class Sugar(AddOnDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)
    def cost(self):
        return self.beverage.cost() + 1
    def description(self):
        return self.beverage.description() + " with Sugar"

class WhippedCream(AddOnDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)
    def cost(self):
        return self.beverage.cost() + 2.5
    def description(self):
        return self.beverage.description() + " with Whipped Cream"

class ChocolateSyrup(AddOnDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)
    def cost(self):
        return self.beverage.cost() + 2
    def description(self):
        return self.beverage.description() + " with Chocolate Syrup"

class Discount(AddOnDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)
    
    def cost(self):
        return self.beverage.cost() * 0.9
    
    def description(self):
        return self.beverage.description() + " with Discount of 10%"


coffee = Coffee()
print(f"{coffee.description()} - ${coffee.cost()}")

coffee_with_milk = Milk(coffee)
print(f"{coffee_with_milk.description()} - ${coffee_with_milk.cost()}")

coffee_with_milk_sugar = Sugar(coffee_with_milk)
print(f"{coffee_with_milk_sugar.description()} - ${coffee_with_milk_sugar.cost()}")

coffee_with_milk_sugar_whipped_cream = WhippedCream(coffee_with_milk_sugar)
print(f"{coffee_with_milk_sugar_whipped_cream.description()} - ${coffee_with_milk_sugar_whipped_cream.cost()}")

coffee_with_milk_sugar_whipped_cream_chocolate_syrup = ChocolateSyrup(coffee_with_milk_sugar_whipped_cream)
print(f"{coffee_with_milk_sugar_whipped_cream_chocolate_syrup.description()} - ${coffee_with_milk_sugar_whipped_cream_chocolate_syrup.cost()}")

coffee_with_milk_sugar_whipped_cream_discounted = Discount(coffee_with_milk_sugar_whipped_cream)
print(f"{coffee_with_milk_sugar_whipped_cream_discounted.description()} - ${coffee_with_milk_sugar_whipped_cream_discounted.cost()}")
