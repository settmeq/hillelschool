
while True:

    def money():
        money = int(input("скільки у вас грошей? :"))
        if money == 0:
            print('stay home')
        elif money >= 10:
            print('go to Silpo')
        elif money >= 9:
            print('go to ATB')
        elif money >= 8:
            print('go to Ashan')
        else:
            print('done func money')

    def money1():
        money = int(input("скільки у вас грошей? :"))

        if money == 0:
            print('stay home')
        if money >= 10:
            print('go to Silpo')
        if money >= 9:
            print('go to ATB')
        if money >= 8:
            print('go to Ashan')
    ### money - elif, money1 - if

    a = input("Ввести money або money1 :")
    if str(a) == "money":
        money()
    if str(a) == "money1":
        money1()

print("END")
