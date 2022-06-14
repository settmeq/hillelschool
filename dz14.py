# Написать функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
# sq = input()
sq = int(input())


def square(sq):
    perim = sq * 4
    pl = sq ** 2
    d = 2 * sq ** 0.5
    return perim, pl, d


res_1 = square(sq)
square(sq)
print(res_1)