def in_range(n: int, start: int, end: int) -> bool:
    """Return True if n is in the range [start, end], else False."""
    return start <= n <= end


def task_11(n: int) -> str:
    """Return a message indicating whether n is in the range [100, 200] or (200, 300] or neither."""
    if in_range(n, 100, 200):
        return f"Число {n} попадает в диапазон от 100 до 200"
    elif in_range(n, 201, 300):
        return f"Число {n} попадает в диапазон от 200 до 300"
    else:
        return f"Число {n} не попадает ни в один диапазон"


def task_12(t: int) -> str:
    """Return the number of minutes it takes for t to reach or exceed 100 by increasing by 0.5 each minute."""
    cnt = 0
    for i in range(t, 100, 1):
        cnt += 1
    return f"{cnt} мин\n"


def task_13(n: int) -> str:
    """Return a string of n lines, each containing a number."""
    return "\n".join([f"{i}. 000" for i in range(1, n + 1)])


def task_14(n: int) -> str:
    """Return a string of n lines, each containing a number of asterisks."""
    return "\n".join(["*" * (i + 1) for i in range(n)])


def task_21(a: int, b: int, c: int, m: int, k: int) -> str:
    """Return a message indicating whether a box with dimensions a x b x c can fit through a door with dimensions m x k."""
    box = sorted([a, b, c])
    door = sorted([m, k])
    if box[0] <= door[0] and box[1] <= door[1]:
        return "Коробка войдет в дверь\n"
    else:
        return "Коробка не войдет в дверь\n"


def task_22(n: int) -> str:
    """Return a string of 2n-1 lines, each containing a number of asterisks."""
    lines = []
    for i in range(1, n + 1):
        lines.append("*" * i)
    for i in range(n - 1, 0, -1):
        lines.append("*" * i)
    return "\n"
