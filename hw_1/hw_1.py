# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому
# s = input('Enter str:')
#
# print(','.join([i for i in s if i.isdigit()]))

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# s = input('Enter str:')
#
# print(','.join(''.join([i if i.isdigit() else ' ' for i in s]).split()))

# list comprehension
#
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting = 'Hello, world'
# print([i.upper() for i in greeting])

# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# l = [i ** 2 for i in range(50) if i % 2 != 0]
# print(l)

# function
#
# - створити функцію яка виводить ліст

# def list_(l):
#     print(l)

# - створити функцію яка приймає три числа та виводить та повертає найменьше.

# def min_(a,b,c):
#     res=min(a,b,c)
#     print(res)
#     return res

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def max_(a,b,c):
#     res=max(a,b,c)
#     print(res)
#     return res

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def max_min(*args):
#     print(max(args))
#     return min(args)

# - створити функцію яка виводить ліст

# def list_(l):
#     print(l)

# - створити функцію яка повертає найбільше число з ліста

# def max_of_list(l):
#     return max(l)

# - створити функцію яка повертає найменьше число з ліста

# def min_of_list(l):
#     return min(l)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# def sum_of_list(l):
#     res=sum(l)
#     return res

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# def avg_of_list(l):
#     res=sum(l)/len(l)
#     return res

# 1)Дан лист:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]

# l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

#   - найти min число в листе

# def min_of_list(l):
#     res = min(l)
#     return res
# print(min_of_list(l))

#   - удалить все дубликаты в листе

# def duplicate(l):
#     res=list(set(l))
#     return res
# print(duplicate(l))

#   - заменить каждое четвертое значение на "Х"
# def x(l):
#     for i in range(3,len(l),4):
#         l[i]='X'
#     print(l)
# x()
# print(l)

# 4) переделать первое задание под меню с помощью цикла

# while True:
#     l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#     print('1) Min of list')
#     print('2) Delete duplicate')
#     print('3) Change every 4 value to X ')
#     print('0) Exit')
#     choise=input('Make you choise:')
#     if choise=='1':
#         print(min_of_list(l))
#     elif choise=='2':
#         print(duplicate(l))
#     elif choise=='3':
#         print(x(l))
#     elif choise=='0':
#         break

# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:

# def square(n):
#     for i in range(n):
#         if i == 0 or i == n - 1:
#             print('*' * n)
#         else:
#             print('*' + ' ' * (n - 2) + '*')
#
# square(20)

# 3) вывести табличку умножения с помощью цикла while

# i = j = 1
#
# while i < 10:
#     j = 1
#     while j < 10:
#         multiplication = i * j
#         print(multiplication, end='')
#         print('  ' if multiplication // 10 else '   ', end='')
#         j += 1
#     i += 1
#     print()
