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
    cnt_a, cnt_b = Counter(arr_a), Counter(arr_b)
    return {e for e in set(arr_a + arr_b)
            if cnt_a[e] > 1 or cnt_b[e] > 1}

def task_2(arr_a: List[int], arr_b: List[int]) -> Set[int]:
    """Элементы, повторяющиеся в B, но ровно 1 раз в A."""
    cnt_a, cnt_b = Counter(arr_a), Counter(arr_b)
    return {e for e in cnt_b if cnt_b[e] > 1 and cnt_a[e] == 1}

def task_3(arr_a: List[int], arr_b: List[int]) -> Set[int]:
    """Элементы из A, отсутствующие в B."""
    return set(arr_a) - set(arr_b)

def main() -> None:
    """Основная функция программы"""
    pass  # Заглушка, будет реализовано позже

if __name__ == '__main__':
    main()