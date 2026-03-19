# 🐞 Bugs Encontrados

## BUG-01 - Validação incorreta de campos vazios no login

**Severidade:** Média  
**Prioridade:** Média  

**Ambiente:**  
Navegador Chrome - Windows  

**Passos para reproduzir:**
1. Acessar a página de login
2. Deixar os campos de e-mail e senha vazios
3. Clicar no botão de login

**Resultado esperado:**  
Sistema deve exibir mensagens informando que os campos são obrigatórios

**Resultado obtido:**  
Sistema exibe a mensagem "Incorrect email or password."

**Descrição:**  
O sistema deveria informar que os campos estão vazios antes de tentar enviar o formulário, mas ele está enviando o formulário e retornando o erro de "usuário incorreto"

---

## BUG-02 - Ausência de opção para selecionar quantidade de produtos

**Severidade:** Baixa  
**Prioridade:** Baixa  

**Ambiente:**  
Navegador Chrome - Windows  

**Passos para reproduzir:**
1. Acessar a página de produtos
2. Selecionar um produto

**Resultado esperado:**  
Sistema deve permitir selecionar a quantidade do produto

**Resultado obtido:**  
Não há opção para escolher quantidade

**Descrição:**  
O sistema não permite ao usuário definir a quantidade de produtos antes de adicionar ao carrinho.

