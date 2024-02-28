# from functii import calc, variabila
# print(calc(10))
# #
# # val = test_func(5)
# # print(val)
#
# from functii import calc as ca
# print(ca(10))

# #
# # val = functie_noua(9)
# # print(val)
#
# # from functii import variabila
# #
# # print(variabila)
#
# from try_except import *
# from functii import *
# print(variabila)

# import functii as fu
# print(fu.variabila)
# print(fu.calc(20))
#
# print(fu.__file__)


""" ce sunt pachetele """
import os
import sys

# import Curs2_conditionari_and_loops.exemplu_fisier_pachete as pachet
# print(pachet.suma_ex(1, 2, 3, 4))

# print(sys.path)
# print(type(sys.path))
# print(pachet.__file__)
path_curs2 = '/home/mihai/SIIT/National-python20'
sys.path.insert(0, path_curs2)
# print(sys.path)
#
# import Curs2_conditionari_and_loops.exemplu_fisier_pachete as pachet
# print(pachet.suma_ex(1, 2, 3, 4))


# BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE)

from Curs1_data_structures.dictionare import dict_2
print(dict_2)