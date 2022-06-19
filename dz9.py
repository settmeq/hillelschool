# #DZ 9

digs = list(map(int, input('Введіть числа: ').split()))
c = 0
for i in range(1, len(digs) - 1):
    if digs[i - 1] < digs[i] > digs[i + 1]:
        c += 1
print("кількість елементів: ", c)




