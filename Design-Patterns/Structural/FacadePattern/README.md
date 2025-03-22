# Facade Design Pattern

The **Facade Design Pattern** is a **structural pattern** that provides a **simplified, unified interface** to a **complex system**. It hides the underlying complexity by exposing a high-level interface, making it easier for clients to interact with the system without needing to understand its intricate details.

## Why do we need this? 🤔

- In smart phones these days we are given the option to set modes on our phone,
- For example, If we select the sleep mode the phone will go to battery saving mode, display turns grayscale and DND is turned on.
- Similarly there are other modes on smartphones these days which let us automatically turn some settings on or off based on our needs.
- Another example is; 
- Imagine a **smart home** 🏠 with multiple systems like **lights, thermostat, security system, and music system**.  
- If you had to **manually** control each system (**turn off lights, adjust temperature, arm security, pause music**), it would be **tedious and error-prone**.  
- Instead, wouldn't it be nice to have a **single command** like “Good Night” 🌙 that **automates everything**?  

- This is exactly what the **Facade Pattern** does – it provides a **simple interface** to interact with a **complex system** behind the scenes. 

## Real-World Examples  

- 🎮 **Gaming Consoles** – Pressing the **Power** button loads multiple subsystems like graphics, audio, and network without manual setup.  
- 📺 **Home Theater System** – A single **remote button** starts the TV, adjusts sound, and dims lights instead of configuring each separately.  
- 📡 **Streaming Services** – Netflix hides the complexities of buffering, resolution adjustments, and network management behind a play button.  
- 🏠 **Smart Home Automation** – “Good Night” mode turns off lights, locks doors, adjusts thermostat, and arms security in one go.

## Implementation  

The **Smart Home** example demonstrates the **Facade Pattern** by creating a single **SmartHomeFacade** class that simplifies the interaction with multiple systems:  

- **Lights** 💡 – Turn on/off.  
- **Thermostat** 🌡️ – Adjusts temperature.  
- **Security System** 🔒 – Arms/disarms the system.  
- **Music System** 🎵 – Plays or pauses music.  