#  mutabile: liste, seturi si dictionare
#  imutabile: numere, stringuri, tupluri

""" tuplurile sunt colectii de obiecte si sunt imutabile si ordonabile (indexabile). Permit elemente duplicate"""

var_tuplu = ()
var_tuplu_a = tuple()

""" ordonarea """  # la fel ca la liste

"""pot contine o varietate de elemente"""  # la fel ca la liste

"""concatenare"""  # la fel ca la liste

"""multiplicare"""  # la fel ca la liste

"""lungimea unei liste len()"""  # la fel ca la liste

"""indexare"""  # la fel ca la liste

"""slicing"""

"""copierea unui tuplu"""

# tuple_3 = (1, 2.5, 'Ana', '22', False, None, 'int', 'len')
# tuple_copy = tuple_3[:]
# print(tuple_copy is tuple_3)

"""operator in si not in"""  # la fel ca la liste
# print("Ana" in tuple_3)
# print("An" in tuple_3)


"""declarare multipla"""
tuple_names = ('Mihai', 'Andrei', 'George')
# (name_1, name_2, name_3) = tuple_names
# print(name_1)
# print(name_2)
# print(name_3)
tuple_names_2 = ('Mihai', 'Andrei', 'George', 'Irina', 'Razvan')
(name_1, *name_2, name_3) = tuple_names_2
# print(name_2)

"""tupluri intretesute(nested)"""  # la fel ca la liste

nested_tuple = ('a', (3, ('22', 16, None), ('mere', False)), (3.55, ), 0)
# print(nested_tuple[2][0])
# print(nested_tuple[1][1][2])

# x = (3.55, )
# print(type(x))


""" cateva metode ptr tupluri """

# count
# print(tuple_names.count(1))

# index
# print(tuple_names.index('George'))


# ex = list(tuple_names_2)
# print(ex, type(ex))