# написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - второй возвращает все записи
#
# запишите 5 тудушек и выведете все
#
# - первый записывает в эту переменную запись
#
# def notebook():
#     todo_list=[]
#     def add_todo(todo):
#         todo_list.append(todo)
#     def get_all():
#         return todo_list
#     return add_todo,get_all
#
# add_todo,get_all=notebook()
#
# add_todo("wake up")
# add_todo('brush your teeth')
# add_todo('listen to a lecture')
# add_todo('do homework')
# add_todo('go sleep')
#
# print(get_all())

# 2) протипизировать первое задание
#
#
def notebook() -> [str]:
    todo_list = []

    def add_todo(todo: str) -> None:
        todo_list.append(todo)

    def get_all() -> list[str]:
        return todo_list

    return add_todo, get_all


add_todo, get_all = notebook()

add_todo("wake up")
add_todo('brush your teeth')
add_todo('listen to a lecture')
add_todo('do homework')
add_todo('go sleep')

print(get_all())

# 3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)
# Пример:
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

# def expanded_form(n):
#     result = []
#     for i, d in enumerate(str(n)[::-1]):
#         if int(d) != 0:
#             result.append(d + ('0' * i))
#     return ' + '.join(result[::-1])
#
# print(expanded_form(132))

# 4)создать декоратор который будет считать сколько раз была запущена функция
# и будет выводит это значение после каждого запуска функции

# def counter(func):
#     def wraper(*args, **kwargs):
#         wraper.count += 1
#         print(wraper.count)
#         func(*args, **kwargs)
#         print('-----------')
#     wraper.count = 0
#     return wraper
#
#
# @counter
# def func1():
#     print('func1')
#
#
# @counter
# def func2():
#     print('func2')
#
#
# func1()
# func1()
# func1()
# func2()
# func2()


# сделайте функцию на замыкания
# которая будет возвращать декоратор который будет считать общее количество запущенных  функций декорированных этим декоратором
#
# from typing import Callable
#
#
# def wrap_decor():
#     def decor(func: Callable, func_calls: dict[Callable] = {}) -> Callable:
#         func_calls[func] = 0
#
#         def wrapper() -> None:
#             func_calls[func] += 1
#             print('count:', sum(func_calls.values()))
#             func()
#             print('----------------------------------------')
#
#         return wrapper
#
#     return decor
#
#
# decor = wrap_decor()
#
#
# @decor
# def func1() -> None:
#     print('func1')
#
#
# @decor
# def func2() -> None:
#     print('func2')
#
#
# func1()
# func1()
# func2()
# func2()
# func1()

# вивести послідовність Фібоначі, кількість вказана в знінній,
#   наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#   (число з послідовності - це сума попередніх двох чисел)
#
# def fibonacci(n: int) -> str:
#     num1 = num2 = 1
#     list_num = [str(num1), str(num2)]
#     for i in range(2, n):
#         num1, num2 = num2, num1 + num2
#         list_num.append(str(num2))
#     return ' '.join(list_num)
#
#
# print(fibonacci(30))


# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3

# def ene(n: int) -> str:
#     e = ne = 0
#     for i in str(n):
#         if int(i) % 2:
#             ne += 1
#         else:
#             e += 1
#     return f'even numbers={e},non-even numbers={ne}'
#
#
# print('********************************************')
# print(ene(46368))


# прога, що виводить кількість кожного символа з введеної строки,
#   наприклад:
#   st = 'as 23 fdfdg544' #введена строка

# def symbol_counter(string: str) -> None:
#     total = {}
#     for i in range(len(string)):
#         counter = total.get(string[i], 0) + 1
#         total.update({string[i]: counter})
#     for k, v in total.items():
#         print(f'\'{k}\' -> {v}')
#
#
# symbol_counter('as 23 fdfdg544')


# генерируем лист с непарных чисел в порядке возрастания [1,3,5,7,9.....n]
# задача сделать c него лист листов такого плана:
#
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  => [ [1], [3,5], [7,9,11], [13,15,17,19] ]
# [1, 3, 5, 7, 9, 11] => [[1], [3, 5], [7, 9, 11]]
# [1, 3, 5, 7, 9]  => [ [1], [3,5], [7,9]]
# [1, 3, 5, 7, 9, 11, 13]  => [[1], [3, 5], [7, 9, 11], [13]]

def list_ne(size: int = 0):
    return [i for i in range(size * 2) if i % 2]
