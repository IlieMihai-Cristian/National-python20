"""Declaratia IF"""

# if expresie:
#     instructiune (set de instructiuni)

first_number = 10
second_number = 20

# if first_number > second_number:
#     print('intra pe linia 10')
#
# if first_number < second_number:
#     print('intra pe linia 13')


# list_ex = ['rosu', 'galben', 'albastru']
#
# if 'galben' in list_ex:
#     print('expresia este adevarata')  # 1
#     if first_number > second_number:
#         print('a intrat pe primul if din interior expresie')
#     if first_number <= second_number:
#         print('a intrat pe al doilea if din interior expresie') # 2
#         print('mesaj 2')  # 3
#     print('mesaj 3')  # 4
# print('mesaj 4')  # 5



# if expresie:
#     instructiune (set de instructiuni)
# else:
#     instructiune (set de instructiuni)

# var_nr = 50
#
# if var_nr > 50:
#     print('nr este mai mare de 50')
# else:
#     print('nr. este mai mic de 50')


nume = 'Ion'

# if nume == 'Radu':
#     print('nume is Radu')
# elif nume == 'George':
#     print('nume is George')
# elif nume == 'Ion':
#     pass
#     # print('nume is Ion')
# else:
#     print('nume e altul')


"""operator ternar"""

# valoare 1 if expresie else valoare 2

var = 'cuvant'
var_2 = 10 if 'cug' in var else 20
# print(var_2)

# if 'cuv' in var:
#     var_2 = 10
# else:
#     var_2 = 20
# print(var_2)

var_2 = 20
if 'cuv' in var:
    var_2 = 10

""" FOR LOOP """

# for <variabila temporara> in <iterabil>:
# instructiune

# print(andrei)
# list_ex = ['unu', 'doi', 'trei', 'patru']
# for andrei in list_ex:
#     if andrei == 'doi':
#         print(andrei)
#     else:
#         print('aici nu executa')
# print(andrei)


var_dict = {'key_1': 1, 'key_2': 2, 'key_3': 3}
# for x in var_dict:
#     print(x)

# for x in var_dict.keys():
#     print(x)

# for x, y in var_dict.items():
#     print(f'Cheia {x} -> are valoarea {y}')
# print(x, y)

""" ENUMERATE """
list_ex = ['unu', 'doi', 'trei', 'patru']

# for idx, elem in enumerate(list_ex, start=101):
#     # print(idx+1, ':', elem)
#     print(idx, ':', elem)


""" RANGE """
# for x in range(2, 10, 2):
#     print(x)


"""BREAK si CONTINUE"""

# for animal in ['cat', 'dog', 'horse', 'pig', 'hen']:
    # if animal.startswith('h'):
    #     break -> intrerupe total iteratia
    # print(animal)
    # if animal.startswith('h'):
    #     continue  # -> sare elementul iterat
    # print(animal)


""" FOR poate sa aiba si ELSE"""
# for animal in ['cat', 'dog', 'horse', 'pig', 'hen']:
#     print(animal)
#     break
# else:
#     print('ok')


"""WHILE LOOP"""
# nr = 5
# while nr > 0:
#     nr -= 1
#     # nr = nr - 1
#     print(nr)


# nr = 0
# while nr > 0:
#     nr -= 1
#     # nr = nr - 1
#     print(nr)

animal = ['cat', 'dog', 'horse', 'pig', 'hen']
while animal:
    animal.pop(-1)
    print(animal)
