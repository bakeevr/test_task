import csv


def read_csv(path: str) -> list[dict[str, str]]:
    """
    Функция считавает csv файл и возвращает список словарей
    """
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        result = [elem for elem in reader]
    return result


