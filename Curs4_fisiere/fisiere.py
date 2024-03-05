import csv

"""
file = open('data.txt', 'r')
r  (vine de la read )-> CITIRE - NU ADAUGA IN FISIER (daca fisierul nu exista atunci cand am modul r, acesta crapa)
file = open('data.txt', 'w')
w (vine de la write)-> SCRIERE (daca fisierul nu exista, Python il creeaza), daca exista ceva in fisier, rescrie
file = open('data.txt', 'a')
a (vine de la append)-> SCRIERE (daca fisierul nu exista, Python il creeaza), adauga la final
file = open('data.txt', 'r+')
r+  (vine de la read )-> CITIRE si SCRIERE - NU ADAUGA IN FISIER (daca fisierul nu exista atunci cand am modul r, acesta crapa),
    suprascrie textul
"""

# mod 1
# file = open('data.txt', 'r+')
# file.write('Astazi este luni')
# file.close()

# mod 2
# file = open('data.txt', 'w')
# try:
#     file.write('Astazi este luni')
# finally:
#     file.close()

# mod 3
# with open('data.txt', 'w') as file:
#     file.write('Astazi este luni')

""" Citire dintr-un fisier """
# var 1
# with open('data.txt', 'r') as file:
#     for line in file.readlines():
#         print(line)

# var 2
# with open('data.txt', 'r') as file:
#     # print(list(file))
#     for item in list(file):
#         print(item)

# var 3
# with open('data.txt', 'r') as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line)


""" CSV """

# with open('fisier_csv.csv', 'r') as csv_file:
#     rows = csv.reader(csv_file, delimiter=',')
#     # print(rows)
#     # print(type(rows))
#     for row in rows:
#         print(row)

car_list = [
    ['Dacia', 'Logan', 2019, 75],
    ['Audi', 'Q8', 2023, 400]
]

# with open('fisier_csv.csv', 'a') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=',')
#     for car in car_list:
#         csv_writer.writerow(car)

with open('fisier_csv.csv', 'a') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerows(car_list)
