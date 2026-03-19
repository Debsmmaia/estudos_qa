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

## BUG-03 - Carrinho de compras não abre no primeiro acesso

**Severidade:** Alta
**Prioridade:** Alta

**Ambiente:**  
Navegador Chrome - Windows  

**Passos para reproduzir:**
1. Acessar a página inicial
2. Selecionar um produto
3. Adicionar um produto ao carrinho
4. CLicar no botão do carrinho

**Resultado esperado:**  
Sistema deve carregar o carrinho com todos os itens escolhidos do cliente de forma rápida

**Resultado obtido:**  
O carrinho de compras não carrega e não abre

**Descrição:**  
O sistema não carrega o carrinho no primeiro acesso, sendo necessário ou recarregar a página ou fechar a abrir novamente

