def task_11(n: int) -> str:
    """Функция для решения задачи 1.1"""
    if 100 <= n <= 200:
        return f'Число {n} попадает в диапазон от 100 до 200'
    if 200 < n <= 300:
        return f'Число {n} попадает в диапазон от 200 до 300'
    return f'Число {n} не попадает ни в один диапазон'


def task_12(t: int) -> str:
    """Функция для решения задачи 1.2"""
    cnt = 0
    while t <= 100:
        t += .5
        cnt += 1
    return str(cnt) + ' мин\n'


def task_13(n: int) -> str:
    """Функция для решения задачи 1.3"""
    s = '\n'
    for i in range(n + 1):
        s += f'{i + 1}. 000\n'
    return s


def task_14(n: int) -> str:
    """Функция для решения задачи 1.4"""
    s = '\n'
    for i in range(n):
        s += '*' * (i + 1) + '\n'
    return s


def task_21(a: int, b: int, c: int, m: int, k: int) -> str:
    """Функция для решения задачи 2.1"""
    box = sorted([a, b, c])
    door = sorted([m, k])
    if box[0] <= door[0] and box[1] <= door[1]:
        return 'Коробка войдет в дверь\n'
    return 'Коробка не войдет в дверь\n'


def task_22(n: int) -> str:
    """Функция для решения задачи 2.2"""
    s = '\n'
    for i in range(1, n + 1):
        s += '*' * i + '\n'
    for i in range(n - 1, 0, -1):
        s += '*' * i + '\n'
    return s


def task_23(n: int) -> str:
    """Функция для решения задачи 2.3"""
    s = ''
    i = 1
    while i ** 2 < n:
        s += str(i ** 2) + ' '
        i += 1
    return s + '\n'


def task_31(n: int) -> str:
    """Функция для решения задачи 3.1"""
    fives = n // 5
    remainder = n % 5

    while fives >= 0:
        if remainder % 3 == 0:
            return f'Можно купить {n} шариков мороженого'
        else:
            fives -= 1
            remainder += 5
    return f'Нельзя купить {n} шариков мороженого'


def task_32(s1: int, p: int, s2: int) -> str:
    """Функция для решения задачи 3.2"""
    cnt = 0
    while s1 < s2:
        s1 += s1 * p / 100
        cnt += 1
    return f'{cnt}\n'


def task_33(n: int) -> str:
    """Функция для решения задачи 3.3"""
    return str(sum(map(int, str(n))))


def get_result_string(func, key: str, value: list) -> str:
    """Функция для формирования результирующей строки

    :param func: функция, выполняющая задание
    :param key: ключ из словаря входных данных
    :param value: значение ключа из словаря входных данных
    :return: результирующая строка
    """
    result = f'{key}\n' \
             f'Входные данные: {value}\n' \
             f'Результат: {func(*value)}\n'
    print(result)
    return result


# Парсим данные из файла input.txt
input_data: dict[str, list[int]] = {}
with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        if line.startswith('Задача'):
            key = line.strip()
            input_data[key] = []
        else:
            input_data[key].append(int(line.strip()))

# Расчет и вывод и сохранение результата
with open('output.txt', 'w', encoding='utf-8') as file:
    for key, value in input_data.items():
        match key:
            case 'Задача 1.1':
                s = get_result_string(task_11, key, value)
                file.write(s + '\n')
            case 'Задача 1.2':
                s = get_result_string(task_12, key, value)
                file.write(s + '\n')
            case 'Задача 1.3':
                s = get_result_string(task_13, key, value)
                file.write(s)
            case 'Задача 1.4':
                s = get_result_string(task_14, key, value)
                file.write(s + '\n')
            case 'Задача 2.1':
                s = get_result_string(task_21, key, value)
                file.write(s + '\n')
            case 'Задача 2.2':
                s = get_result_string(task_22, key, value)
                file.write(s + '\n')
            case 'Задача 2.3':
                s = get_result_string(task_23, key, value)
                file.write(s + '\n')
            case 'Задача 3.1':
                s = get_result_string(task_31, key, value)
                file.write(s + '\n')
            case 'Задача 3.2':
                s = get_result_string(task_32, key, value)
                file.write(s + '\n')
            case 'Задача 3.3':
                s = get_result_string(task_33, key, value)
                file.write(s + '\n')
