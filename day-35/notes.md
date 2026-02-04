# Day 35 — Outlier Detection using IQR (Interquartile Range)

##  Topic Studied
**Outlier Detection using the IQR Method**

---

##  What is an Outlier?
An outlier is a data point that is **very different** from the rest of the dataset.

Outliers can happen due to:
- human/data entry mistakes
- measurement errors
- rare real-world events
- unusual but valid observations

---

##  Why Detect Outliers?
Outliers can:
- distort the mean and standard deviation
- affect model training badly (especially regression)
- reduce accuracy and generalization
- create misleading patterns in data analysis

So detecting them is an important part of **data preprocessing**.

---

##  What is IQR?
IQR stands for **Interquartile Range**.

It measures the spread of the middle 50% of the data.

### Key Terms
- **Q1 (25th percentile)** → value below which 25% of the data lies  
- **Q3 (75th percentile)** → value below which 75% of the data lies  
- **IQR = Q3 - Q1**

---

##  IQR Rule for Outliers
A point is considered an outlier if it lies outside:

### Lower Bound
Q1 - 1.5 * IQR


### Upper Bound
Q3 + 1.5 * IQR


Any value:
- smaller than the lower bound → outlier
- larger than the upper bound → outlier

---

##  Why IQR is Useful
✔ Works well even when data is not normally distributed  
✔ Not affected by extreme values like mean and standard deviation  
✔ Simple, fast, and widely used in ML preprocessing  

---

## 🛠 What I Did Today
- Revised what outliers are and why they matter in ML
- Studied the IQR method step-by-step
- Understood how Q1, Q3, and IQR define the outlier boundaries
- Practiced identifying outliers using:
  - lower bound
  - upper bound
- Learned that IQR is especially useful for skewed distributions

---

##  Important Notes
- IQR detects outliers based on distribution spread, not "errors"
- Some outliers may be valid and meaningful
- Removing outliers blindly can cause loss of useful information

---

##  Key Takeaways
- IQR is a robust method for outlier detection
- Outliers are values outside Q1 - 1.5×IQR and Q3 + 1.5×IQR
- Best used before model training for cleaner, more stable data

---

 **Day 35 completed — Learned Outlier Detection using the IQR method.**

