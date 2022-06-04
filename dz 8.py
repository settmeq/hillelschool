# dz8
import random

petya = int(input("Введіть ріст Петі:"))

numb_list = [random.randint(150, 200) for i in range(15)]
numb_list.append(petya)
numb_list.sort(reverse=True)

ind = numb_list.index(petya) + 1
ss = numb_list.count(petya)

for i, e in enumerate(numb_list, 1):
    if e == petya:
        continue
if ss > 1:
    pos = ind + ss - 1
    print(pos, '<-- Місце петі в строю')
if ss <= 1:
    print(ind, '<-- Місце петі в строю')



print(numb_list)
