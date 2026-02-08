from utils.reader import read_csv
from utils.merger import merge_data
from utils.avg_calculator import calc_avg
from utils.output import output_table
from utils.parser import args

PATH = 'data/'
data = args
res = args.files
report = args.avg[8:]
result = []

try:
    for d in res:
        result.append(calc_avg(read_csv(f"{PATH}{d}"), report))
except FileNotFoundError as err:
    print('Файл с данным именем не найден!\n'
          'Проверьте правильность имени файла',
          err.filename)
    exit(-3)

l = merge_data(*result)

table_data = [
    (i + 1, country, gdp) for i, (country, gdp) in enumerate(l.items())
]

headers = ["country", report]
output_table(table_data, headers=headers)
exit(0)