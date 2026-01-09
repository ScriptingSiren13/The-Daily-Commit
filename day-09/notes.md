# Day 09 — FastAPI Basics and First Endpoint

Today I started with FastAPI and focused on understanding the basics of how
FastAPI applications work, without going into asynchronous programming yet
(that will be covered separately later).

---

## What I Learned Today

### 1. What FastAPI Is

FastAPI is a modern, high-performance web framework in Python for building APIs.
It uses Python type hints for clarity and automatic data validation and supports
efficient asynchronous operations for scalability.

---

### 2. FastAPI Architecture (High-Level)

FastAPI sits on top of three major components:

- **Starlette** → web framework layer (routing, requests, responses, middleware)
- **Pydantic** → data validation and parsing based on Python type hints
- **Uvicorn** → ASGI web server that runs the application

Together these provide performance, validation, and developer ergonomics.

---

### 3. First FastAPI App

I wrote my first small FastAPI application that creates a FastAPI instance,
defines a route using a decorator, and returns JSON to the client. This gave me
a concrete understanding of how FastAPI handles requests and responses.

---

### Note on Async Code

I intentionally did not attempt to understand asynchronous code yet. I encountered
async examples only for exposure, but I will explore FastAPI’s async behavior
separately after I cover more foundational topics.

---

## Repository Decision (Important)

I decided that I will create a **separate repository dedicated entirely to FastAPI**
where the learning content will be organized into folders by topic such as:

- Routing
- Request models
- Validation
- Asynchronous support
- Authentication & Authorization
- Deployment
- Middleware
- CI/CD
- etc.

Each folder will contain **detailed documentation** and **supporting code examples**
so that the repository becomes a long-term, structured FastAPI knowledge base.

This keeps the `365-days` repository focused on daily progress, while the FastAPI
repository becomes a more polished, topic-based learning asset.

---

## Status

I currently have one working FastAPI snippet that returns a JSON response, and a
good conceptual understanding of FastAPI basics. Tomorrow I will continue with
additional foundational components before moving deeper into asynchronous features,
request models, validation, and backend business logic.
