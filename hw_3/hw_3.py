# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон

class Rectangle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.area = x * y

    def __add__(self, other):
        return self.area + other.area

    def __sub__(self, other):
        return self.area - other.area

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __len__(self):
        return self.x * 2 + self.y * 2


r1 = Rectangle(10, 10)
r2 = Rectangle(13, 13)

print(r1 + r2)
print(r1 - r2)
print(r1 == r2)
print(r1 != r2)
print(r1 < r2)
print(r1 > r2)
print(len(r1))
print(len(r2))