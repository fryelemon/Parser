import source as s
from time import time


if __name__ == '__main__':
    # Main variables
    current_page = 1
    start_time = time()
    filename = r'Конфеты.xlsx'

    # Starting web-driver
    browser = s.get_driver()

    # Scraping
    while s.page_exists(browser, current_page) and current_page < 2:
        print(f'Scraping page: #{current_page}...')
        data = s.run_process(current_page, browser)
        s.build_df(data)
        current_page += 1

    # Ending script
    s.to_file(filename)
    browser.quit()
    end_time = time()
    working_time = end_time - start_time
    print(f'Run time: {round(working_time)} seconds.')