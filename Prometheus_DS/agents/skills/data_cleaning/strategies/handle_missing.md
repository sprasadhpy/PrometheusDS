# Strategy: Handle Missing Values

## Rules
1. If a column has >40% missing values, drop the column entirely.
2. For numeric columns with <40% missing, impute with the column mean.
3. For categorical columns with <40% missing, impute with the column mode.
4. After imputation, if rows still have missing values, drop those rows.

## Code Pattern
```python
# Drop columns with >40% missing
threshold = 0.4
missing_pct = data.isna().mean()
cols_to_drop = missing_pct[missing_pct > threshold].index.tolist()
data = data.drop(columns=cols_to_drop)

# Impute numeric with mean
numeric_cols = data.select_dtypes(include='number').columns
for col in numeric_cols:
    if data[col].isna().any():
        data[col] = data[col].fillna(data[col].mean())

# Impute categorical with mode
cat_cols = data.select_dtypes(include='object').columns
for col in cat_cols:
    if data[col].isna().any():
        data[col] = data[col].fillna(data[col].mode()[0])
```

## Important
- Always check if mode() returns an empty Series before using [0]
- Never impute ID columns — drop them or leave them
- Document which columns were imputed and why
