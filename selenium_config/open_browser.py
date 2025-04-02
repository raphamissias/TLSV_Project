from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import socket

def is_debugging_port_active(host="127.0.0.1", port=9222):
    """Verifica se a porta de depuração remota está ativa."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        return sock.connect_ex((host, port)) == 0

def initialize_browser():
    try:
        # Verificar se o Chrome foi iniciado com o modo de depuração
        if not is_debugging_port_active():
            print("Erro: Chrome não está em execução no modo de depuração (porta 9222).")
            print("Inicie o Chrome com: --remote-debugging-port=9222")
            return None

        # Configurar as opções do Chrome
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  # Conectar à instância de depuração

        # Configurar o serviço do ChromeDriver
        # service = Service(ChromeDriverManager().install())  # Baixar e configurar o ChromeDriver

        # Inicializar o navegador
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    except Exception as e:
        print(f"Erro ao inicializar o navegador: {e}")
        return None

def login(browser):
    browser.get("https://copel.etadirect.com")

    login_input = browser.find_element('xpath', '//*[@id="username"]')
    login_input.send_keys("03692703988")

    pass_input = browser.find_element('xpath', '//*[@id="password"]')
    pass_input.send_keys("Aef16dvm*")

    sign_in_button = browser.find_element('xpath', '//*[@id="sign-in"]/div')
    sign_in_button.click()