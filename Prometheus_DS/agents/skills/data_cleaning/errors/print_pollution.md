# Error: Sandbox returned non-JSON output

## Error Message
```
Sandbox returned non-JSON output: 'Initial shape: (7043, 21)...'
```

## Cause
The generated function contains `print()` statements. The sandbox communicates
via JSON on stdout. Any print output corrupts the JSON response.

## Fix
Remove ALL print statements from the generated function:
```python
# BAD - this breaks the sandbox
def data_cleaner(data_raw):
    print(f"Shape: {data_raw.shape}")  # DON'T DO THIS
    ...

# GOOD - no prints
def data_cleaner(data_raw):
    ...
    return data_cleaned
```

## Prevention
- Never include print(), logging, or any stdout output in generated functions
- The function should ONLY return the cleaned DataFrame
- If you need debugging info, store it in variables, don't print it
