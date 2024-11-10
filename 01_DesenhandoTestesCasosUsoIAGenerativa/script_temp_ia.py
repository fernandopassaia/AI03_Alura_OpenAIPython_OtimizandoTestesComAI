from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Configura o caminho do driver do Chromium
chrome_driver_path = "Caminho_para_seu_driver_chromium"

# Inicializa o serviço do driver
service = Service(chrome_driver_path)
service.start()

# Inicializa o navegador Chromium
driver = webdriver.Chrome(service=service)

# URL da plataforma AcordeLab
url = "https://www.acordelab.com"

# Abrir o aplicativo da plataforma AcordeLab
driver.get(url)

# Localizar e selecionar a opção "Login"
login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
login_button.click()

# Preencher o campo "E-mail" com o endereço de e-mail
email_input = driver.find_element(By.NAME, "email")
email_input.send_keys("ana@example.com")

# Preencher o campo "Senha" com a senha de acesso
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("senha123")

# Clicar no botão "Entrar" para realizar o login
enter_button = driver.find_element(By.XPATH, "//button[text()='Entrar']")
enter_button.click()

# Aguardar a validação das informações e redirecionamento para a página inicial logada
time.sleep(3)

# Fechar o navegador após 3 segundos
driver.quit()
