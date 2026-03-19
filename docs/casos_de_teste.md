# 🧪 Casos de Teste - Sauce Demo


## CT-01 - Criar usuário com sucesso

**Pré-condição:**  
Usuário não possui cadastro no sistema

**Passos:**
1. Acessar a página de cadastro
2. Inserir nome válido
3. Inserir sobrenome válido
4. Inserir e-mail válido
5. Inserir senha válida
6. Clicar no botão de cadastro

**Resultado esperado:**  
Sistema deve criar a conta e redirecionar o usuário para sua área logada

---

## CT-02 - Login com sucesso

**Pré-condição:**  
Usuário cadastrado no sistema

**Passos:**
1. Acessar a página de login
2. Inserir e-mail válido
3. Inserir senha válida
4. Clicar no botão de login

**Resultado esperado:**  
Usuário deve ser redirecionado para sua conta

---

## CT-03 - Adicionar produto ao carrinho

**Pré-condição:**  
Usuário logado no sistema

**Passos:**
1. Acessar a página de produtos
2. Selecionar um produto
3. Clicar no botão "Adicionar ao carrinho"

**Resultado esperado:**  
Produto deve ser adicionado ao carrinho

---

## CT-04 - Finalizar compra

**Pré-condição:**  
Usuário logado e com produtos no carrinho

**Passos:**
1. Acessar o carrinho
2. Clicar no botão de finalizar compra
3. Preencher os dados obrigatórios
4. Confirmar a compra

**Resultado esperado:**  
Sistema deve processar o pedido e exibir confirmação de compra

---

## CT-05 - Criar usuário com email já cadastrado

**Resultado esperado:**  
Sistema deve exibir erro informando que o e-mail já está cadastrado

---

## CT-06 - Realizar login com email/senha errados

**Resultado esperado:**  
Sistema deve exibir erro informando que o e-mail ou senha estão incorretos

---

## CT-07 - Login com campos vazios

**Resultado esperado:**  
Sistema deve exibir validação de campos obrigatórios

---

## CT-08 - Mudanças no carrinho 

**Pré-condição:**  
Ter produtos no carrinho de compras

**Passos:**
1. Usuário acessa o carrinho
2. Clica no botão para excluir um item

**Resultado esperado:**  
Sistema deve remover o item do carrinho 

---

## CT-09 - Finalizar compra sem preencher dados

**Resultado esperado:**  
Sistema deve impedir a finalização e exibir erro

---

## CT-10 - Buscar itens do sistema

**Resultado esperado:**  
O sistema deve retornar os produtos relacionados a pesquisa realizada

