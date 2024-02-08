#  mutabile: liste, seturi si dictionare
#  imutabile: numere, stringuri, tupluri

""" listele sunt colectii de obiecte si sunt mutabile si ordonabile (indexabile). Permit elemente duplicate"""

var_list = []
var_list_a = list()

""" ordonarea """
# listele care au aceleasi elemente dar ordine diferita -> liste diferite
list_1 = [1, 2, 3, 4]
list_2 = [2, 1, 3, 4]

# print(list_1 == list_2)

"""pot contine o varietate de elemente"""

# list_3 = [1, 2.5, 'Ana', '22', False, None, int, len]

"""concatenare"""

# print([1, 2] + [3, 4])

"""multiplicare"""

# print([1, 2] * 5)

"""lungimea unei liste len()"""

# print(len(list_3))

"""indexare"""

# print(list_3[4])

"""slicing"""
list_3 = [1, 2.5, 'Ana', '22', False, None, 'int', 'len']
# print(list_3[2:-5])
# print(list_3[::-1])

"""copierea unei liste"""

# list_copy = list_3[:]
# print(list_copy is list_3)

# list_copy = list_3.copy()
# print(list_copy is list_3)

# list_copy = list_3
# print(list_copy is list_3)

"""operator in si not in"""
# print("Ana" in list_3)
# print("An" in list_3)


"""liste intretesute(nested)"""

# nested_list = ['a', [3, ['22', 16, None], ['mere', False]], [3.55], 0]
# # print(nested_list[2][0])
# print(nested_list[1][1][2])

"""mutabilitate"""

# list_3 = [1, 2.5, 'Ana', '22', False, 1]
# list_3[-2] = [1, 3]
# print(list_3)

""" cateva metode ptr liste """

# count
# print(list_3.count(1))

# min si max
list_4 = [45, 34.5, '2', 10*2, 88.88]
# print(max(list_4))
# print(min(list_4))

# list_5 = ['ana', 'are', 'mere', 'si', 'pere']
# print(max(list_5))
# print(min(list_5))

# del
# list_5[1:2] = ['nu', 'ssss', 'fructele']
# print(list_5)
# list_6 = [1, 2, 3]
# list_6[0:1] = [11, 22, 33]
# print(list_6)

# append
# list_5.append('orice')
# print(list_5)

# extend
# list_5.extend(['ok', 10])
# print(list_5)

# insert
# list_5.insert(2, 'gigel')
# print(list_5)

# list_5 = ['ana', 'are', 'mere', 'si', 'pere']
# list_5 += 'ion'
# print(list_5)

# remove
# list_5.remove('si')
# print(list_5)

# pop
# list_temp = list_5.pop()
# print(list_temp, list_5)

# list_5.pop(1)
# print(list_5)

# clear
# list_5.clear()
# print(list_5)

# sort
# list_5.sort(reverse=True)
# print(list_5)

# reverse
list_5 = ['ana', 'are', 'mere', 'si', 'pere']
list_5.reverse()
# print(list_5)

# print(dir(list_5))

a = ''
# print(dir(a))
