# Error: fit_transform() returns 2D array

## Error Message
```
ValueError: Wrong number of items passed 2, placement implies 1
```
or shape mismatch errors when assigning imputer output to a column.

## Cause
`SimpleImputer.fit_transform()` returns a 2D numpy array (shape: n_rows × 1).
A pandas DataFrame column is 1D. Direct assignment fails.

## Fix
Always call `.ravel()` or `.flatten()` on the result:
```python
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='mean')
# WRONG:
# data[col] = imputer.fit_transform(data[[col]])

# CORRECT:
data[col] = imputer.fit_transform(data[[col]]).ravel()
```

## Prevention
- Any time you use fit_transform() and assign to a single column, add .ravel()
- This applies to all sklearn transformers, not just SimpleImputer
