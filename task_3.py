print('1 задание. Калькулятор')
a = input('Введите число а: ')
b = input('Введите число b: ')
oper = input('Введите операцию: ').lower().replace('div', '//').replace('mod', '%').replace('pow', '**')

try:
    print(f'Результат: {eval(a + oper + b)}')
except ZeroDivisionError:
    print('На ноль делить нельзя')


print('\n\n2 Задание')
a, b = int(input('Введите первое число: ')), int(input('Введите второе число: '))
print(f'{a} делится на {b}' if not a % b else f'{a} не делиться на {b}')
print(f'{b} делится на {a}' if not b % a else f'{b} не делиться на {a}')


print('\n\n3 Задание')
print('Есть одинаковые цифры' if len(set(input("Введите трехзначное число: "))) < 3 else 'Нет одинаковых цивр')
