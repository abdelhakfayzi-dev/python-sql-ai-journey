import csv

def parse_csv(filename, select=None, types=None):
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        # Determine which columns to keep
        if select:
            indices = [headers.index(col) for col in select]
            selected_headers = select
        else:
            indices = list(range(len(headers)))
            selected_headers = headers
        
        records = []
        for row in rows:
            if not row:   # Skip empty lines
                continue
            
            # 1. Select columns from the row
            selected_row = [row[i] for i in indices]
            
            # 2. Apply type conversions (if types provided)
            if types:
                typed_row = [func(val) for func, val in zip(types, selected_row)]
            else:
                typed_row = selected_row
            
            # 3. Build dictionary
            record = dict(zip(selected_headers, typed_row))
            records.append(record)
        
        return records
print(parse_csv('Portfolio.csv', select = ['name', 'price'], types = [str,float]))