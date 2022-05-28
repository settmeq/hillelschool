#dz 5

nums = []
while True:
    inpt = int(input('Введіть число: '))
    if inpt == ' ':
        break
    n = inpt
    if n != 0:
        nums.append(n)

    else:

        paired = [i for i in nums if i % 2 == 0]
        unpaired = [i for i in nums if i % 2 != 0]
        count = sum(nums)
        f = count / len(nums)
        print(f, ' <--- середнє арефметичне')
        print(len(paired), ' <---парні', len(unpaired), '<---непарні')
        max_dig = max(nums)
        min_dig = min(nums)
        print(min_dig, '<---мінімальне значення', max_dig,'<---максимальне значення')
        break