import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

webdriver = Service(r'A:\Код\Parser\Сам_Парсер\chromedriver.exe')
driver = Chrome(service=webdriver)

pages = 2

wait = WebDriverWait(driver, 10)

for page in range(1, pages):
    url = 'https://www.ozon.ru/category/konfety-30695/?page=' + str(page)
    driver.get(url)
    wait.until(lambda driver: driver.find_element(By.TAG_NAME, 'h1').text == 'Конфеты')

    candies_link = [0]*36
    for p in range(1,37):
        candies_link[p - 1] = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div['
                                                '1]/div[3]/div[2]/div[2]/div[3]/div[1]'
                                                           '/div/div/div[' + str(p) + ']/a')[0].get_attribute('href')

    for candy_link in candies_link:
        driver.get(candy_link)
        wait.until(lambda driver: driver.find_element(By.TAG_NAME, 'h1').text != 'Конфеты')

        print(driver.find_element(By.TAG_NAME, 'h1').text)

        driver.get(url)
        wait.until(lambda driver: driver.find_element(By.TAG_NAME, 'h1').text == 'Конфеты')
    break

driver.quit()
