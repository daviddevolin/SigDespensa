# Relatório de Testes de Módulo/Sistema

Documento construido a partir do modelo **Modelo BSI - Doc 008 - Relatório de Testes de Módulo/Sistema** que pode ser encontrado no link:
https://docs.google.com/document/d/11hLKf0FcspQrDRfo3gRMXzuY1028cUeniv_Aob8DX_0/edit?usp=sharing
### Legenda
|  Nome      |     Descrição |
| ---------- | ------------- |
|   Teste    | Código ou identificação do Teste. |
| Descrição  | Descrição dos passos e detalhes do teste a ser executado. |
| Especificação | Informações sobre a função testada e se ela de acordo com a especificação do caso de uso.|
| Resultado  |  Resultado do teste, modificações sugeridas ou resultados do teste. No caso de erro ou problema na execução do teste descrever o erro em detalhes e adicionar print's das telas.|

## US00 - Manter Usuário
| Teste | Descrição | Especificação | Resultado |
| ----- | --------- | -------------- | -------- |
| Teste 01: Inserir Usuário | A1 - Inserir Usuário<br> A1.1. O ator preenche os dados;<br> A1.2. O ator clica no botão Enviar;<br>A1.3. O sistema salva os dados<br>A1.4. O sistema retorna para a página de cadastro de Usuário;<br>A1.5. Fim do fluxo. | Especificação OK. | OK.|
| Teste 02: Excluir Usuário | A2 - Excluir Usuário<br>A2.1. O ator executa o fluxo de Listar Usuários;<br>A2.2. O ator clica no botão Excluir;<br>A2.3. O sistema exclui os dados do Usuário;<br>A2.4. O sistema retorna para a página de Usuários;<br>A2.5. Fim do fluxo. | Especificação OK. | OK. |
| Teste 03: Editar Usuário | A3 - Editar Usuário<br>A3.1. O ator executa o fluxo de Listar Usuário;<br>A3.2. O ator clica no botão Editar;<br>A3.3. O sistema redireciona para a página de editar Usuário;<br>A3.4. O ator preenche os dados;<br>A3.5. O ator clica no botão de Editar;<br>A3.6. O sistema salva os dados;<br>A3.7. O sistema redireciona para a página de Usuários;<br>A3.8. Fim do fluxo. | Especificação OK. |OK |
| Teste 04: Listar Usuários | A4 - Listar Usuários<br> A4.1. O ator clica no botão Usuários;<br> A4.2. O sistema redireciona para a página de listagem de Usuários;<br> A4.3. O sistema faz uma consulta aos dados dos Usuários cadastrados;<br> A4.4. O sistema mostra uma mensagem se não houver Usuários cadastrados;<br> A4.5. O sistema lista todos os Usuários na página;<br> A4.6. Fim do fluxo.| Especificação. OK| OK


## US01 - Manter Despensa

| Teste | Descrição | Especificação | Resultado |
| ----- | --------- | -------------- | -------- |
| Teste 01: Incluir Despensa | A1 - Incluir Despensa<br> A1.1. O ator preenche os dados;<br> A1.2. O ator clica no botão Enviar;<br>A1.3. O sistema salva os dados<br>A1.4. O sistema retorna para a página de cadastro de Despensa;<br>A1.5. Fim do fluxo. | Especificação OK. | Ao cadastrar uma despensa, é necessário informar a quantidade total. Além disso, é possível cadastrar mais de uma despensa com as mesmas características, o que pode gerar duplicidade de dados. |
| Teste 02: Excluir Despensa | A2 - Excluir Despensa<br>A2.1. O ator executa o fluxo de Listar Despensas;<br>A2.2. O ator clica no botão Excluir;<br>A2.3. O sistema exclui os dados da Despensa;<br>A2.4. O sistema retorna para a página de Despensas;<br>A2.5. Fim do fluxo. | Especificação OK. | OK. |
| Teste 03: Editar Despensa | A3 - Editar Despensa<br>A3.1. O ator executa o fluxo de Listar Despensas;<br>A3.2. O ator clica no botão Editar;<br>A3.3. O sistema redireciona para a página de editar Despensa;<br>A3.4. O ator preenche os dados;<br>A3.5. O ator clica no botão de Editar;<br>A3.6. O sistema salva os dados;<br>A3.7. O sistema redireciona para a página de Despensas;<br>A3.8. Fim do fluxo. | Especificação OK. | Ao editar uma despensa, a mesma problemática encontrada no teste 01 persiste. Além disso, a possibilidade de cadastrar múltiplas despensas com as mesmas características também deve ser considerada na edição. |
| Teste 04: Listar Despensas | A4 - Listar Despensas<br> A4.1. O ator clica no botão Despensas;<br> A4.2. O sistema redireciona para a página de listagem de Despensas;<br> A4.3. O sistema faz uma consulta aos dados das Despensas cadastradas;<br> A4.4. O sistema mostra uma mensagem se não houver Despensas cadastradas;<br> A4.5. O sistema lista todas as Despensas na página;<br> A4.6. Fim do fluxo. | Especificação OK. | OK. |
| Teste 05: Detalhar Despensa | A5 - Detalhar Despensa<br> A5.1. O ator executa o fluxo de Listar Despensas;<br> A5.2. O ator clica no nome da Despensa;<br> A5.3. O sistema redireciona para a página de detalhes da Despensa;<br> A5.4. A página de detalhes exibe todos os atributos da Despensa;<br> A5.5. Fim do fluxo. | Especificação OK. | Ao clicar no nome da despensa, o redirecionamento para a página de detalhes exibe o erro "despensa_detail() got an unexpected keyword argument 'id'". A página de detalhes deve exibir os valores de todos os atributos da despensa para fornecer uma visão completa das informações. |


## US02 - Manter Categoria

| Teste | Descrição | Especificação | Resultado |
| ----- | --------- | -------------- | -------- |
| Teste 01: Incluir Categoria | A1 - Incluir Categoria<br> A1.1. O ator preenche os dados;<br> A1.2. O ator clica no botão Enviar;<br>A1.3. O sistema salva os dados<br>A1.4. O sistema retorna para a página de cadastro de Categoria;<br>A1.5. Fim do fluxo. | Especificação OK. | OK. |
|Teste 02: Excluir Categoria | A2 - Excluir Categoria<br>A2.1. O ator executa o fluxo de Listar Categorias;<br>A2.2. O ator clica no botão Excluir;<br>A2.3. O sistema exclui os dados da Categoria;<br>A2.4. O sistema retorna para a página de Categorias;<br>A2.5. Fim do fluxo. | Especificação OK. | OK. |
|Teste 03: Editar Categoria | A3 - Editar Categoria<br>A3.1. O ator executa o fluxo de Listar Categorias;<br>A3.2. O ator clica no botão Editar;<br>A3.3. O sistema redireciona para a página de editar Categoria;<br>A3.4. O ator preenche os dados;<br>A3.5. O ator clica no botão de Editar;<br>A3.6. O sistema salva os dados;<br>A3.7. O sistema redireciona para a página de Categorias;<br>A3.8. Fim do fluxo. | Especificação OK. | OK. |
|Teste 04:<br>Listar Categorias | A4 - Listar Categorias<br> A4.1. - O ator clica no botão Categorias;<br> A4.2. - O sistema redireciona para a página de listagem da Categorias;<br>A4.3. O sistema faz uma consulta aos dados das Categorias cadastrados;<br>A4.4. - O sistema mostra uma mensagem se não houver Categorias cadastrados.<br> A4.5. - O sistema lista todas as Categorias na página;<br>A.4.6. Fim do fluxo. | Especificação OK. | OK. |

## US03 - Manter Item

| Teste | Descrição | Especificação | Resultado |
| ----- | --------- | -------------- | -------- |
| Teste 01: Incluir Item | A1 - Incluir Item<br> A1.1. O ator preenche os dados;<br> A1.2. O ator clica no botão Enviar;<br>A1.3. O sistema salva os dados<br>A1.4. O sistema retorna para a página de cadastro de item;<br>A1.5. Fim do fluxo. | Especificação OK. | OK. |
|Teste 02: Excluir Item | A2 - Excluir Item<br>A2.1. O ator executa o fluxo de Listar Itens;<br>A2.2. O ator clica no botão Excluir;<br>A2.3. O sistema exclui os dados do item;<br>A2.4 O sistema retorna para a página de itens;<br>A2.5. Fim do fluxo. | Especificação OK. | OK. |
|Teste 03: Editar Item | A3 - Editar Item<br>A3.1. O ator executa o fluxo de Listar Itens;<br>A3.2. O ator clica no botão Editar;<br>A3.3. O sistema redireciona para a página de editar item;<br>A3.4. O ator preenche os dados;<br>A3.5. O ator clica no botão de Atualizar;<br>A3.6. O sistema salva os dados;<br>A3.7 O sistema redireciona para a página de itens;<br>A3.8 Fim do fluxo. | Especificação OK. | OK. |
|Teste 04:<br>Listar Itens | A4 - Listar Itens<br> A4.1. - O ator clica no botão Itens;<br> A4.2. - O sistema redireciona para a página de listagem de itens;<br>A4.3 O sistema faz uma consulta aos dados dos itens cadastrados;<br>A4.4. - O sistema mostra uma mensagem se não houver itens cadastrados.<br> A4.5. - O sistema lista todos os itens na página;<br>A.4.6. Fim do fluxo. | Especificação OK. | OK. |
