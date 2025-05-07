# Chain of Responsibility Design Pattern

The **Chain of Responsibility Pattern** is a behavioral design pattern that lets you **pass a request along a chain of handlers**. Each handler in the chain decides whether it wants to handle the request or pass it to the next handler in line.

---

## Why do we need this? 🤔

* Imagine a **tech support system** 🎧 where tickets are routed through different support levels: Basic, Advanced, Premium, and finally the CTO.
* Without this pattern, you'd end up with **long conditional chains** (`if...elif...else`) scattered across your code.
* With Chain of Responsibility, you organize handlers into a **chain** — each one checks if it can handle the request, or else delegates it.
* This makes the system more **modular**, **scalable**, and aligned with the **Open/Closed Principle**.

---

## Examples

* 📞 **Customer Support Escalation** – Tickets pass from L1 → L2 → Supervisor → Manager until resolved.
* 🔒 **Authentication Middleware** – Request flows through multiple auth checks (token, roles, rate limiting).
* 📬 **Email Filtering** – Spam filters pass emails through different rules: phishing, spam, promotions.
* 🧾 **Expense Approval** – Each expense passes through multiple approvers (Team Lead → Manager → Finance).
* 🔧 **Event Handling Pipelines** – Events are handled or passed down to lower priority listeners.

---

## Implementation 🛠️

The `support_chain.py` file implements a **tech support escalation system**. Based on ticket priority, requests are handled by:

* `BasicSupportHandler` for "low" priority
* `AdvancedSupportHandler` for "medium" priority
* `PremiumSupportHandler` for "high" priority
* `CTOHandler` as a catch-all fallback for everything else