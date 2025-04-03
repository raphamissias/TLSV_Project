from selenium_config.open_browser import initialize_browser
from wfm.contracts import enter_contract, obtain_contract_info, search_contract
from csv_file.functions import contract_numbers, save_csv, update_csv, dados

if __name__ == "__main__":
    browser = initialize_browser()
    try:
        contracts = contract_numbers()
        for number in contracts:
            search_contract(browser, number)
            enter_contract(browser, number)
            contract_info = obtain_contract_info(browser)
            update_csv(**contract_info)

        save_csv()

    finally:
        browser.quit()
