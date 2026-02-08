from tabulate import tabulate


def output_table(data: list[tuple[int, str, int]], headers) -> None:
    if data:
        print(tabulate(data, headers=headers, tablefmt="simple", numalign="right", stralign="left"))
    else:
        print('Не данных для вывода')
        exit(-4)