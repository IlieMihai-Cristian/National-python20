"""Declaratia IF"""

# if expresie:
#     instructiune (set de instructiuni)

first_number = 10
second_number = 20

# if first_number > second_number:
#     print('intra pe linia 10')
#
# if first_number < second_number:
#     print('intra pe linia 13')


list_ex = ['rosu', 'galben', 'albastru']

if 'galben' in list_ex:
    print('expresia este adevarata')  # 1
    if first_number > second_number:
        print('a intrat pe primul if din interior expresie')
    if first_number <= second_number:
        print('a intrat pe al doilea if din interior expresie') # 2
        print('mesaj 2') # 3
    print('mesaj 3') # 4
print('mesaj 4') # 5

