# Strategy: Remove Duplicate Rows

## Rules
1. Identify fully duplicated rows (all columns identical).
2. Keep the first occurrence, drop the rest.
3. If an ID column exists, duplicates on non-ID columns are also worth checking.

## Code Pattern
```python
# Remove exact duplicate rows
initial_rows = len(data)
data = data.drop_duplicates(keep='first')
rows_removed = initial_rows - len(data)
```

## Important
- Always report how many duplicates were found and removed
- Don't deduplicate on ID columns alone (they should be unique by definition)
- If the dataset has no duplicates, skip this step cleanly
