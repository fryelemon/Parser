import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


data = [[], [], [], []]
indexes = ['Name', 'Price', 'Discounted price', 'Rate']


def page_exists(browser, page_number=1):
    have_connection(browser, page_number)
    try:
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layoutPage"]'
                                                                                   '/div[1]/div[3]/div[2]'
                                                                                   '/div[2]/div[2]/div[1]'
                                                                                   '/div/div/div')))
    except TimeoutException:
        return False
    return True


def run_process(page_number, browser):
    # wait = WebDriverWait(browser, 2)

    if have_connection(browser, page_number):
        # browser.save_screenshot('screenie.png')
        browser.implicitly_wait(2)  # seconds
        # html = browser.page_source
        return parse(browser)
    else:
        print('Error connecting')


def build_df(input_list):
    global data
    n = 0
    for col in input_list:
        [data[n].append(value) for value in col]
        n += 1


def get_driver():
    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("disable-gpu")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--headless")

    # initialisation
    driver = webdriver.Chrome(options=options)
    return driver


def have_connection(browser, page_number):
    main_url = 'https://www.ozon.ru/category/konfety-30695/?page=' + str(page_number)
    connection_attempts = 0
    while connection_attempts < 3:
        try:
            browser.get(main_url)
            WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )
            return True
        except Exception as e:
            print(e)
            connection_attempts += 1
            print(f'Error connecting to {main_url}.')
            print(f'Attempt #{connection_attempts}.')
    return False


def parse(browser):
    try:
        WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layoutPage"]/div[1]'
                                                                                  '/div[3]/div[1]/div/div[2]/h1')))
    except TimeoutException:
        print("Loading took too much time!")
    names = [x.text for x in browser.find_elements(By.XPATH, '//*[@id="layoutPage"]'
                                                             '/div[1]/div[3]/div[2]'
                                                             '/div[2]/div[3]/div[1]'
                                                             '/div/div/div/div[1]/a/span/span')]
    price = [x.text for x in browser.find_elements(By.XPATH, '//*[@id="layoutPage"]'
                                                             '/div[1]/div[3]/div[2]'
                                                             '/div[2]/div[3]/div[1]'
                                                             '/div/div/div/div[1]/div[1]/span[1]')]
    discount_price = [x.text for x in browser.find_elements(By.XPATH, '//*[@id="layoutPage"]'
                                                                      '/div[1]/div[3]/div[2]'
                                                                      '/div[2]/div[3]/div[1]'
                                                                      '/div/div/div/div[1]/div[1]/span[2]')]
    rate = [x.text for x in browser.find_elements(By.XPATH, '//*[@id="layoutPage"]'
                                                            '/div[1]/div[3]/div[2]'
                                                            '/div[2]/div[3]/div[1]'
                                                            '/div/div/div/div[1]/div[2]/a')]

    output = [names, discount_price, price, rate]

    return output


def to_file(filename):
    global indexes
    global data

    try:
        open(filename, 'x')
    except FileExistsError:
        open(filename, 'w')

    book = {
        indexes[0]: data[0],
        indexes[1]: data[1],
        indexes[2]: data[2],
        indexes[3]: data[3]
            }

    df = pd.DataFrame.from_dict(book, orient='index')
    df = df.transpose()

    df.to_excel(filename, index=False)
