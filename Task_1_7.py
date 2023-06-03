# Задание 1 - 7
# 📌 Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# 📌 Для цифры верните её квадрат, например 5 - 25
# 📌 Для двузначного числа произведение цифр, например 30 - 0
# 📌 Для трёхзначного числа его зеркальное отображение, например 520 - 25
# 📌 Если число не из диапазона, запросите новое число
# 📌 Откажитесь от магических чисел
# 📌 В коде должны быть один input и один print

n = 0

while n < 1 or n > 999:
    n = int(input("Введите число от 1 до 999: "))

if 0 < n < 10:
    text = "Введена цифра. Квадрат цифры"
    a = n ** 2
elif 9 < n < 100:
    text = "Введено двухзначное число. Произведение цифр числа"
    a = (n // 10) * (n % 10)
else:
    text = "Введено трехзначное чило. Зеркальное отображение числа"
    n1 = n 
    a = ''
    for i in str(n):
        n2 = n1 % 10
        a = a + str(n2)
        n1 = n1 // 10

print(text, str(n) + ":", a)