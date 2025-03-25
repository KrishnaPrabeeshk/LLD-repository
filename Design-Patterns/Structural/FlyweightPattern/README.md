# Flyweight Design Pattern

The Flyweight Design Pattern is a structural design pattern that helps minimize memory usage by sharing common objects instead of creating new ones for every instance. It is useful when a program needs to create a large number of objects that share common data.

## Why do we need this? 🤔

- Imagine a text editor ✍️ where each character is an object.

- If each character is stored separately, the program consumes a lot of memory.

- Instead, we can reuse characters that have the same properties (e.g., letter, font, size, color).

- This is exactly what the Flyweight Pattern does – it reduces memory usage by sharing objects with identical attributes.

- Now, instead of creating a new object of certain properties everytime first we check if we already did in the past. If we did, we just use the already created object saving the time and resources in creating a new object.

## Examples

- Text Editors ✍️ – Characters with the same properties (font, size, color) are reused instead of creating new objects.

- Video Games 🎮 – Similar game objects (e.g., trees, bullets) reuse the same model to save memory.

- Graphical Applications 🖥️ – UI components like buttons or icons share instances instead of duplicating them.

- Library Systems 📚 – Books with the same title, author, and edition can share the same metadata instead of storing duplicate information.

- Printing Services 🖨️ – Frequently used templates, watermarks, or fonts are stored once and reused in multiple documents.

## Implementation

The texteditor.py file illustrates how saving instances of a character with certain properties can help in faster access to such objects. Without the flyweight pattern, an object of this scale might not significantly impact performance, but when the object creation process is complex, this design pattern becomes essential.