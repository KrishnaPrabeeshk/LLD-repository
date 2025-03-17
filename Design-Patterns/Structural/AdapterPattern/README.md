# Adapter pattern

The Adapter pattern is a structural design pattern that allows incompatible interfaces to work together. It acts as a bridge between two interfaces that might not otherwise be compatible. Essentially, the adapter converts the interface of a class into another interface that a client expects.

## Why do we need this? 🤔

- Imagine you have a USB charger that only fits into USB ports.

- you travel to a country where they use European-style power outlets, which are completely different from USB ports. 

- To use your charger in this new country, you get a travel **adapter**.

- The idea of this pattern is exactly the same as the travel adapter.

- The Adapter Pattern allows two incompatible systems (like your charger and a different outlet) to work together by introducing an intermediary (the adapter).

## Examples

- 💻 SD Card Reader: An SD card reader converts the SD card’s interface to USB for your computer.

- 🎧 Audio Jack to Bluetooth Adapter: A Bluetooth transmitter lets your wired headphones connect wirelessly to your smartphone.

- 🎥 Media Format Conversion: A media player adapter converts an MP4 file to an AVI format for compatibility.

- 🚗 Car Charger for Different Vehicle Types: A power outlet adapter allows a car charger to work with different vehicle power outlets.

- 💾 Database Connection Adapters: A database adapter enables your application to connect to different databases (e.g., MySQL to PostgreSQL).

## Implementation

I have implemented a MediaPlayer.py which shows for example an existing AdvancedMediaPlayer to work with a client that expects the MediaPlayer interface.