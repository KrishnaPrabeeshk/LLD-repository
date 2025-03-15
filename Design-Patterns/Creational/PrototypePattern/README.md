# Prototype Design Pattern

The prototype pattern is a creational design pattern used when object creation is costly, and we want to clone existing objects instead of creating new ones from scratch.

## Why do we need this? 🤔

- Imagine making a character in a game you place it somewhere in the environment of the game and all is good.

- But, now you need another character in the game in another place, what you could do is create another character from scratch and place it where required.

- A smart way to do this is, since most characters are the same with a minor changes or major changes on top what would help is have this template of a basic character and build our own character on top.

- This is exactly what we do with Prototype design pattern.

- Instead of creating another object we just clone the existing one and do whatever changes we need on top of it.

- For Obvious reasons this saves us a lot of time.

## Examples

- 🎮 Video Games (Character & Object Cloning): Instead of creating every enemy or item from scratch, games often clone a predefined prototype and make small changes. For example; Spawning multiple enemies with the same base stats but different weapons.

- 📄 Document/Spreadsheet Software (Duplicating Templates): When you "Create a new document from a template", it’s actually cloning a prototype document. For example; Microsoft Word, Google Docs

- 🏭 Manufacturing (Product Blueprints): Factories use a base design (prototype) and modify it for different product variations. For example; Car models that share the same chassis but have different features.

- 🤖 AI & Machine Learning (Pre-trained Models): Instead of training models from scratch, we clone a pre-trained model and fine-tune it for a specific task. For example; Using a pre-trained NLP model and adapting it to analyze legal documents.

## Implementation
Check out the prototype.py file to understand the convience of implementing a solution with the Prototype Pattern.