# Builder Design Pattern

The Builder Design Pattern is a creational pattern used to construct complex objects step by step. Instead of creating an object all at once, it allows for a flexible and readable construction process, especially when objects have many optional and mandatory attributes.


## Why do we need this? 🤔

-  Without the Builder Pattern, customizing a burger with many optional ingredients might look something like this: Burger("Sesame Bun", "Veg Patty", cheese=True, lettuce=True, tomato=True, sauce=True)

- With the Builder Pattern, it would look like this: BurgerBuilder().add_cheese().add_lettuce().add_tomato().add_sauce().build()

- the second one clearly sounds like we are complicating stuff than keeping it simple like in the first step. So, why do we need it?

- We would be right in thinking so but, If our class starts having many optional parameters, our constructor could become quite large and hard to manage. 

- With the Builder Pattern, we avoid the need to define constructors with numerous parameters, many of which might be None by default. This leads to cleaner code.

- The Builder Pattern also provides a way to customize the construction of objects depending on conditions. 

- For example, if we wanted to impose some logic (like disallowing certain combinations of ingredients), the builder class can enforce that, whereas the constructor approach would require a complicated logic

## Examples

- 🍔 Custom Burger Construction: Dynamically create custom burgers with mandatory ingredients (bun, patty) and optional ingredients (cheese, lettuce, tomato, etc.) in a step-by-step process.
- 🍽️ Meal Preparation: Helps in constructing complex meals (e.g., pizzas, sandwiches) with various toppings, sides, and sauces by adding each component step by step.
- 🚗 Car Assembly: In an automobile factory, various car models with different configurations (e.g., sunroof, sports wheels, etc.) can be assembled by adding components progressively.
- 📦 Package Delivery: For a delivery service, different types of packages (light, heavy, fragile) can be constructed step by step by adding the appropriate shipping components (e.g., box type, padding, etc.).

## Implementation

Check out the withoutBuilderPattern and withBuilderPattern files to see a clear before-and-after comparison of how the Builder Design Pattern improves the code structure, readability, and flexibility.

## Difference between Builder Design Pattern and Factory Design Pattern

I personally found these both quite similar to each other and started 🕵️ for how these both are different. What my understanding is:
- While these both are providing a convienient way for the user to create different user types (in case of factory design pattern) or create different kinds of burgers (in case of Builder Design pattern)
- Factory Pattern: Focuses on creating different types of objects (e.g., creating a Librarian, Member, Admin). It's useful when objects have distinct roles but do not require deep customization.
- Builder Pattern: Focuses on customizing the attributes of a specific object (e.g., creating a Librarian with a specific hairstyle, wearing glasses, sitting at a desk).
- In short, the Factory Pattern creates object types at a high level, while the Builder Pattern customizes the attributes of those objects in detail.
