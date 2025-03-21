# Composite Design Pattern

The **Composite Design Pattern** is used to treat **individual objects** and **compositions of objects** uniformly. It structures objects in a **tree-like** hierarchy, where both single objects and groups of objects are treated the same way.

## Why do we need this? 🤔

- Imagine a **file system** where a **folder** can contain both **files** and **other folders**
- To implement this normally we would have to handle every case carefully
- from adding things into the folder to looking at it's size or deleting it.
- With **composite pattern** we manage **both files and folders** using the **same interface**.
- This makes operations like **displaying details**, **calculating sizes**, or **deleting items** work **recursively** on both files and folders.

## Examples
- 📂 **File System** – Folders contain files and other folders, but we interact with them in a uniform way.
- 🏢 **Company Hierarchy** – An organization has employees at different levels (Managers, Employees), but all are treated as a part of the company.
- 🎨 **Graphics Editor** – A drawing can contain simple shapes (circles, rectangles) or complex compositions of shapes, but all are handled in the same way.
- 🗂️ **UI Components** – User interfaces have individual elements (buttons, labels) and composite elements (forms, panels), all treated as components.

## Implementation

I have implemented the **File System** example using the **Composite Pattern**, demonstrating how it simplifies managing both files and folders. In the code, you’ll see that:

- The **FileSystemItem** interface ensures that both **files and folders** follow a common structure.

- **Folders** can contain multiple **files or other folders**, allowing recursive operations.

- The **get_size()** method calculates the total size dynamically by summing up all contained items.

- The **delete_item()** method enables removal of files from folders, maintaining a structured and flexible hierarchy.