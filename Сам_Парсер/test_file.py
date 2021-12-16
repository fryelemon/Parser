from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from time import sleep
import source
# from multiprocessing import Pool


def go_to_link(link, browser):
    browser.get(link)


chrome = Service(r'A:\Код\Parser\Сам_Парсер\chromedriver.exe')
driver = Chrome(service=chrome)

for page in range(1, 2):
    p = 1
    url = 'https://www.ozon.ru/category/konfety-30695/?page=' + str(page)
    go_to_link(url, driver)

    candies_link = []
    while p < 37:
        candies_link.append(driver.find_elements(By.XPATH, '/html/body/div[1]/div/'
                                                           'div[1]/div[3]/div[2]/di'
                                                           'v[2]/div[3]/div[1]/div/d'
                                                           'iv/div[' + str(p) + ']/a')[0].get_attribute('href'))
        p += 1

    break
    candy_name = []
    for candy_link in candies_link:
        driver.delete_all_cookies()
        go_to_link(candy_link, driver)

        candy_name.append(driver.find_element(By.TAG_NAME, 'h1').text)

        sleep(2)
        go_to_link(url, driver)

    page += 1

#source.to_xlsx(candy_name)

driver.quit()
