class Character:
    """Flyweight object representing a single character."""
    _instances = {}

    def __new__(cls, letter, font="Arial", size=12,color = "Black"):
        key = (letter, font, size, color)
        if key not in cls._instances:
            cls._instances[key] = super(Character, cls).__new__(cls)
            cls._instances[key].letter = letter
            cls._instances[key].font = font
            cls._instances[key].size = size
            cls._instances[key].color = color
        return cls._instances[key]

    def display(self, position):
        print(f"Character '{self.letter}' at position {position} with font {self.font}, with color {self.color} and size {self.size}")

class TextEditor:
    """Context that uses flyweight objects."""
    def __init__(self):
        self.characters = []

    def add_character(self, letter, position, font="Arial", size=12, color = "Black"):
        char = Character(letter, font, size, color)  # Reuses objects
        self.characters.append((char, position))

    def display_text(self):
        for char, position in self.characters:
            char.display(position)

# Client code
editor = TextEditor()
editor.add_character("H", 0)
editor.add_character("e", 1)
editor.add_character("l", 2)
editor.add_character("l", 3)
editor.add_character("o", 4)
editor.add_character("H", 5)  # Reuses 'H' object instead of creating a new one
editor.add_character("W",6,"Times New Roman",14)
editor.add_character("o",7)
editor.add_character("r",8)
editor.add_character("l",8)
editor.add_character("d",8)
editor.add_character("!",8,"Arial",12,"Red")
editor.display_text()
