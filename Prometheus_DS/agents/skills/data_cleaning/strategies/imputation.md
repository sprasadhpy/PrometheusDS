# Strategy: Advanced Imputation

## Rules
1. For SimpleImputer, always call .ravel() on the output before assigning to a column.
2. For categorical imputation, ensure the category exists before assigning.
3. Never impute ID or primary key columns.
4. Consider if the missingness itself is informative (e.g., "no internet service" → missing online features).

## Code Pattern
```python
from sklearn.impute import SimpleImputer

# Numeric imputation with SimpleImputer
imputer = SimpleImputer(strategy='mean')
for col in numeric_cols_with_missing:
    data[col] = imputer.fit_transform(data[[col]]).ravel()  # .ravel() is critical!

# Categorical imputation
imputer_cat = SimpleImputer(strategy='most_frequent')
for col in cat_cols_with_missing:
    data[col] = imputer_cat.fit_transform(data[[col]]).ravel()
```

## Important
- fit_transform() returns a 2D array; DataFrame columns are 1D → always use .ravel()
- If a categorical column is dtype 'category', add new categories BEFORE assigning values
- Verify imputer didn't introduce unexpected values
