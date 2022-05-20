kids = input("Скільки у вас учнів: ")
ap = input("Скільки у вас яблук: ")

result1 = (int(ap) // (int(kids)))
result2 = (int(ap) % (int(kids)))


print(result1, " яблку дістанеться кожному учню.")
print(result2, " яблук залишиться в кошику.")