# pip install selenium
# pip install webdriver_manager
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.bnr.ro/files/xml/nbrfxrates2023.htm")

table_head = driver.find_element(by=By.XPATH, value='//*[@id="Data_table"]/table/thead')
# print(table_head.text)
table_body = driver.find_element(by=By.XPATH, value='//*[@id="Data_table"]/table/tbody')
# print(table_body.text)
header = table_head.text.split('\n')
# print(header)
body = table_body.text.split('\n')
# print(body)

# print(len(header))  # 32 elem
# print(len(body))  # 7936 elem

# [ [. . .],[ . . .],[ . . .] . . . . ]

# TABEL GENERAT PE RANDURI
# body_list = []
# index = 0
# while index < len(body) - len(header):
#     sublist = body[index:index+len(header)]  # 0:31
#     body_list.append(sublist)
#     index += len(header)
# print(body_list)

# for i in range(0, len(body), len(header)):
#     index = i
#     body_list.append((body[index: index+len(header)]))

# df = pd.DataFrame(body_list, columns=header)
# print(df)
# df.to_excel('Tabel_BNR_2023.xlsx', index=False)

# TABEL GENERAT PE COLOANE

# {'Data': [. , . , . ,. ]}

body_columns = {key: [] for key in range(len(header))}
# print(body_columns)
counter = 0
for j in body:
    body_columns[counter % len(header)].append(j)
    counter += 1
# print(body_columns)

df = pd.DataFrame(body_columns)
# print(df)
# df.to_excel('Tabel_BNR_2023_2.xlsx', header=header, index=False)
df.to_csv('Tabel_BNR.csv', header=header)