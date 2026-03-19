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
driver.get("https://sauce-demo.myshopify.com/account/login")

# abre o navegador em tela cheia (evita erros)
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# preenche email
driver.find_element(By.ID, "customer_email").send_keys("deborahmaia48@gmail.com")

# preenche senha
driver.find_element(By.ID, "customer_password").send_keys("12345678")

# clica no botão login
driver.find_element(By.CSS_SELECTOR, "input[value='Sign In']").click()

# espera carregar
time.sleep(3)

# Validação
try:
    wait.until(EC.url_contains("account"))
    print("✅ CT-02 PASSOU - Login realizado com sucesso")
except:
    print("❌ CT-02 FALHOU - Login não funcionou")

# fecha navegador
driver.quit()

#TESTE BEM SUCEDIDO