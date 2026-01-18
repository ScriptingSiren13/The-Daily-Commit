# Day 18 — Turtle Graphics (Styling & Drawing Primitives)

Today I continued exploring Python’s `turtle` module and uploaded multiple small example programs to a separate repository for practice.

The focus for the day was on learning how to control the turtle’s **visual presentation** and **drawing behavior**, not just movement.

---

##  1. Shape Drawing (Filled Triangle)

Tested basic shape drawing with fill operations:

- set fill color
- begin fill
- draw using loop
- end fill

This helped understand how `pen.begin_fill()` and `pen.end_fill()` wrap around drawing operations to generate solid shapes.

---

##  2. Turtle Icon Size (shapesize)

Explored how to resize the **turtle cursor/icon** without affecting line thickness.

Key learning:

> `shapesize()` modifies only the displayed turtle icon — **not the drawn line thickness**

Used stretch-width and stretch-length parameters to change the visual proportions of the turtle.

---

##  3. Line Thickness (pensize)

Experimented with `pensize()` to adjust stroke thickness of lines.

Learning distinction:

> `shapesize()` → affects icon  
> `pensize()` → affects drawing

Both are independent and can be combined for stylistic control.

---

##  4. Drawing Speed (speed)

Explored the animation speed using `speed()`:

- slow movement for visualization
- fast movement for quick rendering

Discovered how speed impacts the feedback loop when testing geometric shapes or animations.

---

##  5. Color Control (pencolor, fillcolor, color)

Learned how to configure:

- **outline stroke color** → `pencolor()`
- **shape fill color** → `fillcolor()`
- **both together** → `color(pen, fill)`

This completed the color model for drawing filled or outlined shapes.

---

##  Final Summary

Today’s themes were:

✔ styling the turtle  
✔ styling the stroke  
✔ styling the shape fill  
✔ increasing drawing control  
✔ uploading practice examples

---

##  Repo Note

All example files for today’s practice sessions were uploaded to a dedicated turtle practice repository for future reference.

---


