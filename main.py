from selenium_config.open_browser import initialize_browser
from wfm.contracts import enter_contract, obtain_contract_info, search_contract
from csv_config.csv_functions import read_csv_contracts, contract_numbers, save_csv, update_csv, dados

if __name__ == "__main__":
    browser = initialize_browser()
    try:
        contract_numbers = read_csv_contracts()
        for number in contract_numbers:
            search_contract(browser, number)
            enter_contract(browser, number)
            contract_info = obtain_contract_info(browser)
            update_csv(**contract_info)

        save_csv()

    finally:
        browser.quit()
