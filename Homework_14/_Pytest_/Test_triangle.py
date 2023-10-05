
import pytest
from Task_3_pytest import check_triangle

def test_check_triangle_equilateral():
    assert check_triangle(5, 5, 5) == "Равносторонний треугольник"

def test_check_triangle_isosceles():
    assert check_triangle(5, 5, 3) == "Равнобедренный треугольник"
    assert check_triangle(5, 3, 5) == "Равнобедренный треугольник"
    assert check_triangle(3, 5, 5) == "Равнобедренный треугольник"

def test_check_triangle_scalene():
    assert check_triangle(3, 4, 5) == "Разносторонний треугольник"

def test_check_triangle_invalid():
    assert check_triangle(1, 1, 3) == "Треугольник с такими сторонами не существует"
    assert check_triangle(0, 0, 0) == "Треугольник с такими сторонами не существует"


if __name__ == '__main__':
    pytest.main(['-v'])