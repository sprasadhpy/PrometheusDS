# Pattern: Convert String Columns to Numeric

## When to Use
- Column dtype is 'object' but contains mostly numbers
- Sample values look like "29.85", "1889.5", " " (whitespace)
- The profiler shows high unique_count for an object column

## Implementation
```python
# Strip whitespace, replace empty strings, then convert
data[col] = data[col].astype(str).str.strip()
data[col] = data[col].replace(['', ' ', 'nan', 'None'], np.nan)
data[col] = pd.to_numeric(data[col], errors='coerce')
```

## Key Rules
- Always strip whitespace FIRST
- Use errors='coerce' to handle unconvertible values gracefully
- After conversion, the column will have NaN where strings couldn't convert
- Follow up with imputation if needed
