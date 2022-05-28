#z5(2)
max_range = int(input())
n = range(1, max_range)
for i in n:
    dub = i ** 2
    if dub <= max_range:
        print(dub, end=' ')

