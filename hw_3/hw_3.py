# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон

# class Rectangle:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y
#         self.area = x * y
#
#     def __add__(self, other):
#         return self.area + other.area
#
#     def __sub__(self, other):
#         return self.area - other.area
#
#     def __eq__(self, other):
#         return self.area == other.area
#
#     def __ne__(self, other):
#         return self.area != other.area
#
#     def __lt__(self, other):
#         return self.area < other.area
#
#     def __gt__(self, other):
#         return self.area > other.area
#
#     def __len__(self):
#         return self.x * 2 + self.y * 2
#
#
# r1 = Rectangle(10, 10)
# r2 = Rectangle(13, 13)
#
# print(r1 + r2)
# print(r1 - r2)
# print(r1 == r2)
# print(r1 != r2)
# print(r1 < r2)
# print(r1 > r2)
# print(len(r1))
# print(len(r2))
#
# создать класс Human (name, age)
# создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# у принца имя, возраст и размер найденной туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую
#
# в классе золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# и метод класса который будет показывать это количество

class Human:
    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name

    def __str__(self):
        return self.name, self.age

    def __repr__(self):
        return self.__str__()


class Cinderella(Human):
    count = 0

    @classmethod
    def inc_count(cls):
        cls.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    def __init__(self, name: str, age: int, size: int):
        super().__init__(name, age)
        self.size = size
        Cinderella.inc_count()

    def __str__(self):
        return f'{super().__str__()} ({self.size})'


class Prince(Human):
    def __init__(self, name: str, age: int, size: int):
        super().__init__(name, age)
        self.size = size

    def __str__(self):
        return f'{super().__str__()} ({self.size})'

    def find(self, find_list: list[Cinderella]):
        for cinderella in find_list:
            if cinderella.size == self.size:
                return cinderella
        return None

prince = Prince('Max', 25, 35)
cinderellas_list = [Cinderella('Kira', 22, 34), Cinderella('Anna', 25, 35), Cinderella('Olya', 26, 36)]

print(prince)
print(cinderellas_list)
print(prince.find(cinderellas_list))
print(Cinderella.get_count())