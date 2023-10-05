"""
Задача №1 (unittest)
Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
2-5 тестов на задание в трёх вариантах:
doctest,
unittest,
pytest.

Задача №1 из семинара 1
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""
import unittest


def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Равносторонний треугольник"
        elif a == b or a == c or b == c:
            return "Равнобедренный треугольник"
        else:
            return "Разносторонний треугольник"
    else:
        return "Треугольник с такими сторонами не существует"


class TestDetermineTriangleType(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertEqual(check_triangle(5, 5, 5), 'Равносторонний треугольник')

    def test_isosceles_triangle(self):
        self.assertEqual(check_triangle(4, 4, 5), 'Равнобедренный треугольник')

    def test_scalene_triangle(self):
        self.assertEqual(check_triangle(3, 4, 5), 'Разносторонний треугольник')

    def test_invalid_triangle(self):
        self.assertEqual(check_triangle(1, 2, 3), 'Треугольник с такими сторонами не существует')


if __name__ == '__main__':
    unittest.main(verbosity=2)