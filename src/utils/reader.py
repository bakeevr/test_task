import csv


def read_csv(path: str) -> list[dict[str, str]]:
    """
    Функция считавает csv файл и возвращает список словарей
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            result = [elem for elem in reader]
            return result
    except PermissionError as err:
        print(f'Доступ {err.filename} к файлу запрещен')
        exit(-5)


