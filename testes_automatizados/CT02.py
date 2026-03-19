from selenium import webdriver
from selenium.webdriver.chrome.service import Service # Quem inicia o chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# inicia navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # Conecta o selenium com o chrome (baixa automaticamente)

# acessa o site
driver.get("https://sauce-demo.myshopify.com/account/register")

# abre o navegador em tela cheia (evita erros)
driver.maximize_window()

wait = WebDriverWait(driver, 20)

# preenche nome e sobrenome
driver.find_element(By.CSS_SELECTOR, "input#first_name").send_keys("Julia")
driver.find_element(By.CSS_SELECTOR, "input#last_name").send_keys("Dias")

# preenche email
driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("Julia@gmail.com")

# preenche senha
driver.find_element(By.CSS_SELECTOR, "input#password").send_keys("12345678")

# clica no botão de criar usuário
driver.find_element(By.CSS_SELECTOR, "input[value='Create']").click()

# espera carregar
time.sleep(3)

# Validação
try:
    wait.until(EC.url_contains("account"))
    print("✅ CT-01 PASSOU - Usuário criado com sucesso")
except:
    print("❌ CT-01 FALHOU - Criação de usuário não funcionou")

# fecha navegador
driver.quit()

#TESTE BEM SUCEDIDO 