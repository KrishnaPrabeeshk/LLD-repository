from abc import ABC, abstractmethod

# Fly Behavior Strategy Interface
class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

# Quack Behavior Strategy Interface
class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass

# Concrete Fly Behaviors
class FlyWithWings(FlyBehavior):
    def fly(self):
        return "I'm flying with wings!"

class FlyNoWay(FlyBehavior):
    def fly(self):
        return "I can't fly."

class FlyRocketPowered(FlyBehavior):
    def fly(self):
        return "I am flying with a rocket! 🚀🚀"

# Concrete Quack Behaviors
class Quack(QuackBehavior):
    def quack(self):
        return "I Quack."

class Squeak(QuackBehavior):
    def quack(self):
        return "I Squeak."

class Mute(QuackBehavior):
    def quack(self):
        return "I am mute."

# Duck Context Class
class Duck:
    def __init__(self, name, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior):
        self.name = name
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def perform_fly(self):
        return f"{self.name}: {self.fly_behavior.fly()}"

    def set_fly_behavior(self, fly_behavior: FlyBehavior):
        self.fly_behavior = fly_behavior

    def perform_quack(self):
        return f"{self.name}: {self.quack_behavior.quack()}"

    def set_quack_behavior(self, quack_behavior: QuackBehavior):
        self.quack_behavior = quack_behavior

# Example usage
if __name__ == "__main__":
    mallard = Duck("Mallard", FlyWithWings(), Quack())
    print(mallard.perform_fly())     # Mallard: I'm flying with wings!
    print(mallard.perform_quack())   # Mallard: I Quack.

    rubber_duck = Duck("Rubber Duck", FlyNoWay(), Squeak())
    print(rubber_duck.perform_fly())     # Rubber Duck: I can't fly.
    print(rubber_duck.perform_quack())   # Rubber Duck: I Squeak.

    # Runtime behavior swap
    rubber_duck.set_fly_behavior(FlyRocketPowered())
    rubber_duck.set_quack_behavior(Mute())
    print(rubber_duck.perform_fly())     # Rubber Duck: I am flying with a rocket! 🚀🚀
    print(rubber_duck.perform_quack())   # Rubber Duck: I am mute.
