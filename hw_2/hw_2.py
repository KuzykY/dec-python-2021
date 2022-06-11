# написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - второй возвращает все записи
#
# запишите 5 тудушек и выведете все
#
# - первый записывает в эту переменную запись

def notebook():
    todo_list = []

    def add_todo():
        pass

    def get_all():
        pass


# 3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)
# Пример:
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
def expanded_form(n):
    result = []
    for index, digit in enumerate(str(n)[::-1]):
        if int(digit) != 0:
            result.append(digit + ('0' * index))
    return ' + '.join(result[::-1])

print(expanded_form(132))

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