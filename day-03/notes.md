# Day 03 — map() and filter() with Lambda Functions

## What is map()?

map() is a higher-order function that applies a given function to each element of an iterable, such as a list, and returns the transformed results.

The structure of the data remains the same. Only the values change as a result of applying the function to every element.

In other words, map() answers the question:
“What should I do to each element?”

---

## What is filter()?

filter() is a higher-order function that selects elements from an iterable based on a condition.

The function passed to filter() must return either True or False.
Only the elements for which the function returns True are kept in the result.

filter() answers a different question:
“Which elements should be kept?”

---

## Relationship with Lambda Functions

Both map() and filter() are higher-order functions because they accept another function as input.

When the logic passed to them is small and used only once, lambda functions are ideal. They allow the behavior to be written inline without creating separate helper functions.

This keeps the code concise while preserving the separation between structure (map/filter) and behavior (the lambda expression).
