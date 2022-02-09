from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from time import sleep
import source

def go_to_link(link, browser):
    browser.get(link)


chrome = Service(r'A:\Код\Parser\Сам_Парсер\chromedriver.exe')
driver = Chrome(service=chrome)

for page in range(1, 2):
    p = 1
    url = 'https://www.ozon.ru/category/konfety-30695/?page=' + str(page)
    go_to_link(url, driver)

    while p < 37:
        candies_link = driver.find_elements(
            By.XPATH, '//*[@id="layoutPage"]/div[1]/div[3]/div[2]/div[2]/div[3]/div[1]/div/div/div/a'
        )
        p += 1

    print(candies_link[0].get_attribute('href'))
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
