# Sales Data Cleaning Project

This project cleans messy sales data using Python.

## What It Does
- Makes column names lowercase with underscores
- Removes rows with missing prices or quantities
- Removes rows with negative numbers

## How to Run
1. Put `sales_data_raw.csv` in the `data/raw/` folder
2. Run this command:
```bash
python src/data_cleaning.py
```
3. Find the clean data in `data/processed/sales_data_clean.csv`

## Requirements
- Python 3
- pandas

Install pandas:
```bash
pip install pandas
```