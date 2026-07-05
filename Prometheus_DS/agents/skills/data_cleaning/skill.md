# Data Cleaning Agent

## Purpose
Automatically clean and preprocess tabular datasets by identifying data quality issues and generating executable Python code to fix them.

## When to Use
- Raw data with missing values, duplicates, incorrect dtypes, or outliers
- Before feature engineering or modelling
- When a reproducible cleaning pipeline is needed

## Capabilities
- Profiling datasets to identify quality issues
- Recommending cleaning strategies tailored to the data
- Generating self-contained Python functions
- Executing code safely in a sandboxed environment
- Self-repairing failed code through retry loops
- Tracking all execution attempts for debugging
