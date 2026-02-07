from reader import read_csv
from avg_calculator import calc_avg

def merge_data(*data: dict[str, int]) -> dict[str, int]:
    """
    Функция принимает словари и возвращает общий словарь
    """
    result = {}
    for d in data:
        result.update(d)
    return result



