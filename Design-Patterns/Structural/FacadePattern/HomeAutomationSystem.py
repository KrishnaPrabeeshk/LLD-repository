class Lights:
    def turn_on(self):
        print("Lights turned on")
    def turn_off(self):
        print("Lights turned off")

class Thermostat:
    def set_temperature(self, temp):
        print(f"Thermostat set to {temp}°F")

class SecuritySystem:
    def arm(self):
        print("System armed")
    def disarm(self):
        print("System disarmed")

class MusicSystem:
    def __init__(self,song):
        self.song = song
    def play(self):
        print(f"Playing {self.song}")
    def pause(self):
        print(f"{self.song} paused")

class SmartHomeFacade:
    def __init__(self):
        self.lights = Lights()
        self.thermostat = Thermostat()
        self.security = SecuritySystem()
        self.music = MusicSystem("Music.mp3")
    
    def good_night(self):
        print("\nActivating Sleep mode...")
        self.security.arm()
        self.music.pause()
        self.lights.turn_off()
        self.thermostat.set_temperature(71)
    
    def good_morning(self):
        print("\n Decativating Sleep mode...")
        self.music.play()
        self.lights.turn_on()
        self.security.disarm()
        self.thermostat.set_temperature(73)
    
home = SmartHomeFacade()
home.good_night()
home.good_morning()