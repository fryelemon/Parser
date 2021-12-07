import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

webdriver = Service(r'A:\Код\Parser\Сам_Парсер\chromedriver.exe')
driver = Chrome(service=webdriver)

pages = 10


for page in range(1, pages):

    url = 'https://www.ozon.ru/category/konfety-30695/?page=' + str(page)
    driver.get(url)

    candies = driver.find_elements(By.CLASS_NAME, 'tile-hover-target')

    for candy in candies:
        candy.click()

        wait = WebDriverWait(driver, 10)
        wait.until(lambda driver: driver.find_element(By.TAG_NAME, 'h1').text != 'Конфеты')

        print(driver.find_element(By.TAG_NAME, 'h1').text)
        driver.get(url)
        wait.until(lambda driver: driver.find_element(By.TAG_NAME, 'h1').text == 'Конфеты')
        break

driver.quit()
