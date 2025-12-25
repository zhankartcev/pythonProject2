from collections import Counter
from typing import List, Set

def parse_int_list(prompt: str) -> List[int]:
    """Парсит строку с числами, разделёнными пробелами, в список целых чисел.

    Args:
        prompt (str): Приглашение для ввода чисел.

    Returns:
        List[int]: Список целых чисел, введённых пользователем.
    """
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
    """Элементы, встречающиеся >1 раза в A или B.

    Args:
        arr_a (List[int]): Первый список чисел.
        arr_b (List[int]): Второй список чисел.

    Returns:
        Set[int]: Множество элементов, встречающихся более одного раза в A или B.
    """
    count_a, count_b = Counter(arr_a), Counter(arr_b)
    return {e for e in set(arr_a + arr_b)
            if count_a[e] > 1 or count_b[e] > 1}

def task_2(arr_a: List[int], arr_b: List[int]) -> Set[int]:
    """Элементы, повторяющиеся в B, но ровно 1 раз в A.

    Args:
        arr_a (List[int]): Первый список чисел.
        arr_b (List[int]): Второй список чисел.

    Returns:
        Set[int]: Множество элементов, повторяющихся в B, но ровно 1 раз в A.
    """
    count_a, count_b = Counter(arr_a), Counter(arr_b)
    return {e for e in count_b if count_b[e] > 1 and count_a[e] == 1}

def task_3(arr_a: List[int], arr_b: List[int]) -> Set[int]:
    """Элементы из A, отсутствующие в B.

    Args:
        arr_a (List[int]): Первый список чисел.
        arr_b (List[int]): Второй список чисел.

    Returns:
        Set[int]: Множество элементов из A, отсутствующих в B.
    """
    return set(arr_a) - set(arr_b)

def main() -> None:
    """Основная функция программы"""
    menu = (
        '\n=== МЕНЮ ===\n'
        '1 – Элементы, повторяющиеся в A или B\n'
        '2 – Повторяющиеся в B, но 1 раз в A\n'
        '3 – Есть в A, но нет в B\n'
        '0 – Выход\n'
    )
    actions = {'1': task_1, '2': task_2, '3': task_3}

    while True:
        choice = input(menu + 'Ваш выбор: ').strip()
        if choice == '0':
            print('Пока!')
            break
        if choice not in actions:
            print('Некорректный ввод.')
            continue

        first = parse_int_list('Введите массив A: ')
        second = parse_int_list('Введите массив B: ')
        result = actions[choice](first, second)
        print(f'Результат: {sorted(result) if result else "пусто"}')

if __name__ == '__main__':
    main()