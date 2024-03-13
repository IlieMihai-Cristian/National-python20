""" Functia Lambda """
# - se mai numeste si functie anonima (fara def/ fara nume)
# pot avea oricate argumente dar o singura expresie. Expresia este concomitent evaluata si returnata

element = lambda x: x * 10  # unde x este argumentul si x * 10 este expresia

def element_1(x):
    return x * 10

# print(element(10))
# print(element_1(10))

# element_2 = lambda x, y: x + y
# print(element_2(11, 21))


""" FILTER """
# Fct. Filter intoarce un obiect al clasei filter (care este defapt un iterator) rezultat prin aplicarea unei functii
# fiecarui element dintr-un obiect iterabil (lista, tuplu ...)

# program care sa returneze o lista cu nr pare dintr-o lista initiala

list_1 = [1, 5, 3, 6, 8, 12, 4, 3, 11]
list_2 = list(filter(lambda x: (x % 2 == 0), list_1))
# print(list_2)
# print(type(list_2))
# print(list(list_2))

# ex: cu for loop
list_2bis = []
for i in list_1:
    if i % 2 == 0:
        list_2bis.append(i)
# print(list_2bis)

# ex: cu def
def filtrare(var):
    if var % 2 == 0:
        return True
    else:
        return False
# print(filtrare)

# apelare = filter(filtrare, list_1)
# print(list(apelare))

# print(list(range(1, 100)))

"""MAP"""

# Fct. MAP intoarce un obiect al clasei map (care este defapt un iterator) rezultat prin aplicarea unei functii
# fiecarui element dintr-un obiect iterabil (lista, tuplu ...)

# program care sa dubleze fiecare element dintr-o lista folosind map si lambda
list_1 = [1, 5, 3, 6, 8, 12, 4, 3, 11]
# list(filter(lambda x: (x % 2 == 0), list_1))
list_3 = list(map(lambda x: x * 2, list_1))
# print(list_3)


""" ZIP """

# Fct. ZIP preia parametrii iterabili (pot fi 0 sau mai multi) si returneaza un obiect al clasei zip
# (care este defapt un iterator) sub forma de tupluri, formate din grupuri de elemente provenite din parametrii initiali
# Lungimea finala a obiectului iterabil este egala cu lungimea celei mai scurte structuri initiale


list_wit_int = [1, 2, 3, 4, 5]
list_with_strings = ['one', 'two', 'three', 'four', 'five']
# var = []
# var_2 = list()
# result = zip()
# print(list(result))

# result = list(zip(list_wit_int, list_with_strings))
# list_with_decimals = [1.1, 2.2, 3.3, 4.4, 5.5]
#
# result_3 = list(zip(list_wit_int, list_with_strings, list_with_decimals))
# print(result_3)
# print(dict(zip(list_wit_int, list_with_strings)))

""" UNZIP """
# * cu zip
result = zip(list_wit_int, list_with_strings)
# print(list(result))
val_1, val_2 = zip(*list(result))
# print('val1 = ', list(val_1))
# print('val2 = ', list(val_2))


""" COMPREHENSION LIST """

var = 'comprehension'

# print(list(var))
# caz cu forloop
# list_for_loop = []
# for elem in var:
#     list_for_loop.append(elem)
# print(list_for_loop, 100)
#
#
# # caz cu lambda:
# list_lambda = list(map(lambda x: x, var))
# print(list_lambda, 105)
#
# # caz cu comprehension:
# list_string = [elem for elem in var]
# print(list_string, 109)
#
# number_list = []
# for x in range(20):
#     if x % 2 == 0:
#         number_list.append(x)
#
# print(number_list)
#
# number_list_2 = [x for x in range(20) if x % 2 == 0]
# print(number_list_2)
# # lista_noua = [expresie(element) for element in iterabil if conditie]
#
# number_list_3 = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]  # cand am o singura conditie trec la sfarsit
# print(number_list_3)
#
# number_list_4 = ['Par' if var % 2 == 0 else 'Impar' for var in range(20)] # cand am ternar trec in fata
# print(number_list_4)

""" COMPREHENSION DICTIONARY """

# square_dict = dict()
# for num in range(1, 11):
#     square_dict[num] = num * num
# print(square_dict)
#
# square_comprehension = {num: num * num for num in range(1, 11)}
# print(square_comprehension)

# print(isinstance(40, float))
# print(issubclass((40, 12), tuple))


a = [41, 45]
b = [1, 41]
c = [41, 45]

# print(any(i in a for i in b))
# print(all(i in a for i in c))

# value = eval('2 + 2')
# print(value)

value_2 = eval('{1: 2}')
print(value_2)
print(type(value_2))