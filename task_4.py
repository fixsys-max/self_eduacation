import pytest


def task_11(n: int) -> str:
    """Функция для решения задачи 1.1"""
    if 100 <= n <= 200:
        return f'Число {n} попадает в диапазон от 100 до 200'
    if 200 < n <= 300:
        return f'Число {n} попадает в диапазон от 200 до 300'
    return f'Число {n} не попадает ни в один диапазон'


def task_12(t: int) -> str:
    """Функция для решения задачи 1.2"""
    if t in range(101):
        cnt = 0
        while t <= 100:
            t += .5
            cnt += 1
    else:
        raise ValueError
    return str(cnt - 1) + ' мин\n'


def task_13(n: int) -> str:
    """Функция для решения задачи 1.3"""
    if 0 <= n <= 100:
        s = '\n'
        for i in range(n):
            s += f'{i + 1}. 000\n'
    else:
        raise ValueError
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
    if s1 < s2 and p > 0:
        cnt = 0
        while s1 < s2:
            s1 += s1 * p / 100
            cnt += 1
    else:
        raise ValueError
    return f'{cnt}\n'


def task_33(n: int) -> str:
    """Функция для решения задачи 3.3"""
    if not isinstance(n, int):
        raise TypeError
    return str(sum(map(int, str(n).strip(' -'))))


def get_result_string(func, key: str, value: list) -> str:
    """Функция для формирования результирующей строки

    :param func: функция, выполняющая задание
    :param key: ключ из словаря входных данных
    :param value: значение ключа из словаря входных данных
    :return: результирующая строка
    """
    result = f'{key}\n' \
             f'Входные данные: {", ".join(map(str, value))}\n' \
             f'Результат: {func(*value)}\n'
    print(result)
    return result + '\n'


if __name__ == '__main__':
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
                    file.write(get_result_string(task_11, key, value))
                case 'Задача 1.2':
                    file.write(get_result_string(task_12, key, value))
                case 'Задача 1.3':
                    file.write(get_result_string(task_13, key, value))
                case 'Задача 1.4':
                    file.write(get_result_string(task_14, key, value))
                case 'Задача 2.1':
                    file.write(get_result_string(task_21, key, value))
                case 'Задача 2.2':
                    file.write(get_result_string(task_22, key, value))
                case 'Задача 2.3':
                    file.write(get_result_string(task_23, key, value))
                case 'Задача 3.1':
                    file.write(get_result_string(task_31, key, value))
                case 'Задача 3.2':
                    file.write(get_result_string(task_32, key, value))
                case 'Задача 3.3':
                    file.write(get_result_string(task_33, key, value))


################################## Unit Tests ###################################
#                                                                               #
#   Update this repository from GitHub with command 'git pull origin main'      #
#   Install pytest with command 'pip install pytest'                            #
#   Check if the pytest.ini file exists in the project directory.               #
#                                                                               #
#   For run tests enter command: pytest -s -v --tb=line task_4.py               #
#                                                                               #
#################################################################################


class TestTask11:
    """Unit tests for task 1.1"""

    @pytest.mark.positive
    @pytest.mark.parametrize('input_data', [100, 150, 200])
    def test_input_in_range_100_200(self, input_data):
        assert task_11(input_data) == f'Число {input_data} попадает в диапазон от 100 до 200'

    @pytest.mark.positive
    @pytest.mark.parametrize('input_data', [201, 250, 300])
    def test_input_in_range_200_300(self, input_data):
        assert task_11(input_data) == f'Число {input_data} попадает в диапазон от 200 до 300'

    @pytest.mark.positive
    @pytest.mark.parametrize('input_data', [99, 301, 1555])
    def test_input_not_in_ranges_100_200_and_200_300(self, input_data):
        assert task_11(input_data) == f'Число {input_data} не попадает ни в один диапазон'

    @pytest.mark.negative
    @pytest.mark.parametrize('input_data', ['123', [123], {'n': 123}])
    def test_invalid_input(self, input_data):
        try:
            result = task_11(input_data)
        except TypeError as Er:
            result = Er
        assert isinstance(result, TypeError)


class TestTask12:
    """Unit tests for task 1.2"""

    @pytest.mark.positive
    @pytest.mark.parametrize('input_data, expected_result', [(0, 200), (50, 100), (100, 0)])
    def test_correct_temperature_input(self, input_data, expected_result):
        result = task_12(input_data)
        expected_result = f"{expected_result} мин\n"
        assert result == expected_result, f"{result} :: {expected_result}"

    @pytest.mark.negative
    @pytest.mark.parametrize('input_data', [-1, 101, 300])
    def test_incorrect_temperature_input(self, input_data):
        try:
            result = task_12(input_data)
        except ValueError as Er:
            result = Er
        assert isinstance(result, ValueError)

    @pytest.mark.negative
    @pytest.mark.parametrize('input_data', ['50', [75], {'t': 300}])
    def test_invalid_type_data_input(self, input_data):
        try:
            result = task_11(input_data)
        except TypeError as Er:
            result = Er
        assert isinstance(result, TypeError)


class TestTask13:
    """Unit tests for task 1.3"""
    @pytest.mark.positive
    @pytest.mark.parametrize('input_data, expected_result', [(0, '\n'),
                                                             (2, '\n1. 000\n2. 000\n'),
                                                             (5, '\n1. 000\n2. 000\n3. 000\n4. 000\n5. 000\n')])
    def test_correct_input(self, input_data, expected_result):
        assert task_13(input_data) == expected_result

    @pytest.mark.negative
    @pytest.mark.parametrize('input_data', [-1, -50, 101])
    def test_incorrect_input(self, input_data):
        try:
            result = task_12(input_data)
        except ValueError as Er:
            result = Er
        assert isinstance(result, ValueError)

    @pytest.mark.negative
    @pytest.mark.parametrize('input_data', ['12', [5], {'n': 10}])
    def test_invalid_type_data_input(self, input_data):
        try:
            result = task_11(input_data)
        except TypeError as Er:
            result = Er
        assert isinstance(result, TypeError)


class TestTask21:
    """Unit tests for task 2.1"""

    @pytest.mark.positive
    @pytest.mark.parametrize('input_data, expected_result', [([2, 3, 4, 4, 3], 'Коробка войдет в дверь\n'),
                                                             ([5, 6, 7, 1, 2], 'Коробка не войдет в дверь\n')])
    def test_correct_input(self, input_data, expected_result):
        assert task_21(*input_data) == expected_result

    @pytest.mark.negative
    @pytest.mark.parametrize('input_data', [['2', 3, 4, 4, 3],
                                            [2, 3, 4, [4], 3]])
    def test_invalid_data_type(self, input_data):
        try:
            result = task_11(*input_data)
        except TypeError as Er:
            result = Er
        assert isinstance(result, TypeError)


class TestTask23:
    """Unit tests for task 2.3"""

    @pytest.mark.positive
    @pytest.mark.parametrize('input_data, expected_result', [(10, '1 4 9 \n'),
                                                             (30, '1 4 9 16 25 \n'),
                                                             (40, '1 4 9 16 25 36 \n')])
    def test_correct_input(self, input_data, expected_result):
        assert task_23(input_data) == expected_result

    @pytest.mark.negative
    @pytest.mark.parametrize('input_data', ['20', {'n': 15}, [44]])
    def test_invalid_data_type(self, input_data):
        try:
            result = task_11(input_data)
        except TypeError as Er:
            result = Er
        assert isinstance(result, TypeError)


class TestTask31:
    """Unit tests for task 3.1"""

    @pytest.mark.positive
    @pytest.mark.parametrize('input_data, expected_result', [(8, 'Можно купить 8 шариков мороженого'),
                                                             (11, 'Можно купить 11 шариков мороженого'),
                                                             (7, 'Нельзя купить 7 шариков мороженого')])
    def test_correct_input(self, input_data, expected_result):
        assert task_31(input_data) == expected_result

    @pytest.mark.negative
    @pytest.mark.parametrize('input_data', ['20', {'n': 15}, [44]])
    def test_invalid_data_type(self, input_data):
        try:
            result = task_31(input_data)
        except TypeError as Er:
            result = Er
        assert isinstance(result, TypeError)


class TestTask32:
    """Unit tests for task 3.2"""

    @pytest.mark.positive
    @pytest.mark.parametrize('input_data, expected_result', [([1000, 3, 2000], '24\n'),
                                                             ([1000, 5, 2000], '15\n')])
    def test_correct_input(self, input_data, expected_result):
        assert task_32(*input_data) == expected_result

    @pytest.mark.negative
    @pytest.mark.parametrize('input_data', [[10000, 5, 5000],
                                            [1000, -3, 2000]])
    def test_incorrect_input(self, input_data):
        try:
            result = task_32(*input_data)
        except ValueError as Er:
            result = Er
        assert isinstance(result, ValueError)

    @pytest.mark.negative
    @pytest.mark.parametrize('input_data', ['20', {'n': 15}, [44]])
    def test_invalid_data_type_input(self, input_data):
        try:
            result = task_32(*input_data)
        except TypeError as Er:
            result = Er
        assert isinstance(result, TypeError)


class TestTask33:
    """Unit tests for task 3.2"""

    @pytest.mark.positive
    @pytest.mark.parametrize('input_data, expected_result', [(123, '6'),
                                                             (456, '15'),
                                                             (-222, '6')])
    def test_correct_input(self, input_data, expected_result):
        assert task_33(input_data) == expected_result

    @pytest.mark.negative
    @pytest.mark.parametrize('input_data', ['20', {'n': 15}, [44]])
    def test_invalid_data_type_input(self, input_data):
        try:
            result = task_33(input_data)
        except TypeError as Er:
            result = Er
        assert isinstance(result, TypeError)
