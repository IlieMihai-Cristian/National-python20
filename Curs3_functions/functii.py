# """ Definitia generala a functiilor """
#
# # def nume_functie(parametru/parametrii):
# #     set instructiuni
#
# # def my_function():
# #     var = 'Rezultat'
# #     return var
# #
# # func = my_function()
# # print(func)
#
# """ Incapsulare """
#
# """ Namespace """
#
#
# # def my_function_2():
# #     var_2 = 10
# #     return var_2
# #
# #
# # out = my_function_2()
# # print(out)
# # print(var_2)
#
#
# """Parametrii si Argumentele functiilor"""
#
# def func(nume, cantitate, device):
#     result = f'{nume} a comandat {cantitate} bucati din categoria {device}'
#     return result
#
#
# # info = func('Mihai', 20, 'calculatoare')
# # print(info)
#
# # print(func('Cristian', 10))
# # print(func('Cristian', 10, 'tablete', 30))
#
#
# """ Argumente Keyword"""
#
# # print(func(nume='Mihai', cantitate=4, device='telefoane'))
# # print(func(device='telefoane', nume='Mihai', cantitate=4))
# # print(func(device='telefoane', nume='Mihai', numar=4))
#
# # print(func('Mihai', device='telefoane', cantitate=30))
# # print(func(40, device='telefoane', nume='Mihai'))  -> crapa
# # print(func(device='telefoane', 'Mihai', cantitate=30))  -> crapa
#
#
# """ Parametrii Default (standard)"""
#
# def func_2(nume='Radu', cantitate=100, device='ceasuri'):
#     result = f'{nume} a comandat {cantitate} bucati din categoria {device}'
#     return result
#
#
# # print(func_2())
# # print((func_2('Ion', 40)))
# # print((func_2(cantitate=111)))
# # print(func_2('Alina', device='monitoare'))
# # print(func_2('Alina', nume='monitoare')) -> crapa
#
# """
# REZUMAT:
# CAZ 1: parametrii pozitionali: def func(a, b, c)
#
#     1. argumentre pozitionale func(10, 20, 30) -> conteaza ca numarul si ordinea argumentelor = cei ai parametrilor
#     2. argumente keyword func(c=10, b-30, a=20) -> nu conteaza ordinea dar conteaza nr argum. = nr. param.
#     3. argumente mix func(10, c=20, b=30) -> intotdeauna pozitional si pe urma punem keyword
#
# CAZ 2: parametrii default: def func(a=1, b=2, c=3)
#
#     1. argumentre pozitionale func(10, 20, 30) -> conteaza ca numarul argumentelor <= nr. parametrii
#     2. argumente keyword func(c=10, b-30, a=20) -> nu conteaza ordinea dar conteaza ca numarul argumentelor <= nr. parametrii
#     3. argumente mix func(10, c=20, b=30) -> intotdeauna pozitional si pe urma punem keyword si conteaza ca numarul argumentelor <= nr. parametrii
#
# CAZ 3: parametrii mix: def func(a, b=5, c=7) -> se respecta ordinea cu parametrii pozitionali primii
#                                                 unde avem parametrii pozitionali se respecta regulile de la CAZ 1
#                                                 unde avem parametrii default se respecta regulile de la CAZ 2
# """
#
#
#
# """ return """
#
#
# # def calc(x):
# #     if x < 0:
# #         return
# #     if x > 0:
# #         return
# #     print(x)
# #     return
# #
# #
# # res = calc(0)
# # print(res)
#
#
# """ ANOTARI """
#
# # def calcul(a: int = 0, b: int = 0, c: int = 0):
# #     return a + b + c
#
# # print(calcul())
# # print(calcul(10))
# # print(calcul('10', '20', '30'))
#
# def calcul(a: int = 0, b: int = 0, c: int = 0) -> int:
#     """
#     :param a:
#     :param b:
#     :param c:
#     :return:
#     """
#     return a + b + c
#
#
# """ args si kwargs """
#
# # args
#
# # def suma(a, b=0, *args):
# #     print(type(args))
# #     return a + b
#
# # var = suma(1, 2, 3, 4, 5, 6)
# # print(var)
#
# def suma(a, b=0, *args):
#     initial = a + b
#     total = 0
#     for elem in args:
#         total = total + elem
#     return initial + total
#
# result = suma(1, 2, 3, 4, 5, 6, 1000)
# # print(result)
#
#
# # ---------------------------------------------
# # kwargs
#
# def suma_2(a, b=0, *args, **kwargs):
#     # print(type(kwargs))
#     initial = a + b
#     total = 0
#     for elem in args:
#         total = total + elem
#     for key, value in kwargs.items():
#         # print(key, value)
#         total += value  # acelasi lucru cu total =  total + value
#     return initial + total
#
#
# # result_2 = suma_2(1, 2, 3, 4, nume=5, device=6)
# # print(result_2)
#
#
# result_2_1 = suma_2(1, 2, c=7, d=8, e=9)
# # print(result_2_1)
# # result_2_2 = suma_2(1, 2, 3, c=7, d=8, e=9, 10, 11)
# # result_2_3 = suma_2(1, 2, 3, c=7, a=8, b=9)
#
#
# def suma_3(a, b=0, *args, **kwargs):
#     # print(type(kwargs))
#     initial = a + b
#     total_args = 0
#     for elem in args:
#         total_args += elem
#     total_kwargs = 0
#     for key, value in kwargs.items():
#         total_kwargs += value
#     return initial, total_args, total_kwargs
#
#
# result_initial, result_args, result_kwargs = suma_3(1, 2, 3, 4, nume=5, device=6)
# # print(result_initial, ':', result_args, ':', result_kwargs)
#
#
# """ RECURSIVITATE """
#
# def test_func(nr):
#     if nr > 100:
#         return nr
#     else:
#         print(f'Nr. este acum {nr}')
#         return test_func(nr+10)
#
#
# val = test_func(3)
# print(val)

def calc(x):
    return x * x


variabila = 'AAA'
