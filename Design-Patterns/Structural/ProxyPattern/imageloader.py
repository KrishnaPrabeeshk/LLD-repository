from abc import ABC, abstractmethod
import time

class Image(ABC):
    @abstractmethod
    def display(self):
        pass

class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_image_from_disk()
        self.logs = []

    def load_image_from_disk(self):
        print(f"Loading high-resolution image: {self.filename}")
    
    def display(self):
        print(f"Displaying {self.filename}")

class ProxyImage(Image):
    def __init__(self, filename, password):
        self.filename = filename
        self.password = password
        self.real_image = None
        self.correct_password = "accessdisk"
        self.logs = []

    def authenticate(self):
        if self.password == self.correct_password:
            return True
        else:
            print("Access Denied: Incorrect Password!")
            return False

    def display(self):
        if not self.authenticate():
            return  # Stop execution if authentication fails

        if self.real_image is None:
            print(f"Loading image for the first time...")
            self.real_image = RealImage(self.filename)
        
        # Logging access time
        access_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.logs.append(f"Accessed {self.filename} at {access_time}")
        
        self.real_image.display()

# Client Code
print("Using Proxy Pattern:")
image1 = ProxyImage("photo1.jpg", "atoz")  # Wrong password
image1.display()  # Should deny access
print()
image2 = ProxyImage("photo2.jpg", "accessdisk")  # Correct password
image2.display()  # Loads and displays
print()
image1.display()
image2.display()  # Doesn't reload, just displays

