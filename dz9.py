# #DZ 9
import random

numb_list = [random.randint(1, 100) for i in range(20)]
z = []
for i in numb_list:
    z.append(i)

#Варіант 1
# if z[1] > z[0]:
#     if z[1] > z[2]:
#         print(z[1],)
#print(numb_list)


#Варіант 2
#c = 0
# for i, e in enumerate(numb_list, 1):
# 
#     if e[i - 1] < e[i] > e[i +1]:
#         #c += 1
#         #print(i, e)
# print(c)
# print(numb_list)
