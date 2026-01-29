# Day 29 — Ordinal & Label Encoding with Train–Test Split

Today I worked on **data preprocessing and encoding categorical features** using NumPy, Pandas, and scikit-learn.

---

## 1. Dataset Loading & Initial Processing

- Loaded a CSV dataset using Pandas.
- Performed basic inspection using `.sample()` and `.head()`.
- Selected relevant categorical columns for modeling:
  - review
  - education
  - purchased (target)

This step helped focus only on features required for encoding and model training.

---

## 2. Train–Test Split

- Split the dataset into training and testing sets using `train_test_split`.
- Features (`X`):
  - review
  - education
- Target (`y`):
  - purchased
- Used an 80–20 split to avoid data leakage and ensure fair evaluation.

This ensures encoders are fitted **only on training data**, which is a best practice.

---

## 3. Ordinal Encoding for Ordinal Features

Applied **Ordinal Encoding** to categorical input features that have a natural order.

### Feature Ordering Used:
- review: `Poor < Average < Good`
- education: `School < UG < PG`

Key learnings:
- OrdinalEncoder converts ordered categories into numeric values.
- Category order must be defined explicitly.
- Encoder is fitted on training data and applied to both train and test sets.

This preserves semantic meaning while converting categories into numbers.

---

## 4. Label Encoding for Target Variable

Applied **Label Encoding** to the output feature (`purchased`).

- Classes:
  - No → 0
  - Yes → 1

Key points:
- LabelEncoder is suitable for encoding target labels.
- Encoded both `y_train` and `y_test`.
- Ensures compatibility with machine learning models.

---

## 5. Conceptual Takeaways

- Ordinal encoding is used when categories have a meaningful order.
- Label encoding is appropriate for binary or categorical target variables.
- Encoders must always be fitted on training data only.
- Proper preprocessing is essential for stable and unbiased ML models.

This session strengthened my understanding of **categorical data handling** and **ML preprocessing pipelines**.
