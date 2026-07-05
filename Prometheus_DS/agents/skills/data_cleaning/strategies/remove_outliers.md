# Strategy: Remove Outliers

## Rules
1. Only apply to numeric columns.
2. Use the IQR method: values beyond 3× IQR from Q1/Q3 are extreme outliers.
3. Only remove rows if the user has NOT instructed to keep outliers.
4. If the user says "don't remove outliers", skip this step entirely.

## Code Pattern
```python
numeric_cols = data.select_dtypes(include='number').columns
for col in numeric_cols:
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 3 * IQR
    upper = Q3 + 3 * IQR
    data = data[(data[col] >= lower) & (data[col] <= upper)]
```

## Important
- 3× IQR is for EXTREME outliers only (not mild outliers at 1.5× IQR)
- Always respect user instructions about outlier handling
- Don't apply to binary/boolean columns or low-cardinality integers
- Log how many rows were removed
