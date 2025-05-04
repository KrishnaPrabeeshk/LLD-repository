# Command Design Pattern

The **Command Design Pattern** is a behavioral pattern that turns a **request into a standalone object**. This allows requests to be **parameterized, queued, executed at different times, undone,** or even **logged**, all while keeping the sender (invoker) decoupled from the receiver.

## Why do we need this? 🤔

Let’s say I’m building a **smart home remote** 🎛️ that can turn devices like lights and fans on/off. If I directly call methods like `light.on()` or `fan.off()` inside my remote, it’s super tightly coupled to all the devices.

Now that might seem fine initially, but it falls apart when I want to:

- Add undo functionality (e.g., "oops, turn the light back off")

- Add new devices like speakers or TVs

- Schedule actions or store command history

- Change behavior on the fly

So instead of directly calling device methods, I wrap every action inside a **command object**. The remote just stores and runs whatever command it’s given — it doesn’t need to know what it’s doing or how. This makes the whole thing **decoupled, extensible**, and really clean.


## Examples 

- 🎨 **GUI buttons** – Every button click just triggers a command object (`SaveCommand`, `UndoCommand`, etc.)

- 🏠 **Smart Home remotes** – Turn on/off lights, fans, etc., all through command wrappers

- 📋 **Job queues** – Commands can be stored and executed later

- 🧠 **Macros** – Record and replay a batch of commands

- 🔄 **Undo/redo systems** – Every action can be reversed using its command’s `undo()` method

## What the system looks like: Before vs After 🧵

### ❌ Without Command Pattern:

```python
remote.press_light_on(light)
remote.press_fan_off(fan)
```

Here the remote **knows too much** — it’s directly talking to each device. So anytime I add a new action, I need to go back and change the remote. Not scalable.

### ✅ With Command Pattern:

```python
remote.set_command(LightOnCommand(light))
remote.press_button()
```

Now the remote just works with commands — it doesn’t care who or what the receiver is. That’s 🔥 for flexibility.

And because I added `undo()` in each command, I can do stuff like:

```python
remote.press_undo()
```

---

## Wait — how’s this different from Facade? 🤔

Great question. They’re kinda similar at first glance, but serve totally different purposes.

Here’s how I think about it:

| Feature       | **Command Pattern**                                  | **Facade Pattern**                                    |
| ------------- | ---------------------------------------------------- | ----------------------------------------------------- |
| Pattern Type  | Behavioral                                           | Structural                                            |
| Why it's used | Wrap each action so it can be run, queued, or undone | Hide system complexity behind a clean interface       |
| Focus         | Behavior control (execute, undo, log)                | Simplicity and convenience                            |
| Example       | Remote executes `TurnOnCommand`                      | `GoodNightMode()` turns off lights, locks doors, etc. |
| Undo support  | ✅ Built in if you add `undo()`                       | ❌ Not part of its goal                                |
| Flexibility   | High — super dynamic                                 | Moderate — fixed interface                            |


## Implementation 🛠️

The `smarthomeremotecontrol.py` file shows how I set up commands for devices like lights and fans. I also implemented **undo** — which is where this pattern really helps.