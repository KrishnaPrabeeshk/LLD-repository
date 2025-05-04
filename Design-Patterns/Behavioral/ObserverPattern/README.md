# Observer Design Pattern

The **Observer Design Pattern** is a behavioral design pattern that defines a **one-to-many dependency** between objects. When one object (the **subject**) changes state, all its **observers** are automatically notified and updated.

## Why do we need this? 🤔
- Imagine a **news agency** 📡 that sends real-time updates to multiple **news channels**.

- Without the observer pattern, the agency would have to manually notify each channel — making the system **tightly coupled** and hard to extend.

- With Observer, channels (observers) **subscribe** to the agency (subject), and get updates **automatically** when news is published.

- This promotes **loose coupling**, **event-driven communication**, and adheres to **SOLID principles** (especially Open/Closed and Dependency Inversion).


## Examples 

- **Social Media Notifications** 🔔 – When someone posts, all followers get notified.

- **Stock Market Dashboards** 📈 – Price changes are pushed to all subscribed views.

- **Weather Apps** 🌦️ – Real-time weather changes trigger updates across devices.

- **Auction Systems** 🛎️ – All bidders are alerted when a new bid is placed.

- **Messaging Apps** 💬 – New messages notify all active chat windows.

## Implementation 🛠️
The `newsagency.py` file demonstrates how different NewsChannel observers can subscribe to a NewsAgency and receive updates only for topics they care about.