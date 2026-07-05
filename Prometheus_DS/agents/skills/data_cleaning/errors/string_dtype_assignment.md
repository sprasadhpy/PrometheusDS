# Error: Invalid value for dtype 'str'

## Error Message
```
TypeError: Invalid value for dtype 'str'. Value should be a string or missing value (or array of those).
```

## Cause
Trying to assign a non-string value (like a float or int) to a column with Arrow string dtype.
Happens when pandas uses `string[pyarrow]` dtype and you try to fill with a numeric value.

## Fix
Ensure the fill value is a string:
```python
# Convert fill value to string
fill_val = str(data[col].mode()[0])
data[col] = data[col].fillna(fill_val)
```

Or convert the column to object first:
```python
data[col] = data[col].astype(object)
data[col] = data[col].fillna(fill_value)
```

## Prevention
- Check dtype before imputation: if it's string/object, ensure fill values are strings
- Use `pd.isna()` checks rather than comparing to None directly
