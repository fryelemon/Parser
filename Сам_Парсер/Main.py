# import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def go_to_link(link):
    driver.get(link)
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))


chrome = Service(r'A:\Код\Parser\Сам_Парсер\chromedriver.exe')
driver = Chrome(service=chrome)
pages = 2

for page in range(1, pages):
    url = 'https://www.ozon.ru/category/konfety-30695/?page=' + str(page)
    go_to_link(url, driver)

    candies_link = [0]*36
    for p in range(1,37):
        candies_link[p - 1] = driver.find_elements(By.XPATH, '/html/body'
                                                             '/div[1]/div'
                                                             '/div[1]/div[3]'
                                                             '/div[2]/div[2]'
                                                             '/div[3]/div[1]'
                                                             '/div/div/div[' + str(p) + ']/a')[0].get_attribute('href')

    candy_name = []
    for candy_link in candies_link:
        driver.delete_all_cookies()

        go_to_link(candy_link, driver)

        candy_name.append(driver.find_element(By.TAG_NAME, 'h1').text))

        sleep(2)
        go_to_link(url, driver)



driver.quit()
