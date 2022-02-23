import source as s
from time import time


if __name__ == '__main__':
    # Main variables
    current_page = 1
    start_time = time()
    filename = r'Конфеты.xlsx'

    # Starting web-driver
    browser = s.get_driver()

    # Scraaaaaaaaaaping
    while current_page <= 10:
        print(f'Scraping page: #{current_page}...')
        data = s.run_process(current_page, filename, browser)
        s.build_df(data)
        current_page += 1

    # Ending script
    s.to_file(filename)
    browser.quit()
    end_time = time()
    working_time = end_time - start_time
    print(f'Run time: {working_time}')