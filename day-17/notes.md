# Day 16 — Turtle Graphics Primer + Repo Setup

Today I explored the basics of the **Turtle Graphics** module in Python, focusing on how drawing works through movement, pen controls, and heading orientation. This was mainly foundational learning to understand how graphical commands translate into visible output.

---

## 1. Turtle Drawing Model

Turtle uses a simple model:

```
Canvas (Window) + Turtle (Pen) + Movement Commands
```

Core conclusions:

- The turtle acts like a pen
- A window is required to display drawings
- The turtle always has a **direction (heading)**
- Movement draws lines depending on pen state
- `turtle.done()` keeps the window open after execution

---

## 2. Canvas Setup Concepts

Learned how to:

- initialize the drawing window
- change background color
- set title
- create a turtle pen object

These are required before any drawing code.

---

## 3. Movement & Heading

Movement tested:

- `forward()`
- `backward()`

Turning tested:

- `left()`
- `right()`

Heading angles visualized as:

```
      90°  ↑
           |
180°  ←   T   → 0°
           |
          270°
```

Also noted:  
`heading()` returns orientation without modifying it.

---

## 4. Pen Drawing vs Non-Drawing Modes

Understood difference between modes:

- `pendown()` → draw while moving
- `penup()` → move without drawing

Useful for patterns with gaps or separate strokes.

---

## 5. Practical Exercises Completed

Ran multiple mini scripts to verify:

- window creation
- movement commands
- heading tracking
- pen up/down effects

Helped understand how Turtle converts instructions into visuals.

---

## 6. Repository Work

Created a **separate Turtle repository** to store the exercises.

Current contents include:

✔ basic window setup  
✔ movement tests  
✔ heading experiments  
✔ pen control snippets  

This repo will continue growing as I explore more features.

---

## 7. Forward Plan

Next stages of learning:

- geometric shapes (square, triangle, star)
- simple animations
- event-driven interactions (mouse/keyboard)
- possible teaching use-cases with Turtle

---
