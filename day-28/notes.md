# Day 28 — Reciprocal Transformation using NumPy & Scikit-learn

Today I studied and implemented **reciprocal transformation** as a feature transformation technique.

## 1. Reciprocal Transformation with NumPy

I applied a reciprocal transformation directly using NumPy to understand the math behind it.

Key points:
- Reciprocal transformation is computed as: 1 / x
- A small constant (1e-9) is added to avoid division by zero
- Useful for reducing the impact of large values and handling skewed data

Outcome:
- Learned how raw numerical data changes after reciprocal scaling
- Observed how larger values shrink more aggressively than smaller ones

---

## 2. Reciprocal Transformation using Scikit-learn

I then implemented the same transformation using **FunctionTransformer** from scikit-learn.

Key points:
- `FunctionTransformer` allows custom transformations inside ML pipelines
- The transformation logic is defined as a reusable function
- Makes the transformation compatible with preprocessing workflows

Benefits:
- Cleaner integration with machine learning pipelines
- Consistent preprocessing during training and inference
- More production-friendly than manual NumPy operations

---

## 3. Conceptual Takeaways

- Reciprocal transformation is a **non-linear feature transformation**
- Helps stabilize variance and reduce skewness
- Scikit-learn’s `FunctionTransformer` is ideal when transformations need to be part of a pipeline
- Adding a small epsilon is essential for numerical stability

This strengthened my understanding of feature engineering and preprocessing techniques.
