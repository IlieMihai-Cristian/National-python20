# x = 1
#
# def f():
#     return x
#
# print(x)
# print(f())
#
#
# # a. error
#
# # b. 1
#
# # c. 1
# #    1
#
# # d. 0 1


# ----------------------------------------

# x = [111, 2, "hello", "world", ["another", "list"]]
# print(len(x[3]))
#
# # a. TypeError: object of type 'int' has no len()
# # b. 5
# # c. 0
# # d. 2


# ----------------------------------------

# x = (1, 2, 3)
#
# x[1] = 4
#
#
# # a. x = (1, 1, 3)
# # b. x = (1, 4, 3)
# # c. x = [1, 2, 3]
# # d.TypeError

# ----------------------------------------

# a = [1, 2, 3]
# b = [4, 5]
#
# print(a + b * 3)

# a. [1, 2, 3, 4, 5]
# b. [1, 2, 3, 12, 15]
# c. error
# d. [1, 2, 3, 4, 5, 4, 5, 4, 5]

# ----------------------------------------


# x = [1, 2, 3, 4]
# print(x[-1:])

# a. [1, 2, 3]
# b. [4]
# c. [1, 2, 3, 4]
# d. [3, 2, 1]

# ----------------------------------------

# x = [0, 1, [2]]
# x[2][0] = 3
# x[2].append(4)
# x[2] = 2
# print(x)

# a. [0, 1, 3]
# b. [0, 1, [2]]
# c. [0, 1, 2]
# d. error


# ----------------------------------------

# def exercitiu(i):
#     for i in range(i):
#         return i
#
#
# x = exercitiu(3)
# print(x)
#
# # a. error
# # b. 0 1 2
# # c. 3
# # d. 0


# ----------------------------------------
#
# a = range(10)
# y = [x*x for x in a if x % 2 == 0]
# print(y)
#
# # a. [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # b. [2, 4, 6, 8]
# # c. [0, 4, 16, 36, 64]
# # d. [0, 2, 16, 36, 64]


# ----------------------------------------

# def make_account():
#     return {'balance': 0}
#
#
# def deposit(account, amount):
#     account['balance'] = account['balance'] + amount
#     return account['balance']
#
#
# a = make_account()
# print(deposit(a, 10))
#
# # a. error
# # b. 0
# # c. 10
# # d. None

# ----------------------------------------

# print("foo" + 2)

# a. cannot concatenate 'str' and 'int' objects
# b. name 'foo' is not defined
# c. foo2
# d. integer division or modulo by zero

# ----------------------------------------

# try:
#     print("a")
# except:
#     print("b")
# else:
#     print("c")
# finally:
#     print("d")

# a. a b c d
# b. a b c
# c. a c d
# d. error

# ----------------------------------------

# for k in {"x": 1, "y": 2}:
#     print(k)

# a. {"x": 1, "y": 2}
# b. x y
# c. 1 2
# d. error

# ----------------------------------------

# print(list("python"))

# a. ['python']
# b. ‘p’, ‘y’, ‘t’, ‘h’, ‘o’, ‘n’
# c. error
# d. [‘p’, ‘y’, ‘t’, ‘h’, ‘o’, ‘n’]


# ----------------------------------------

# def func(*args):
#     return 3 + len(args)
#
#
# print(func(4, 4, 4))

# a. 4
# b. error
# c. 6
# d. 15

# ----------------------------------------

# count = (3, 2, 5, 4)
# while len(count) < 5:
#     count0 = count[0] + 1
#     print("Hello Geek")

# a. Hello Geek
# b. loop infinit in care se afiseaza Hello Geek
# c. None
# d. error


# ----------------------------------------

# def exercitiu(var):
#     for letter in "geeksforgeeks":
#         if letter == 'e' or letter == 's':
#             continue
#         print("Current letter :", letter)
#         var = 10
#         return var
#
#
# print(exercitiu(20))

# a. 10
# b. None
# c. Current letter: g
#    10
# d. Current letter: g
#    20

# ----------------------------------------

# def f(a, ccc=None):
#     aaa = []
#     for i in range(a):
#         ccc.append(i*i)
#     return ccc
#
#
# print(f(3))
# print(f(2, [1, 2, 3]))
# print(f(2))
#
#
# # a. [0, 1, 4] [1, 2, 3, 0, 1] [0, 1, 4, 0, 1]
# # b. [0, 1, 4] [1, 2, 3, 0, 1] [0, 1]
# # c. error
# # d. [0, 1, 4]

# ----------------------------------------

# list = ['1', '2', '3', '4', '5']
# print(list[12:])

# a. index error
# b. []
# c. None
# d. list este cuvant rezervat
