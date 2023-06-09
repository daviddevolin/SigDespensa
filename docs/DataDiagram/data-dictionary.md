## Dicionário de Dados

## Usuário

|   Tabela   |  Usuário  |
| ---------- | ------------- |
| Descrição  | Armazena as informações do usuario|

|  Nome         | Descrição                      | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------| ------------ | ------- | --------------------- |
| id     | identificador gerado pelo SGBD |       INT    |   ---   | PK / Identity        |
| nome          | representa o nome do usuário   | VARCHAR      |   150   | Not Null           |
| email         | representa o e-mail escolhido pelo usuário | VARCHAR      |   50   | Unique / Not Null     |
| senha         | representa a senha de usuário  | VARCHAR      | 50      | Unique / Not  Null  |
| CPF | representa o Cadastro de Pessoa Física do usuário | VARCHAR      | 11      | Unique / Not Null              |
| telefone      | representa o numero para contato do usuário | INT      | 11      | Unique / Not Null             |


## Despensa

|   Tabela   | Inserir Despensa  |
| ---------- | ------------- |
| Descrição  | Cadastra despensa no sistema|

|  Nome         | Descrição                                                    | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | ------------------------------------------------------------ | ------------ | ------- | --------------------- |
| id          | identificador gerado pelo SGBD                               | INT          | ---     | PK / Identity         ||
| quantTotal          | quantidade total de produtos na despensa                               | INT          | 300     | Not Null       |
| capacidade          | capacidade total de produtos na despensa                               | INT          | 300     | Not Null         |
| categoria          | categoria dos produtos da despensa                               | VARCHAR          | ---    | Not Null         | 

## Categoria

|   Tabela   | Inserir Categoria  |
| ---------- | ------------- |
| Descrição  | Categoria estabelece que tipo de item pode ser armazenado em determinado depósito|

|  Nome         | Descrição                                                    | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | ------------------------------------------------------------ | ------------ | ------- | --------------------- |
| id          | identificador gerado pelo SGBD                               | INT          | ---     | PK / Identity         |
| nome          | representa o nome da categoria                      | VARCHAR      | 150     | Unique / Not Null              |

## Histórico

|   Tabela   | Cadastro do Histórico  |
| ---------- | ------------- |
| Descrição  | Um Histórico irá constar, todo o acesso e movimentação feita por cada usuário ao despensa|

|  Nome         | Descrição                                                    | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | ------------------------------------------------------------ | ------------ | ------- | --------------------- |
| id          | identificador gerado pelo SGBD                               | INT          | ---     | PK / Identity         |            |
| horários      | representa a hora em que a movimentação foi feita | DATETIME      | ---      | Unique / Not Null     |
| data      | representa a data em que a movimentação foi feita | DATETIME      | ---      | Unique / Not  Null             |
| user_id          | Código ID do usuário que executou a movimentação                               | INT          | ---     | PK / Identity         |            |

## Item

|   Tabela   | Inserir Item  |
| ---------- | ------------- |
| Descrição  | Um Item representa um produto ou objeto que pode ser armazenado e gerenciado no sistema|

|  Nome         | Descrição                                                    | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | ------------------------------------------------------------ | ------------ | ------- | --------------------- |
| id          | identificador gerado pelo SGBD                               | INT          | ---     | PK / Identity         ||
| nome          | representa o nome do item                      | VARCHAR      | 150     | Not Null              |
| categoria          | representa qual a cadegoria do item                               | VARCHAR          | ---     | Not Null       |
| marca          | Representa qual é a marca do item                               | VARCHAR          | 300     | Not Null         |
| peso          | representa o peso dos produtos                               | FLOAT          | ---    | Not Null         | 
| data_de_validade     | representa a data de validade dos produtos | DATETIME      | ---      | Unique / Not  Null         