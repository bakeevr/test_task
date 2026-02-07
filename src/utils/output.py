from tabulate import tabulate


def output_table(data: list[tuple[int, str, int]], headers) -> None:
    print(tabulate(data, headers=headers, tablefmt="simple", numalign="right", stralign="left"))