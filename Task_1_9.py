# Задание 1 - 9
# 📌 Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

for i in range(2, 10):
    for j in range(2, 11):
        print(i, "X", j, "=", i*j)
    print()