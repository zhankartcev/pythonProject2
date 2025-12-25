from collections import Counter
from typing import List, Set

def parse_int_list(prompt: str) -> List[int]:
    """Парсит строку с числами, разделёнными пробелами, в список целых чисел."""
    while True:
        raw = input(prompt).strip()
        if not raw:
            print('Пустая строка. Попробуйте ещё раз.')
            continue
        try:
            return [int(x) for x in raw.split()]
        except ValueError:
            print('Можно вводить только числа через пробел.')

def task_1(arr_a: List[int], arr_b: List[int]) -> Set[int]:
    """Элементы, встречающиеся >1 раза в A или B."""
    pass  # Заглушка, будет реализовано позже

def task_2(arr_a: List[int], arr_b: List[int]) -> Set[int]:
    """Элементы, повторяющиеся в B, но ровно 1 раз в A."""
    pass  # Заглушка, будет реализовано позже

def task_3(arr_a: List[int], arr_b: List[int]) -> Set[int]:
    """Элементы из A, отсутствующие в B."""
    pass  # Заглушка, будет реализовано позже

def main() -> None:
    """Основная функция программы"""
    pass  # Заглушка, будет реализовано позже

if __name__ == '__main__':
    main()