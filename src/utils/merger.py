def merge_data(*data: dict[str, int]) -> dict[str, int]:
    """
    Функция принимает словари и возвращает общий словарь
    """
    result = {}
    for d in data:
        if isinstance(d, dict):
            result.update(d)
    return result



