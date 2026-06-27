import csv
def parse_csv(filename,select=None):
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records=[]
        for row in rows:
            if not row:
                continue
            record = dict(zip(headers,row))
            records.append(record)
    return records
print(parse_csv('Portfolio.csv', select=['name','shares']))