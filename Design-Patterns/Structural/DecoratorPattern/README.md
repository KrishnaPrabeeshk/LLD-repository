# Decorator Design Pattern

The **Decorator Design Pattern** is used to **dynamically add** behavior or responsibilities to an object **without modifying its structure**. It provides a flexible alternative to subclassing for extending functionality.

## Why do we need this? 🤔

- Imagine programming a coffee machine, Initially it is just a coffee so, we create a class for this called Coffee.

- Later we are told that we need to have milk as an add on so we write another sub class for it called CoffeeWithMilk.

- Later we are told that we need to have Sugar, Whipped Cream, Chocolate Syrup creating a sub class for every add on is not ideal

- Instead of creating new subclasses for every possible combination (e.g., CoffeeWithMilk, CoffeeWithSugarAndMilk), we use decorators to add features dynamically.

- This allows us to extend behavior without modifying existing code, making it flexible and scalable.

- Say we want to add a discount on top of any type of beverage. With these decorators we can do so easily

## Difference between this and Builder Design Pattern? 🤨

- The Decorator Pattern and Builder Pattern may seem similar because they both involve customization, but they serve different purposes.

- **🏗️ Builder Pattern** (Step-by-Step Construction)  
  - Think of it like **ordering a custom burger** 🍔 – you pick each ingredient **before** the burger is made.  
  - The **final object** (e.g., a burger) is assembled **once at the end**.  

- **🎨 Decorator Pattern** (Dynamic Enhancements)  
  - Used to **dynamically add features** to an object **at runtime**.  
  - Think of it like **adding extra toppings to your coffee** ☕ – you can **keep adding** new flavors even after the coffee is made.  
  - The **base object remains the same**, but it **keeps getting enhanced** with new features.  

- You can use these both **together** for a burger, 
- For example, once you build your burger with **Builder pattern**
- you can **add** Ketch up on top using **Decorator pattern**

## Implementation
I have implemented the **Coffee Customization** example discussed above to show how convenient the **Decorator Pattern** is. In the code, you’ll see that:

- **Without the Decorator Pattern**, we would need to create multiple subclasses for every combination of coffee (e.g., CoffeeWithMilk, CoffeeWithSugarAndMilk).

- **With the Decorator Pattern**, we can dynamically wrap a coffee object with decorators (Milk, Sugar, etc.), adding behavior at runtime without modifying the original coffee class.

