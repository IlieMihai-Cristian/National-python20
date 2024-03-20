from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.emag.ro/")

element = driver.find_element(by=By.ID, value='searchboxTrigger')
element.send_keys('placa video PNY')
element.submit()

video_boards = driver.find_elements(by=By.CLASS_NAME, value='card-v2')
# print(len(video_boards))

for i in range(1, len(video_boards)+1):
    try:
        video = driver.find_element(by=By.XPATH, value=f'//*[@id="card_grid"]/div[@data-position="{i}"]')
        # print(video.text, '\n', ' ----------------------- ')
    except Exception:
        video = False
    if video:
        if 'GeForce RTX 4070' in video.text:
            # print(video.text, '\n', ' ----------------------- ')
            price = driver.find_element(by=By.XPATH, value=f'//*[@id="card_grid"]/div[@data-position="{i}"]/div/div/div[4]/div[1]/p[2]').text
            # print(price)
            # print(video.text, '\n', ' ----------------------- ')
            # 3.888, 88 Lei
            transformed_price = price.strip().replace('.', '').replace(',', '.').split(' ')[0]
            # print(transformed_price)
            if float(transformed_price) < 4000:
                # print(float(transformed_price), 'ok')
                driver.find_element(by=By.XPATH, value=f'//*[@id="card_grid"]/div[@data-position="{i}"]/div/div/div[4]/div[2]/form/button').submit()
                break


