from utils.reader import read_csv
from utils.merger import merge_data
from utils.avg_calculator import calc_avg
from utils.output import output_table


data = ['../data/economic1.csv', '../data/economic2.csv']


res = []
for d in data:
    res.append(calc_avg(read_csv(d), 'gdp'))

l = merge_data(*res)

table_data = [
    (i + 1, country, gdp) for i, (country, gdp) in enumerate(l.items())
]

headers = ["country", "gdp"]
output_table(table_data, headers=headers)