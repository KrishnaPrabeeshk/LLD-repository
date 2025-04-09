# Strategy Design Pattern

The **Strategy Design Pattern** is a behavioral design pattern that enables selecting an algorithm’s behavior at runtime by encapsulating each algorithm in a separate class.

## Why do we need this? 🤔
- Imagine a **Duck Simulator** 🦆 that models different ducks with varying **fly** and **quack** behaviors.
- Hardcoding behaviors into the duck class leads to **rigid**, **inflexible** code.
- Instead, we can **encapsulate behaviors** (like flying and quacking) into **interchangeable strategy classes**.
- This allows us to **change behaviors at runtime** without modifying the `Duck` class.
- The pattern also promotes **code reuse**, **clean separation of concerns**, and adherence to **SOLID principles** (especially the Open/Closed Principle).

## Examples 
- **Navigation App 🗺️** – Users can switch between fastest, shortest, and scenic routes.
- **Payment System 💳** – Different payment strategies: credit card, PayPal, cryptocurrency.
- **Sorting Algorithms 🔢** – Strategy swaps between bubble sort, quick sort, merge sort.
- **Compression Utilities 📦** – Choose between ZIP, RAR, or 7z at runtime.
- **Character Behavior in Games 🎮** – AI characters can change strategy: attack, defend, flee.

## Implementation 🛠️
The `duckbehavior.py` file demonstrates how the Strategy Pattern allows ducks to change their **fly** and **quack** behaviors dynamically:
- `FlyBehavior` and `QuackBehavior` are strategy interfaces.
- Ducks use these behaviors via composition.
- Behaviors can be changed at runtime using setter methods.
- Examples include:
  - `FlyWithWings`, `FlyNoWay`, `FlyRocketPowered`
  - `Quack`, `Squeak`, `Mute`

This approach results in **flexible**, **maintainable**, and **extensible** code—exactly what you want when your ducks start demanding jetpacks.
