from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from csv_config.csv_functions import save_csv

def search_contract(browser, contract_number):
    """Tenta localizar o campo de pesquisa por diferentes seletores."""
    try:
        # Primeiro XPath
        search_input = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Pesquisa em atividades"]'))
        )

        search_input.click()
        search_input.clear()

        search_input.send_keys("_" + contract_number)

        # Segundo XPath
        search_input = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@class="search-bar-input"]'))
        )

        search_input.click()
        search_input.clear()
        search_input.send_keys(contract_number)

        return search_input
    except Exception:
        try:
            # Segundo XPath
            search_input = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@class="search-bar-input"]'))
            )

            search_input.click()
            search_input.clear()
            search_input.send_keys(contract_number)

            return search_input
        except Exception:
            # Retorna None se nenhum campo for encontrado
            return None

def enter_contract(browser, contract_number):
    try:
        # Localiza o campo de pesquisa
        contract_founded = search_contract(browser, contract_number)
        if not contract_founded:
            raise Exception("Nenhum campo de pesquisa encontrado.")

        # Aguarda até que a atividade seja localizada e clica nela
        activity_founded = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="oj-collapsible-content oj-component-content"]/div[1]/div[1]'))
        )
        activity_founded.click()
        print(f"Contrato {contract_number} acessado com sucesso!")
    
    except Exception as e:
        print(f"Erro ao acessar o contrato {contract_number}: {e}")

def obtain_contract_info(browser):
    try:
        try:
            XA_NOTDONE_REASON = browser.find_element(By.XPATH, '//*[@data-label="XA_NOTDONE_REASON"]').text
        except:
            XA_NOTDONE_REASON = "Finalizado"

        customer_number = browser.find_element(By.XPATH, '//*[@data-label="customer_number"]').text
        try:
            ccell = browser.find_element(By.XPATH, '//*[@data-label="ccell"]').text
        except:
            ccell = "Sem número"
        try:
            XA_NEIGHBORHOOD = browser.find_element(By.XPATH, '//*[@data-label="XA_NEIGHBORHOOD"]').text
        except:
            XA_NEIGHBORHOOD = None

        a_tsid = browser.find_element(By.XPATH, '//*[@data-label="a_tsid"]').text

        data = {
            "XA_NOTDONE_REASON": XA_NOTDONE_REASON,
            "customer_number": customer_number,
            "ccell": ccell,
            "XA_NEIGHBORHOOD": XA_NEIGHBORHOOD,
            "a_tsid": a_tsid,
        }

        return (data)
    except Exception as e:
        print(f"Erro ao obter informações do contrato.\n {e}")

