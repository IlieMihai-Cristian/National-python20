""" dictionarele sunt colectii de obiecte si sunt mutabile si ordonabile (indexabile, incepand cu Python 3.7). Nu permit elemente duplicat"""

# var_dict = dict()
# var_dict_a = {}

var_dict = {'cheie_1': 'valoare_1', 'cheie_2': 'valoare_2'}

var_dict_1 = {1: 'a', 'a': 1, "list": [1, '2', 'trei', 4.4], 'dict': {'dict_2': 4}}
var_dict_2 = {1: bool, 2: str}

"""lungimea len()"""
# print(len(var_dict_1))

"""indexare"""
# print(var_dict['cheie_2'])

"""dictionare intretesute"""
ex_dict = {'key_1': {'key_2': {'key_3': ['a', 1.1, [333, (23, )]]}, 'key_4': 10}, 'key_5': 'key_6'}
# print(ex_dict['key_1']['key_2']['key_3'][2][1][0])

"""adaugare elemente noi"""
var_dict_3 = {'key_1': 1, 'key_2': 2}
var_dict_3['key_3'] = 3
# print(var_dict_3)
# var_dict_3['key_4'] = 4
# print(var_dict_3)


"""cateva metode la dict"""
# clear
# var_dict_3.clear()
# print(var_dict_3)

# get
# print(var_dict_3['key_4'])
# print(var_dict_3.get('key_4', 'Nu am cheie!'))

# items()
# print(var_dict_3.items())

# keys()
# print(var_dict_3.keys())

# values()
# print(var_dict_3.values())

# pop
# print(var_dict_3.pop('key_1'))
# print(var_dict_3)

# popitem
# print(var_dict_3.popitem())
# print(var_dict_3)

# update
dict_2 = {'key_5': 5}
var_dict_3.update(dict_2)
print(var_dict_3)