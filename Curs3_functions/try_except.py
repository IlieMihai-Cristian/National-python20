#
# # var = 10
# # print(var/0)) # eroare de sintaxa
# # print(var/0)  # eroare de exceptie
#
# """ Raise Exception """
#
# # var = 10
# # if var >= 5:
# #     raise Exception('Aici este o eroare')
#
#
# """ blocul try / except """
#
# # # ex:
# # my_text = input('Introduceti un nr.: ')
# # # value = int(my_text)
# # try:
# #     value = int(my_text)
# #     print(value)
# #     print(variabila_nedefinita)
# # except ValueError:
# #     print('Nu pot converti un sir de caractere la int')
# # except NameError:
# #     variabila_nedefinita = 100
# #     print(f'Nu am stiut ce valoare are variabila ta asa ca i-am alocat {variabila_nedefinita}')
# # except Exception as e:
# #     print('intra pe exceptie: ', e)
#
# """ else/finally """
#
# # ex:
# my_text = input('Introduceti un nr.: ')
# # value = int(my_text)
# try:
#     value = int(my_text)
#     print(value)
#     # print(variabila_nedefinita)
# except ValueError:
#     print('Nu pot converti un sir de caractere la int')
# except NameError:
#     variabila_nedefinita = 100
#     print(f'Nu am stiut ce valoare are variabila ta asa ca i-am alocat {variabila_nedefinita}')
# except Exception as e:
#     print('intra pe exceptie: ', e)
# else:   # se executa doar daca nu sunt exceptii
#     print('nu sunt exceptii')
# finally:
#     print('printez orice ar fi')


variabila = 'BBB'