import source as s
from time import sleep, time
import sys


if __name__ == '__main__':
    # headless mod working?
    headless = False
    if len(sys.argv) > 1:
        if sys.argv[1] == "headless":
            print("Running in headless mode")
            headless = True

    # Main variables
    current_page = 1
    start_time = time()
    filename = r'Конфеты.xlsx'

    # Starting web-driver
    browser = s.get_driver(headless=headless)

    # Scraaaaaaaaaaping
    while current_page <= 5:
        print(f'Scraping page: #{current_page}...')

        current_page += 1

    # Ending script
    browser.quit()
    end_time = time()
    working_time = end_time - start_time
    print(f'Run time: {working_time}')