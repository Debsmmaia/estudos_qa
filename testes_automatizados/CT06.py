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

wait = WebDriverWait(driver, 20)

# preenche email
driver.find_element(By.ID, "customer_email").send_keys("deborahmaia48@gmail.com")

# preenche senha
driver.find_element(By.ID, "customer_password").send_keys("12345")

# clica no botão login
driver.find_element(By.CSS_SELECTOR, "input[value='Sign In']").click()


erro_localizado = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".errors"))) #espera o erro ficar visível

# 2Obtem o texto escrito 
texto_exibido = erro_localizado.text

# Se conter essa parte no texto da tela, o código continua
assert "Incorrect email or password." in texto_exibido #assert verifica o texto

print("✅ Sucesso: O sistema negou o login com senha errada!")


# fecha navegador
driver.quit()

#TESTE FALHOU
# O site possui captcha para login, não sendo possível fazer de forma automática