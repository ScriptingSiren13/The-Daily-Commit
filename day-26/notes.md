# Day 26 — Displaying Images in Tkinter

Today I studied how images are loaded and displayed inside Tkinter applications. After learning the concepts, I uploaded the `.py` example files to my **Tkinter** repository.

---

##  Why this topic matters

Images are commonly used in desktop GUIs for:

- icons
- backgrounds
- buttons
- previews

Tkinter supports this, but image handling comes with rules and limitations that developers must understand.

---

##  Image handling in Tkinter (conceptual)

Tkinter uses `PhotoImage` to show images inside widgets such as:

- Label
- Button
- Canvas
- Text

However, **PhotoImage only supports:**

✓ PNG  
✓ GIF  
✓ PPM/PGM  

and **does NOT support `.jpg` directly**, so PIL (Pillow) is used for JPG support.

---

##  Using PIL for JPG

To load JPG images, we use:

- `Image.open()` for loading
- `ImageTk.PhotoImage()` for converting to a Tk-compatible object

This allows displaying JPGs in GUI elements like labels or backgrounds.

---

##  The “reference rule” (important)

Tkinter requires keeping a reference to the image object.  
If not, Python’s garbage collector removes it and the image disappears.

Developers fix this by doing:

```
label.image = photo
```

This keeps the image alive for the lifetime of the widget.

---

##  Today’s learning covered:

- displaying images on labels
- using images as backgrounds with `.place()`
- difference between PhotoImage vs PIL
- format support differences (PNG vs JPG)
- keeping references to prevent disappearing images

---

##  Repository Work

Today I uploaded `.py` scripts to the **Tkinter repository** demonstrating:

✔ image display using PhotoImage  
✔ image display using PIL (for JPG)  
✔ background image placement  
✔ reference management examples  

---

##  Key takeaways

- Tkinter’s native support is limited to a few formats
- PIL enables wider format support including JPG
- every displayed image must be referenced
- images integrate inside standard widgets
- useful for UI-focused Python desktop apps
