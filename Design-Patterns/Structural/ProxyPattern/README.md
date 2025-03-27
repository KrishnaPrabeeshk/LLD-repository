# Proxy Design Pattern

The **Proxy Design Pattern** is a structural design pattern that acts as a placeholder or intermediary for another object to control access, enhance functionality, or reduce resource consumption.

## Why do we need this? 🤔
- Imagine a **high-resolution image viewer** 🖼️ that loads large image files.
- If every image loads immediately, it may cause **slow performance**.
- Instead, a **proxy** can **delay** loading the actual image until needed (lazy loading).
- The proxy can also **control access** (e.g., password protection) or **log requests**.

## Examples 
- **Virtual Proxy (Lazy Loading) 🎭** – Image viewers load images only when displayed.
- **Security Proxy 🔒** – Requires authentication before accessing sensitive data.
- **Logging Proxy 📝** – Logs access details (e.g., tracking requests to a service).
- **Caching Proxy 📦** – Stores results to avoid repeated expensive operations.
- **Internet Proxy 🌐** – Filters requests, caches websites, or controls network access.

## Implementation 🛠️
The `imageloader.py` file illustrates how a proxy class can control access to an image loader. It adds **lazy loading**, **password protection**, and **logging** to the real object.