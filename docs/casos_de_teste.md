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
Sistema deve criar a conta

**Resultado obtido:**  
A conta foi criada com sucesso

**Status:**  
✅ Passou

**Observações:**  
Sem nenhum erro

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

**Resultado obtido:**  
O login foi realizado com sucesso

**Status:**  
✅ Passou

**Observações:**  
Sem nenhum erro, o usuário foi redirecionado corretamente

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

**Resultado obtido:**  
O produto foi adicionado com sucesso

**Status:**  
✅ Passou

**Observações:**  
Sem nenhum erro, mas não é possível escolher a quantidade de produtos que desejo comprar diretamente no produto 

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

**Resultado obtido:**  
O sistema redireciona corretamente durante todo o processo

**Status:**  
❌ Falhou

**Observações:**  
Não foi possível finalizar a compra devido à necessidade de dados bancários. O fluxo não pôde ser concluído.

---

## CT-05 - Criar usuário com email já cadastrado

**Resultado esperado:**  
Sistema deve exibir erro informando que o e-mail já está cadastrado

**Resultado obtido:**  
O sistema gera um erro e não cria a conta

**Status:**  
✅ Passou

**Observações:**  
ERRO GERADO: This email address is already associated with an account. If this account is yours, you can <a href="/account/login#recover">reset your password</a>

---

## CT-06 - Realizar login com email/senha errados

**Resultado esperado:**  
Sistema deve exibir erro informando que o e-mail ou senha estão incorretos

**Resultado obtido:**  
O sistema gera um erro e não permite fazer login no sistema 

**Status:**  
✅ Passou

**Observações:** 
Incorrect email or password.

---

## CT-07 - Login com campos vazios

**Resultado esperado:**  
Sistema deve exibir validação de campos obrigatórios

**Resultado obtido:**  
O sistema gera um erro e não permite fazer login no sistema 

**Status:**  
✅ Passou

**Observações:** 
ERRO GERADO: Incorrect email or password.
O tratamento para esse erro deveria ser melhor, o sistema apenas valida que não há correspondência entre o login e a senha, mas deveria ser feito uma verificação se o campo está vazio ou não diretamente no formulário

---

## CT-08 - Mudanças no carrinho 

**Pré-condição:**  
Ter produtos no carrinho de compras

**Passos:**
1. Usuário acessa o carrinho
2. Clica no botão para excluir um item

**Resultado esperado:**  
Sistema deve remover o item do carrinho 

**Resultado obtido:**  
O sistema remove o produto do carrinho

**Status:**  
✅ Passou

**Observações:** 
Sem nenhum erro

---

## CT-09 - Finalizar compra sem preencher dados

**Resultado esperado:**  
Sistema deve impedir a finalização e exibir erro

**Resultado obtido:**  
O sistema não permite finalizar a compra sem os campos preenchidos corretamente

**Status:**  
✅ Passou
 

---

## CT-10 - Buscar itens do sistema

**Resultado esperado:**  
O sistema deve retornar os produtos relacionados a pesquisa realizada

**Resultado obtido:**  
O sistema realiza buscar de forma correta, trazendo os produtos corretos de acordo com o que está no campo de pesquisa

**Status:**  
✅ Passou
 

