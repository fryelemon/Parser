import requests
import pandas as pd
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

UserAgent().chrome

page_link = 'https://www.wildberries.ru/catalog/0/search.aspx?search=%D0%BA%D0%BE%D1%80%D0%BC+%D0%B4%D0%BB%D1%8F+%D0%BA%D0%BE%D1%88%D0%B5%D0%BA'
response = requests.get(page_link)

html = response.content

soup = BeautifulSoup(html,'html.parser')

