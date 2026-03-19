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

wait = WebDriverWait(driver, 10)

# preenche nome e sobrenome
driver.find_element(By.CSS_SELECTOR, "input#first_name").send_keys("Carla")
driver.find_element(By.CSS_SELECTOR, "input#last_name").send_keys("Campos")

# preenche email
driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("deborahmaia48@gmail.com")

# preenche senha
driver.find_element(By.CSS_SELECTOR, "input#password").send_keys("12345678")

# clica no botão de criar usuário
driver.find_element(By.CSS_SELECTOR, "input[value='Create']").click()


# Espera a mensagem de erro aparecer na tela 
erro_localizado = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".errors"))) #espera o erro ficar visível

# Obtem o texto escrito 
texto_exibido = erro_localizado.text

# Se conter essa parte no texto da tela, o código continua
assert "email address is already associated" in texto_exibido #assert verifica o texto

print("✅ Sucesso: O sistema barrou o e-mail duplicado.")

# TESTE FALHOU
# O site possui captcha, então não foi possível criar outro usuário 