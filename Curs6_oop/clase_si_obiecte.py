""" Bafta este o pisica mare care doarme toata ziua  """

# object_name = Bafta (numele obiectului) (subiect)
# class_name = Pisica (numele clasei) (substantiv)
# property = marime_pisica (proprietate sau atribut) (adjectiv/adverb)
# activity = doarme (actiune) (verb)


""" O masina Dacia alba, merge repede """
# object_name = Dacia
# class_name = masina
# property = alba, repede
# activity = merge


""" Catelul Dino are 4 picioare si latra tare """
# object_name = Dino
# class_name = catel
# property = 4 picioare, tare
# activity = latra


""" transpunere """


# class Dog:    # (FirstDogClass)
#     pass


# class Dog:
#
#     def __init__(self):
#         pass
#
#
# dino = Dog()


# class Stack:
#
#     variabila = 10
#
#     def __init__(self):
#         stack_list = [1]
#         self.stack_list = [2]
#         self.__stack_list = [3]
#
#     def gigel(self):
#         print(self.stack_list)
#         print(self.__stack_list)
#
#
# obj_stiva = Stack()
# print(obj_stiva.stack_list)
# # print(obj_stiva.__stack_list)
# print(obj_stiva.variabila)


# class Stack:
#
#     def __init__(self):
#         self.__stack_list = []
#
#     def push(self, val):
#         self.__stack_list.append(val)
#         print(self.__stack_list)
#
#     def pop(self):
#         valoare = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return valoare
#
#
# obj_stiva = Stack()
# obj_stiva.push(1)
# obj_stiva.push(2)
# obj_stiva.push(3)
#
# print(obj_stiva.pop())
# print(obj_stiva.pop())
# print(obj_stiva.pop())


# class Stack:
#
#     def __init__(self, val1):
#         self.__stack_list = []
#         self.val1 = val1
#
#     def push(self, val):
#         self.__stack_list.append(val)
#         print(self.__stack_list)
#         print(self.val1)
#
#     def pop(self):
#         valoare = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return valoare
#
#
# obj_stiva = Stack(4)
# print(obj_stiva)
#
# obj_stiva.push(1)
# obj_stiva.push(2)
# obj_stiva.push(3)
#
# print(obj_stiva.pop())
# print(obj_stiva.pop())
# print(obj_stiva.pop())


class Stack:

    def __init__(self, *val1):
        self.__stack_list = []
        self.val1 = val1

    def push(self):
        for element in self.val1:
            self.__stack_list.append(element)
        print(self.__stack_list)

    def pop(self):
        valoare = self.__stack_list[-1]
        del self.__stack_list[-1]
        return valoare


obj_stiva = Stack(1, 2, 3)

obj_stiva.push()

print(obj_stiva.pop())
print(obj_stiva.pop())
print(obj_stiva.pop())
