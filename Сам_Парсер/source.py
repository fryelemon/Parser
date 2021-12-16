import pandas as pd
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC


def write_to_file(names, filename):
    try:
        open(filename, 'x')
    except FileExistsError:
        open(filename, 'w')

    summary = {'Наименования': names}
    df = pd.DataFrame(summary)

    df.to_excel(filename, index=False)


def get_driver(headless):
    chrome = Service(r'chromedriver.exe')
    options = webdriver.ChromeOptions()

    if headless:
        options.add_argument('--headless')

    driver = webdriver.Chrome(service=chrome, chrome_options=options)
    return driver


def connect_to_base(browser, page_number):


def run_process(page_number, filename, browser):
