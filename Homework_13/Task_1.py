"""
Задача №1
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации. Поднимайте исключения внутри основного кода.
Например нельзя создавать прямоугольник со сторонами отрицательной длины.

Задача №1 из семинара 1
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""


class NegativeLengthError(Exception):
    def init(self, name, value):
        self.name = name
        self.value = value

    def str(self):
        return f'Сторона треугольника {self.name} = {self.value}, а должна быть больше 0.'


class TriangleError(Exception):
    def init(self, message='Треугольник с такими сторонами не существует'):
        self.message = message
        super().init(self.message)

    def str(self):
        return self.message


def classify_triangle(a, b, c):
    if a <= 0:
        raise NegativeLengthError("a", a)
    elif b <= 0:
        raise NegativeLengthError("b", b)
    elif c <= 0:
        raise NegativeLengthError("c", c)
    if a + b <= c or a + c <= b or b + c <= a:
        raise TriangleError()
    if a == b == c:
        print("Равносторонний треугольник")
    elif a == b or a == c or b == c:
        print("Равнобедренный треугольник")
    else:
        print("Разносторонний треугольник")


if __name__ == '__main__':
    classify_triangle(2, 3, 4)
