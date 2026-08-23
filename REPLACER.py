import csv

input_file = 'servgrow_sample_emails.csv'
output_file = 'servgrow_sample_emails_clean.csv'

with open(input_file, 'r', encoding='utf-8') as f_in:
    rows = list(csv.reader(f_in))

with open(output_file, 'w', newline='', encoding='utf-8') as f_out:
    writer = csv.writer(f_out)
    for row in rows:
        # Removes literal double quotes from every cell in the row
        clean_row = [cell.replace('"', '') for cell in row]
        writer.writerow(clean_row)

print(f"[OK] Cleaned file saved as {output_file}")