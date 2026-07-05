# Pattern: Categorical Column Imputation

## When to Use
- Object or category columns with missing values
- Low cardinality columns (< 20 unique values)

## Implementation
```python
for col in data.select_dtypes(include=['object', 'category']).columns:
    if data[col].isna().any():
        # Convert to object to avoid category issues
        data[col] = data[col].astype(object)
        # Fill with mode
        mode_val = data[col].mode()
        if len(mode_val) > 0:
            data[col] = data[col].fillna(mode_val[0])
```

## Key Rules
- Always convert categorical dtype to object BEFORE imputation
- Check that mode() actually returns a value (empty Series if all NaN)
- Convert back to category after imputation if needed
- Don't impute if the column is an ID or has very high cardinality
