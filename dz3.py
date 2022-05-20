#Домашнє завдання №3

classA = input("Кількість учнів в А класі: ")
classB = input("Кількість учнів в B класі: ")
classC = input("Кількість учнів в C класі: ")

result0 = ((int(classA) + int(classB) + int(classC)))
result1 = ((int(classA) + int(classB) + int(classC)) // 2)
result2 = ((int(classA) + int(classB) + int(classC)) % 2)
result3 = result1 + result2

print("кількість  учнів :", result0)
print("потрібно закупити: ", result3, " парт")
