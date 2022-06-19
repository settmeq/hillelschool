import random
import string


def gen_dict():
    dictionary = dict()
    while len(dictionary) < 10:
        rand_letter = random.choice(string.ascii_letters.lower())
        rand_number = random.randint(0, 9)
        dictionary.update({rand_letter: rand_number})
    return dictionary


def final_dict(d_1, d_2):
    new_dict = d_1.copy()
    for key, value in d_1.items():
        for key_1, value_2 in d_2.items():
            if key_1 not in new_dict.keys() or (key_1 == key and value_2 > value):
                new_dict.update({key_1: value_2})
    return new_dict


dict_1 = gen_dict()
dict_2 = gen_dict()
dict_3 = final_dict(dict_1, dict_2)

print(dict_1, dict_2, dict_3, sep='\n')