# ###
set_1 = {1,2,3,4}
set_2 = {2,3,4,5,6, 'gg'}
set_3 = {2,3, 'gg'}
set_4 = {2,'gg',4}
supset = set_2 > set_3
sup_set = set_4 > set_2
if supset is True:
    print('Являється суперменом')
elif supset is not True:
    print('Не являється суперменом')

print(supset)
print(sup_set)
# d = set_2.issuperset(set_3)
# print(d)