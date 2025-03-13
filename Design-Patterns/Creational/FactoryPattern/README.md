# Factory Design Pattern  

The Factory Design Pattern is a **creational design pattern** used to **encapsulate object creation logic** in a separate method or class. Instead of instantiating objects directly, it provides a way to create objects based on input or conditions dynamically.  

## Motivation  

- ✅ **Decouples object creation** from the main business logic, making the code more modular and maintainable.  
- 🔄 **Provides flexibility** to return different object types based on input without modifying existing code.  
- 🏗️ **Simplifies complex object creation** by centralizing the instantiation logic in one place.  

## When to Use?  

Use the **Factory Pattern** when:  

- You need to create objects **without specifying their exact class**.  
- The **object creation logic is complex** and needs to be centralized.  
- Your system should be **easily extendable** to support new object types without modifying existing code.  

## Examples  

- ✅ **Payment Gateway Integration:** Dynamically creates instances of different payment processors like **PayPal, Stripe, Razorpay, etc.**, based on user selection.  

- 🗄️ **Database Connection Manager:** Helps in switching between different databases (**MySQL, PostgreSQL, MongoDB, etc.**) without modifying the core application logic.  

- 📩 **Notification System:** Allows sending notifications through different channels like **Email, SMS, and Push Notifications**, depending on user preference.  

- 🎨 **Graphic Applications (Shape Creation):** Used in drawing applications to dynamically generate objects like **Circles, Squares, and Rectangles** based on user input.  

## Implementation  

Check out the **`withoutFactoryPattern`** and **`withFactoryPattern`** directories to see a clear **before-and-after comparison** of how the Factory Design Pattern improves code flexibility and maintainability.  
