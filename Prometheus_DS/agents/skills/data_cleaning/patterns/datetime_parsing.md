# Pattern: Parse Datetime Columns

## When to Use
- Object columns with values like "2023-01-15", "15/01/2023", "Jan 15, 2023"
- Column names containing 'date', 'time', 'timestamp', 'created', 'updated'

## Implementation
```python
date_candidates = [col for col in data.columns 
                   if any(kw in col.lower() for kw in ['date', 'time', 'timestamp', 'created', 'updated'])]

for col in date_candidates:
    if data[col].dtype == 'object':
        try:
            data[col] = pd.to_datetime(data[col], infer_datetime_format=True, errors='coerce')
        except Exception:
            pass  # Leave as-is if conversion fails
```

## Key Rules
- Use infer_datetime_format=True for automatic format detection
- Use errors='coerce' to handle unparseable values
- Don't force datetime conversion on columns that aren't dates
- Check a few sample values before deciding to convert
