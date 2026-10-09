import csv

input_file = "sample_dirty.csv"
output_file = "cleaned.csv"

rows_read = 0
rows_skipped = 0
duplicates_removed = 0
rows_saved = 0

clean_rows = []
seen_rows = set()

with open(input_file, "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        rows_read += 1

        
        row = [value.strip() for value in row]

        
        if len(row) < 3:
            rows_skipped += 1
            continue

        name = row[0]
        email = row[1].lower()
        city = row[2]

        
        if email == "":
            rows_skipped += 1
            continue

        cleaned_row = [name, email, city]

        
        row_key = tuple(cleaned_row)

        if row_key in seen_rows:
            duplicates_removed += 1
            continue

        seen_rows.add(row_key)
        clean_rows.append(cleaned_row)

with open(output_file, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(header)
    writer.writerows(clean_rows)

    rows_saved = len(clean_rows)

print("Cleaning complete")
print("Rows read:", rows_read)
print("Rows skipped:", rows_skipped)
print("Duplicates removed:", duplicates_removed)
print("Rows saved:", rows_saved)
print("Output file:", output_file)