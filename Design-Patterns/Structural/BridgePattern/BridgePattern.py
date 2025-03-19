class Device:
    def turnOn(self):
        pass
    def turnOff(self):
        pass
    def setVolume(self):
        pass

class TV(Device):
    def turnOn(self):
        print("TV is turned on")
    def turnOff(self):
        print("TV is turned off")
    def setVolume(self,volume):
        print(f"TV Volume set to {volume}")

class Radio(Device):
    def turnOn(self):
        print("Radio is turned on")
    def turnOff(self):
        print("Radio is turned off")
    def setVolume(self,volume):
        print(f"Radio Volume set to {volume}")

class RemoteControl:
    def __init__(self,device: Device):
        self.device = device
    
    def powerOn(self):
        self.device.turnOn()
    def powerOff(self):
        self.device.turnOff()
    def adjustVolume(self,volume):
        self.device.setVolume(volume)

class SmartRemoteControl(RemoteControl):
    def mute(self):
        self.device.setVolume(0)

tv = TV()
radio = Radio()

remote_tv = RemoteControl(tv)
remote_radio = RemoteControl(radio)

remote_tv.powerOn()
remote_tv.adjustVolume(20)
remote_tv.powerOff()

remote_radio.powerOn()
remote_radio.adjustVolume(10)
remote_radio.powerOff()

smart_remote_tv = SmartRemoteControl(tv)
smart_remote_tv.mute()