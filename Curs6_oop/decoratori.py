# class Dog:
#
#     legs_no = 4
#
#     def __init__(self, name):
#         self.name = name
#
#     # def __str__(self):
#     #     return self.name



# caine = Dog("Rex")
# print(caine)
# print(caine.name)
# print(caine.legs_no)
# print(Dog.legs_no)

# ---------------------------------------------------------

# class Dog:
#
#     legs_no = 4
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def change_name(self, name):
#         self.name = name
#         return self.name
#
#
# caine = Dog("Rex")
# print(caine.change_name('Rex1'))

# ---------------------------------------------------------

# class Dog:
#
#     legs_no = 4
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def change_name(self, name):
#         self.name = name
#         return self.name
#     @staticmethod    # decorator
#     def speak():
#         return 'Ham, ham, ham'


# caine = Dog("Rex")
# print(caine.speak())
# print(Dog.speak())
# print(Dog.change_name('Max'))


# _________________________________________________


# class Dog:
#
#     legs_no = 4
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property  # decorator care ne ajuta sa putem seta o metoda a clasei (ca atirbut/proprietate)
#     def nume(self):
#         return self.__name  # returneaza proprietatea privata a instantei
#
#     def __str__(self):
#         return self.__name


# caine = Dog("Rex")
# # print(caine.name)
# # print(caine._Dog__name)
# print(caine.nume)


# _________________________________________________


# class Dog:
#
#     legs_no = 4
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def nume(self):
#         return self.__name
#     @nume.setter
#     def nume(self, nume_schimbat):
#         self.__name = nume_schimbat
#
#     def __str__(self):
#         return self.__name


# caine = Dog("Rex")
# print(caine.nume)
# caine.nume = 'Max'
# print(caine.nume)



# _________________________________________________

# class Dog:
#
#     legs_no = 4
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def nume(self):
#         return self.__name
#
#     @nume.setter
#     def nume(self, nume_schimbat):
#         self.__name = nume_schimbat
#
#     @nume.deleter
#     def nume(self):
#         del self.__name
#
#     def __str__(self):
#         return self.__name
#
#
# caine = Dog("Rex")
# print(caine.nume)
# print(caine.__dict__)
# caine.nume = 'Max'
# print(caine.nume)
# print(caine.__dict__)
# del caine.nume
# print(caine.__dict__)




# _________________________________________________


# def decorator_simplu(parametru):
#     print(f'Apelam functia {parametru.__name__}')
#     return parametru
#
#
# @decorator_simplu   # decorator_simplu()
# def functie_simpla():
#     return 'Buna seara!'
#
#
# # print(functie_simpla())


# _________________________________________________

# def decorator_depozit(functia_noastra): # parametrul "functia_noastra" echivaleaza denumirea functiei decorate
#     def ambalaj(carte):  # parametrul "carte" echivaleaza parametrul functiei decorate
#         return f'Ambalare produs {functia_noastra.__name__} ce contine cartea cu titlul {carte}'
#     return ambalaj
#
# @decorator_depozit
# def impachetare_carti(nume):
#     return nume


# print(impachetare_carti('Moara cu Noroc'))


# _________________________________________________


# def decorator_depozit(material): # parametrul "material" echivaleaza parametrul decoratorului
#     def ambalaj(functia_noastra):  # parametrul "functia_noastra" echivaleaza denumirea functiei decorate
#         def ambalaj_interior(carte):  # parametrul "carte" echivaleaza parametrul functiei decorate
#             return f'Ambalare produs {functia_noastra.__name__} cu ambalaj din material {material} ce contine cartea cu titlul {carte}'
#         return ambalaj_interior
#     return ambalaj
#
#
# # @decorator_depozit('hartie')
# @decorator_depozit
# def impachetare_carti(nume):
#     return nume
#
#
# print(impachetare_carti('Moara cu Noroc'))

# _________________________________________________

# def decorator_depozit(material): # parametrul "material" echivaleaza parametrul decoratorului
#     def ambalaj(functia_noastra):  # parametrul "functia_noastra" echivaleaza denumirea functiei decorate
#         def ambalaj_interior(*carte):  # parametrul "carte" echivaleaza parametrul functiei decorate
#             return f'Ambalare produs {functia_noastra.__name__} cu ambalaj din material {material} ce contine cartea cu titlul: {", ".join(carte)}'
#         return ambalaj_interior
#     return ambalaj
#
#
# @decorator_depozit('hartie')
# def impachetare_carti(*nume):
#     return nume
#
#
#
# print(impachetare_carti('Moara cu Noroc', 'Ion'))

# _________________________________________________


# def decorator(functie):
#     def functie_upper(parametru):
#         return parametru.upper()
#     return functie_upper
#
# @decorator
# def functie(propozitie):
#     return propozitie
#
# print(functie('Ana are mere'))`


# _________________________________________________
import time

def execution_time(function_target):
    def wrapper(param):
        start = time.time()
        function_target(param)
        end = time.time()
        return f'Execution time: {end - start} and result is {function_target(param)}'
    return wrapper


@execution_time
def addition(number):
    intial_sum = 0
    for i in range(number):
        intial_sum += i
    return intial_sum

print(addition(1000))
print(addition(100))
print(addition(100000000))
