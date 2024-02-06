""" siruri de caractere, imutabile, indexabile """

# var = str()

"""concatenare"""

# var_1 = 'pro'
# var_2 = 'gram'
# var_3 = 'are'
# print(var_1 + var_2 + var_3)

"""multiplicare"""
# multip = 4
# print(multip * var_1)

# print(-4 * var_1)
# print(id(-4 * var_1))
# print(id(""))

""" transformarea in string cu str() """
# print("43.5", type("43.5"))
# print(str(43.5), type(str(43.5)))

"""lungimea unui string len()"""
# var_4 = "programare"
# print(len(var_4))  # numara inclusiv spatiile

"""operatori in si not in"""
# print('gr' in var_4)
# print('gr' not in var_4)

"""indexare"""  # var[index]
# print(var_4[0])
# print(var_4[9])
# print(var_4[10]) # da eroare
# print(var_4[-1])
# print(var_4[len(var_4) - 1])
# print(var_4[-len(var_4)])

"""slicing"""  # [start:stop:pas]
# print(var_4[1:10:2])
# print(var_4[-6::2])

"""interpolare variabilelor in stringuri"""

var_1 = 'Python'
var_2 = 'Scoala'
var_3 = 'IT'

# caz 1
# print('Grupa de ' + var_1 + ' de la ' + var_2 + ' Informala de ' + var_3 + '!')

# caz 2 cu .format
    # cu acolade goale
# print('Grupa de {} de la {} Informala de {}!'.format(var_1, var_2, var_3))

    # cu index in acolade
# print('Grupa de {0} de la {1} Informala de {2}!'.format(var_1, var_2, var_3))

    # cu dennumire variabila in acolade
# print('Grupa de {str_1} de la {str_2} Informala de {str_3}!'.format(str_1='Python', str_2='Scoala', str_3='IT'))

# caz 3 cu f'string  -> Python 3.6
# print(f'Grupa de {var_1} de la {var_2} Informala de {var_3}!')


# x = '10'
# y = int(x)
# print(y, type(y))


""" cateva metode folosite ptr obiectele de tip string"""

# string_1 = 'programare'
# print(string_1.capitalize())  # primul char cu litera mare
# print(string_1.upper())  # caracterele cu litere mari
string_1 = 'PROGRAMARE'
# print(string_1.lower())  # caracterele cu litere mici
string_2 = 'Ana banana'
# print(string_2.count('na'))  # returneaza de cate ori un substr exista intr-un str

string_3 = 'Metode folosite pentru stringuri'
# print(string_3.find('pentru'))
# print(string_3.find('xxxxxx'))
# print(string_3.index('pentru'))
# print(string_3.index('xxxxxx'))

string_4 = 'Ana, are mere, are pere, si, are struguri!'
# print(string_4.split(' '))  # returneaza o lista cu sirul splituit

string_5 = ['Ana', ' are mere', ' are pere', ' si', ' are struguri!']
# print(''.join(string_5))

# print(string_3.replace('pentru', 'la'))

string_6 = '      Ana are      '
# print(string_6.lstrip())
# print(string_6.rstrip())
print(string_6.strip())
