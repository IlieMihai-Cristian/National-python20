""" seturile sunt colectii de obiecte si sunt imutabile si neordonabile (neindexabile). Nu permit duplicate"""

var_set = set()
# var_set_1 = {1, "2", 5, 2, 4, '1'}

# print(set('AbcbbcA'))
# print(var_set_1)

""" permite orice tip de element dar sa fie imutabil"""

# var_set_2 = {10, '22', 44.3, (2, 4, 6)}
# print(var_set_2)
# var_set_3 = {10, '22', 44.3, [2, 4, 6]}
# print(var_set_3)

list_demo = [1, 2, 3, 1, 5, 2, 4, 5, 2]
# print(list(set(list_demo)))

"""lungimea unui set len()"""

"""operator in si not in"""

"""operatii in seturi"""

var_set_1 = {'a', 'b', 'c'}
var_set_2 = {'a', 'e', 'f'}

# UNION  - preia toate elementele fara duplicate
# var 1
# print(var_set_1.union(var_set_2))
# # var 2
# print(var_set_1 | var_set_2)

# print(var_set_1 | ('a', 'e', 'f'))
# print(var_set_1 .union(('a', 'e', 'f')))


# INTERSECTION  - preia elementele comune
# var 1
# print(var_set_1.intersection(var_set_2))
# # var 2
# print(var_set_1 & var_set_2)

# var_set_3 = var_set_1.intersection(var_set_2)
# print(var_set_3)


# DIFFERENCE  - returneaza elementele din primul set si care nu se regasesc in al doilea set
# var 1
# print(var_set_1.difference(var_set_2))
# # var 2
# print(var_set_1 - var_set_2)

var_set_1 = {'a', 'b', 'c'}
var_set_2 = {'a', 'e', 'f'}

# SYMETRIC DIFFERENCE  - returneaza elementele care sunt fie in primul fie in al doilea set si nu sunt comune
# var 1
# print(var_set_1.symmetric_difference(var_set_2))
# # var 2
# print(var_set_1 ^ var_set_2)


# var_set_1.update(var_set_2)
# print(var_set_1)

# var_set_1.add('d')
# print(var_set_1)

# var_set_1.remove('x') # eroare
# print(var_set_1)

# var_set_1.discard('x')
# print(var_set_1)

# var_set_1.pop()
# print(var_set_1)

var_set_1.clear()
print(var_set_1)
