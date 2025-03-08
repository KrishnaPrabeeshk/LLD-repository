##Singleton Design Pattern

This pattern is mainly used when only one instance of a class should exist throughout the lifecycle of an application

#Examples

-🔧 Configuration Manager: A class that loads app settings from a config file and ensures that the same settings are used throughout the program.

-🗄️ Database Connection Manager: Ensures that all parts of the application share a single database connection instead of creating multiple connections.

-📝 Logger (Logging System):A logging service that ensures all logs go to a single file or console instance.

-🌍 Caching System: A cache that stores frequently accessed data so that every part of the app uses the same cache instance.

#Implementation
For example look at the Database.py file where I implemented a Database Connection Manager which ensures that all parts of the application share a single database connection instead of creating multiple connections.
