# Interpreter Design Pattern

The **Interpreter Design Pattern** is a behavioral design pattern that defines a way to **evaluate language grammar or expressions** by building an interpreter for it.

---

## Why do we need this? 🤔

* Imagine you're building a **smart home command interpreter** that takes natural commands like:

  > `Turn off the lights AND lock the doors`
* You want the system to **understand**, **parse**, and **execute** this logic step-by-step — including complex ones like:

  > `Turn off the lights AND (lock the doors OR arm the alarm)`
* Instead of hardcoding every condition, the interpreter pattern lets you model each command as an **object** that knows how to interpret itself.
* This allows for flexible composition of commands, nested logic, and extensible grammars.

This is especially useful for:

* **DSLs (Domain-Specific Languages)**
* **Rule engines**, **query engines**, and **template evaluators**
* Systems that must understand and act on **textual input** from users or scripts
* Imagine you're building a system that can understand expressions like:

  > `NOT (True AND False) OR True`
* Instead of manually parsing and evaluating strings, the interpreter pattern lets you model expressions as **tree structures**.
* Each node in the tree knows **how to interpret itself**, making the entire system composable, recursive, and **extensible**.

This is especially useful for:

* **DSLs (Domain-Specific Languages)**
* **Rule engines**, **query engines**, and **template evaluators**
* Situations where you want to evaluate text as logic/code, but without using something like `eval()`

---

## Examples

* 🧠 **Math expression evaluators** – Evaluate `(2 + 3) * 4`
* 🔍 **Search query engines** – Parse queries like `title:Python AND NOT tags:beginner`
* 💬 **Template engines** – Evaluate `{{ if is_admin }} Show Dashboard {{ endif }}`
* 🔒 **Access rule checkers** – Evaluate `UserIsManager AND NOT OnVacation`
* 🧾 **Expression-based validation** – Form input validations like `length > 5 AND isAlpha`

---

## Implementation 🛠️

The `booleanInterpreter.py` file demonstrates how to evaluate boolean logic strings like:

```
NOT True AND False OR True
```