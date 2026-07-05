# Error: Cannot setitem on a Categorical with a new category

## Error Message
```
TypeError: Cannot setitem on a Categorical with a new category, set the categories first
```

## Cause
Trying to assign a value to a categorical column that doesn't include that value in its category list.
Commonly happens when imputing missing values into a categorical column.

## Fix
Add the new category before assignment:
```python
# Before assigning a new value to a categorical column:
if hasattr(data[col], 'cat'):
    new_val = data[col].mode()[0]
    if new_val not in data[col].cat.categories:
        data[col] = data[col].cat.add_categories(new_val)
    data[col] = data[col].fillna(new_val)
```

## Prevention
- Convert to object type before imputation, then back to category after:
```python
data[col] = data[col].astype(object)
data[col] = data[col].fillna(fill_value)
data[col] = data[col].astype('category')
```
