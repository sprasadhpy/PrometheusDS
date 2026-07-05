# Strategy: Fix Data Types

## Rules
1. Columns that contain numeric values stored as strings should be converted to float/int.
2. Before converting, strip whitespace and replace empty strings with NaN.
3. Columns with low cardinality (<10 unique values) that are object type may be categorical.
4. Columns matching date patterns should be converted to datetime.

## Code Pattern
```python
# String to numeric (handles spaces like " " in TotalCharges)
for col in data.select_dtypes(include='object').columns:
    # Try numeric conversion
    stripped = data[col].str.strip().replace('', np.nan)
    converted = pd.to_numeric(stripped, errors='coerce')
    # If >80% converted successfully, it's numeric
    if converted.notna().mean() > 0.8:
        data[col] = converted

# Low cardinality to category
for col in data.select_dtypes(include='object').columns:
    if data[col].nunique() < 10:
        data[col] = data[col].astype('category')
```

## Important
- Always strip whitespace BEFORE attempting conversion
- Use errors='coerce' to avoid crashes on unconvertible values
- Don't convert ID columns to numeric even if they look numeric
