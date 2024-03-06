import datetime

def category_insertion():
    while True:
        with open('catergorii.txt', 'a') as file:
            file.write(f'{input("Adauga categoria: ")} \n')
        next_category = input('Introduceti o alta categorie? (Y/N): ').lower()
        if next_category == 'n':
            break
    return True


# category_insertion()

# print(datetime.datetime.now())
# date = datetime.datetime.now()
date = '2024-03-20 19:00'
obj_time = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M')  # obiect tip data
print(obj_time)
print(type(obj_time))
new_format_date = datetime.datetime.strftime(obj_time, '%d-%m-%Y %H:%M')  # string tip data
print(new_format_date)
