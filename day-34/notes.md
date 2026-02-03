# Day 34 — Most Frequent Imputation

##  Topic Studied
**Most Frequent Imputation (Mode Imputation)**

---

##  What is Most Frequent Imputation?
Most frequent imputation is a missing value handling technique where missing values are replaced with the **most commonly occurring value (mode)** in a feature.

It is especially useful for:
- Categorical features
- Discrete numerical features

---

##  Why Use Most Frequent Imputation?
- Simple and fast to implement
- Preserves existing categories
- Works well when missing values are random
- Does not introduce new or unrealistic values

---

## 🛠 How It Works
1. Identify missing values in a feature  
2. Compute the mode of the feature (ignoring missing values)  
3. Replace all missing values with that mode  

---

##  Example

### Original Data
| Color |
|------|
| Red  |
| Blue |
| Red  |
| NaN  |
| Red  |

**Most frequent value:** Red

### After Imputation
| Color |
|------|
| Red  |
| Blue |
| Red  |
| Red  |
| Red  |

---

##  Implementation in Scikit-Learn
```python
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='most_frequent')
X_imputed = imputer.fit_transform(X)
