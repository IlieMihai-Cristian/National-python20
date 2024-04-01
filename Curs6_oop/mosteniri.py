# Inheritance (unul din cele 4 concepte fundamentale din OOP) pe langa abstractism, incapsulare, polimorfism


# class Example:
#
#     def __init__(self, val=24):
#         self.first = val
#         self.aaa = 'ION'
#
#     def set_second(self, valoare):
#         self.second = valoare
#         return self.second
#
#
# obj_1 = Example()
# # print(obj_1.set_second(4))
# print(obj_1.__dict__)  # propritatile obiectului instantiat
# obj_1.third = 5
# print(obj_1.__dict__)


# class Example:
#
#     def __init__(self, val=24):
#         self.__first = val
#         self.aaa = 'ION'
#
#     def set_second(self, valoare):
#         self.second = valoare
#         return self.second
#
#
# obj_1 = Example()
# # print(obj_1.__first)
# # print(obj_1.__dict__)
# print(obj_1._Example__first)
# print(obj_1.__dir__())


# class Example:
#
#     __counter = 0   # val incrementata cu 1 fata de cate ori este instantiat obiectul
#
#     def __init__(self, val=1):
#         self.__first = val    # val din instantiere obj
#         Example.__counter += 1
#         self.__counter += 1
#
#
# obj_1 = Example()
# obj_2 = Example(2)
# obj_3 = Example(100)
#
# print(obj_1.__dict__, obj_1._Example__counter)
# print(obj_2.__dict__, obj_2._Example__counter)
# print(obj_3.__dict__, obj_3._Example__counter)


# class Example:
#     __counter = 0
#
#     def __init__(self, val=1):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 2
#
#
# object_1 = Example()
# print(hasattr(object_1, 'a'))
# print(hasattr(object_1, 'b'))
# try:
#     print(object_1.a)
# except AttributeError:
#     pass
# try:
#     print(object_1.b)
# except AttributeError:
#     pass


# class Example:
#     __counter = 0
#
#     def __init__(self, val=1):
#         if val % 2 != 0:
#             self.a = 1
#             Example.a = 5
#         else:
#             self.b = 2
#
#
# object_1 = Example()
# print(object_1.__dict__)
# print(Example.__dict__)


# class Example:
#     __counter = 0
#
#     def __init__(self, val=1):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 2
#
#
# object_1 = Example()
# print(object_1.a)
# print(getattr(object_1, 'a'))


class Example:

    def __init__(self, val):
        self.val = val


ob1 = Example(0)
ob2 = Example(0)
ob3 = ob1
ob3.val += 1

# print(ob1 is ob2)
# print(ob1 is ob3)
# print(ob2 is ob3)
# print(ob1.val, ob2.val, ob3.val)  # 0, 2, 1  (0, 2, 0), (1, 2, 1)
# print(id(ob1.val))
# print(id(ob2.val))
# print(id(ob3.val))


# a = 10
# b = 20
# c = 10
#
# print(a is c)

# aa = (1, 2, 3)
# bb = (2, 2, 3)
# cc = (1, 2, 3)
#
# print(aa is cc)


""" MOSTENIRI """


class Vehicule:
    pass


class Masini(Vehicule):
    pass


class MasiniDeTeren(Masini):
    pass


# print(issubclass(MasiniDeTeren, Vehicule))
# print(issubclass(Vehicule, MasiniDeTeren))

vehicul_1 = Vehicule()
masina_1 = Masini()
masina_de_teren_1 = MasiniDeTeren()

# print(isinstance(masina_1, MasiniDeTeren))
# print(isinstance(masina_1, Masini))
# print(isinstance(masina_1, Vehicule))


""" Rescriere metode """


# class SuperClasa:
#     def __init__(self, name='Ion'):
#         self.name = name
#
#     def __str__(self):
#         return f' Numele meu este {self.name}'
#
#
# class SubClasa(SuperClasa):
#     # def __init__(self, name):
#     #     self.name = name
#     # super(SuperClasa, self).__init__(name):
#     #     super().__init__(name)
#
#     def __init__(self, name='George'):
#         super().__init__(name)
#
#     def __str__(self):
#         return f' Print {self.name}'
#
#
# object_1 = SubClasa('Vasile')
# print(object_1)



# class SuperClasa:
#
#     super_variabila = 'super'
#
#     def __init__(self, name='Ion'):
#         self.name = name
#
#     def __str__(self):
#         return f' Numele meu este {self.name}'


# class SubClasa(SuperClasa):
#
#     sub_variabila = 'sub'
#
#     def __init__(self, name='George'):
#         super().__init__(name)
#
#     def __str__(self):
#         return f' Print {self.name}'


# object_1 = SubClasa()
# # print(object_1.sub_variabila)
# print(object_1.super_variabila)



class SuperClasa:

    super_variabila = 'super'
    sub_variabila = 'sub_parinte'

    def __init__(self, name='Ion', var=55):
        self.name = name
        self.var_init = 30

    def __str__(self):
        return f' Numele meu este {self.name}'


class Mijloc:
    variabila_mijloc = 3
    super_variabila = 'mijloc'


class SubClasa(Mijloc, SuperClasa):

    sub_variabila = 'sub'
    super_variabila = 'super_copil'

    def __init__(self, profesor='George', var=22):
        super().__init__(profesor, var)
        # self.var_init = 12

    def __str__(self):
        return f'Print {self.name}'


object_1 = SubClasa()
print(object_1)

