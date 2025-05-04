from abc import ABC, abstractmethod
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def undo(self):
        pass

class Light:
    def on(self):
        print("Light is ON")

    def off(self):
        print("Light is OFF")
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    def undo(self):
        self.light.off()

    def execute(self):
        self.light.on()
class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()
    def undo(self):
        self.light.on()

class Fan:
    def on(self):
        print("Fan is ON")

    def off(self):
        print("Fan is OFF")
class FanOnCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.on()
    def undo(self):
        self.fan.off()

class FanOffCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.off()
    def undo(self):
        self.fan.on()

class RemoteControl:
    def __init__(self):
        self.command = None
        self.history = []  # Maintain a history of executed commands

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()
            self.history.append(self.command)  # Add the command to history
        else:
            print("No command set.")

    def press_undo(self):
        if self.history:
            last_command = self.history.pop()  # Get the last executed command
            last_command.undo()
        else:
            print("No commands to undo.")

# Client code
if __name__ == "__main__":
    # Create the receiver objects
    light = Light()
    fan = Fan()

    # Create command objects
    light_on_command = LightOnCommand(light)
    light_off_command = LightOffCommand(light)
    fan_on_command = FanOnCommand(fan)
    fan_off_command = FanOffCommand(fan)

    # Create the remote control
    remote = RemoteControl()

    # Turn on the light
    remote.set_command(light_on_command)
    remote.press_button()

    # Turn off the light
    remote.set_command(light_off_command)
    remote.press_button()

    # Turn on the fan
    remote.set_command(fan_on_command)
    remote.press_button()

    # Turn off the fan
    remote.set_command(fan_off_command)
    remote.press_button()

    print("\nUndoing last commands:")
    # Undo the last command (turn off the fan)
    remote.press_undo()
    # Undo the last command (turn on the fan)
    remote.press_undo()
    # Undo the last command (turn off the light)
    remote.press_undo()
    # Undo the last command (turn on the light)
    remote.press_undo()