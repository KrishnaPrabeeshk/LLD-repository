# Bridge Design Pattern

The **Bridge Design Pattern** is used to separate the **abstraction** (the interface) from its **implementation**, allowing both to evolve **independently**. This ensures that changes or extensions in one do not affect the other.

## Why do we need this? 🤔

- Look around! Almost every **electronic device** has a dedicated **remote control**.
- However, some **smartphones** now allow us to control multiple devices using **a single app**.
- How convenient, right? Who wouldn’t love an **all-in-one solution** to control everything?
- This **convenience** is exactly what the **Bridge Pattern** offers in software design.
- It helps **separate components that can change independently**, making it easier to add **new features or devices** without breaking existing code.

## Examples

- 🎮 Remote Control & Devices – A universal remote works with multiple devices like TV, Radio, Sound System without needing separate remotes.

- 📹 Video Streaming Platforms – Netflix, YouTube, Prime Video run on different devices like Smart TV, Phone, Laptop independently.

- 💳 Payment Systems & Banks – Online payments (PayPal, Stripe) support multiple banks (BankA, BankB, BankC) without changing their core logic.

- 🕹️ Game Controllers & Consoles – A single game controller can work with Xbox and PC, keeping hardware and software separate.

- 🖥️ Operating Systems & File Systems – File managers like Windows Explorer, macOS Finder, Linux File Manager work across different operating systems.

## Implementation

I have implemented the **Remote Control** example discussed above to demonstrate how convenient the **Bridge Pattern** is. In the code, you’ll see that:

- Without the **RemoteControl** class, we would need to create **separate remote classes** for each device.
- This would lead to **unnecessary duplication** and make extending functionality harder.
- The **Bridge Pattern** solves this by **decoupling** the remote from the devices, allowing **flexibility and scalability**.