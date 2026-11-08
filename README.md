# ETL System

A small Python project demonstrating a basic sales-data ETL workflow:

1. **Extract** sample sales records.
2. **Transform** each amount from text to an integer, treating `"Free"` as `0`.
3. **Load** the cleaned records by printing them and appending them to `sales_data.txt`.

## Requirements

- Python 3
- No third-party packages are required.

## Run the ETL pipeline

From the project directory, run:

```bash
python main.py
```

Each run appends the processed records to `sales_data.txt`; running it again adds another copy of the sample records.

## Project files

| File | Purpose |
| --- | --- |
| `main.py` | Runs the extract, clean, and save steps in sequence. |
| `extractor.py` | Provides the sample sales records. |
| `cleaner.py` | Converts the `amount` field to an integer and maps `"Free"` to `0`. |
| `loader.py` | Prints records and appends them to `sales_data.txt`. |
| `sales_data.txt` | Output file containing saved sales records. |


