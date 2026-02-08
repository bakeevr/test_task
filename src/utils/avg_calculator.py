from collections import defaultdict


def calc_avg(data: list[dict[str, str]], col_name: str) -> dict[str, int]:
    """
    Функция принимает список словарей и имя столбца и
    возвращает словарь с найденным средним значением по столбу
    для каждой страны
    """
    grouped = defaultdict(list)
    for item in data:
        grouped[item['country']].append(item[col_name])
    result = {}
    for country, values in grouped.items():
        try:
            values = [int(i) for i in values]
            result[country] = round(sum(values) / len(values), 2)
        except ValueError as err:
            print(f'Файл содержит некорректные данные {err.args}')
    return result
