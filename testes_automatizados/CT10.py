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
driver.get("https://sauce-demo.myshopify.com/")

# abre o navegador em tela cheia (evita erros)
driver.maximize_window()

wait = WebDriverWait(driver, 20)

time.sleep(2)
# preenche email
driver.find_element(By.CSS_SELECTOR, ".search").send_keys("Grey")
driver.find_element(By.CSS_SELECTOR, "#search-submit").submit()

time.sleep(2)
palavra_localizada = wait.until(EC.visibility_of_element_located((By.ID, "keyword")))
resultado = palavra_localizada.text
# Espera o item estar visível e encontra a palavra pesquisada no retorno da busca

assert "grey" in resultado.lower()

print(f"✅ Sucesso: A busca foi feita corretamente!")

driver.quit()
 