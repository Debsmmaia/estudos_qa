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

wait = WebDriverWait(driver, 10)

# clica no produto
driver.find_element(By.CSS_SELECTOR, "#product-1").click()

# clica para escolher a cor
driver.find_element(By.CSS_SELECTOR, "#add").click()

# necessário esperar o produto ser adicionado para clicar
time.sleep(2)

# espera para ser encontrado e após ser encontrado, clica no botão
checkout_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout")))
checkout_btn.click()

time.sleep(2)
checkout_btn_2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout")))
checkout_btn_2.click()

# fecha navegador
driver.quit()

#TESTE BEM SUCEDIDO
