from abc import ABC, abstractmethod

class FileSystemItem(ABC):
    @abstractmethod
    def show_details(self,indent = 0):
        pass
    @abstractmethod
    def get_size(self):
        pass

class File(FileSystemItem):
    def __init__(self,name,size):
        self.name = name
        self.size = size
    
    def show_details(self, indent=0):
        print(" " * indent + f"📄 {self.name} ({self.size}KB)")
    
    def get_size(self):
        return self.size

class Folder(FileSystemItem):
    def __init__(self,name):
        self.name = name
        self.items = []
    
    def add(self,item:FileSystemItem):
        self.items.append(item)
    
    def show_details(self, indent=0):
        print(" " * indent + f"📁 {self.name} ({self.get_size()}KB)")
        for item in self.items:
            item.show_details(indent + 2)
    
    def get_size(self):
        return sum(item.get_size() for item in self.items)
    
    def delete_item(self, item: FileSystemItem):
        if item in self.items:
            self.items.remove(item)
            print(f"{item.name} deleted successfully.")
            if isinstance(item, Folder):
                print(f"All contents of {item.name} are also deleted.")
        else:
            print(f"No {item.name} found in this directory.")


root = Folder("Root")
folder1 = Folder("Documents")
folder2 = Folder("Pictures")

file1 = File("Resume.pdf",120)
file2 = File("Project.docx",300)
file3 = File("Photo.jpg",500)

folder1.add(file1)
folder1.add(file2)
folder2.add(file3)
root.add(folder1)
root.add(folder2)

root.show_details()

folder1.delete_item(file2)

root.show_details()