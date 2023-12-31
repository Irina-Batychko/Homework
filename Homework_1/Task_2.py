"""Задача №2
 Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч."""

number = int(input("Введите целое число от 0 до 100 000: "))

if number < 0 or number > 100000:
    print('Вы ввели число вне диапазона! Введите целое число от 0 до 100 000 ;)')
elif number <= 1:
    print(f"Число {number} является исключением")
else:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print('Число является простым')
    else:
        print('Число является составным')
