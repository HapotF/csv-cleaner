# CSV Cleaner

A simple Python script for cleaning CSV data.

## Features

- Removes leading and trailing whitespace
- Converts email addresses to lowercase
- Skips rows with missing email addresses
- Removes duplicate rows
- Saves cleaned data to a new CSV file
- Prints a processing summary

## Example

Input:

```csv
name,email,city
John,john@example.com,Berlin
Anna,anna@example.com,Munich
John,john@example.com,Berlin
Mike,,Hamburg
 anna ,ANNA@example.com, munich
```

Output:

```csv
name,email,city
John,john@example.com,Berlin
Anna,anna@example.com,Munich
anna,anna@example.com,munich
```

## Run

```bash
python cleaner.py
```

The cleaned file will be saved as:

```text
cleaned.csv
```

## Requirements

- Python 3.x
- No external dependencies required
