try:
    from utils.reader import read_csv
    from utils.merger import merge_data
    from utils.avg_calculator import calc_avg
    from utils.output import output_table
    from utils.parser import parser
except ImportError:
    from src.utils.reader import read_csv
    from src.utils.merger import merge_data
    from src.utils.avg_calculator import calc_avg
    from src.utils.output import output_table
    from src.utils.parser import parser


def main():
    args = parser.parse_args()

    PATH = "data/"
    res = args.files
    report = args.avg[8:]
    result = []

    try:
        for d in res:
            result.append(calc_avg(read_csv(f"{PATH}{d}"), report))
    except FileNotFoundError as err:
        print(
            "Файл с данным именем не найден!\n" "Проверьте правильность имени файла",
            err.filename,
        )
        exit(-3)

    merge_dict = merge_data(*result)

    table_data = [
        (i + 1, country, gdp) for i, (country, gdp) in enumerate(merge_dict.items())
    ]

    headers = ["country", report]
    output_table(table_data, headers=headers)
    exit(0)


if __name__ == "__main__":
    main()
