import csv


def read_csv(path: str, col_name) -> list[dict[str, str]]:
    """"""
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        result = calc_avg(reader, col_name)
    return result


def calc_avg(reader: csv.DictReader, col_name: str) -> list[dict[str, str]]:
    """"""
    total = 0
    count = 0
    result = []
    for row in reader:
        if col_name in row:
            value = float(row[col_name])
            total += value
            count += 1
        result.append({'country': row['country'], col_name: row[col_name]})
    return result

print(read_csv('../../data/economic1.csv', 'population'))



