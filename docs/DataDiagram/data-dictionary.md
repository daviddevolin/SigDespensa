## Dicionário de Dados

## Inserir Usuário

|   Tabela   | Inserir Usuário  |
| ---------- | ------------- |
| Descrição  | Cadastra usuários no sistema|

|  Nome         | Descrição                                                    | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | ------------------------------------------------------------ | ------------ | ------- | --------------------- |
| código-ID          | identificador gerado pelo SGBD                               | INT          | ---     | PK / Identity         |
| nome          | representa o nome do usuário                      | VARCHAR      | 150     | Not Null              |
| email      | representa o e-mail escolhido pelo usuário | VARCHAR      | 50      | Unique / Not Null     |
| senha      | representa a senha de usuário | VARCHAR      | 50      | Unique / Not  Null             |
| endereço      | representa o local de moradia do usuário | VARCHAR      | 100      | Not Null              |
| CPF      | representa o Cadastro de Pessoa Física do usuário | VARCHAR      | 11      | Unique / Not Null              |
| telefone      | representa o numero para contato do usuário | INT      | 11      | Unique / Not Null             |

## Alterar Usuário

|   Tabela   | Alterar Usuário  |
| ---------- | ------------- |
| Descrição  | Altera os dados cadastrados pelo usuários no sistema|

|  Nome         | Descrição                                                    | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | ------------------------------------------------------------ | ------------ | ------- | --------------------- |
| nome          | representa o nome do usuário                      | VARCHAR      | 150     | Not Null              |
| email      | representa o e-mail escolhido pelo usuário | VARCHAR      | 50      | Unique / Not Null     |
| senha      | representa a senha de usuário | VARCHAR      | 50      | Unique / Not  Null             |
| endereço      | representa o local de moradia do usuário | VARCHAR      | 100      | Not Null              |
| CPF      | representa o Cadastro de Pessoa Física do usuário | VARCHAR      | 11      | Unique / Not Null              |
| telefone      | representa o número para contato do usuário | INT      | 11      | Unique / Not Null             |

## Pesquisar Usuário

|   Tabela   | Pesquisar Usuário  |
| ---------- | ------------- |
| Descrição  | Pesquisa usuários no sistema|

|  Nome         | Descrição                                                    | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | ------------------------------------------------------------ | ------------ | ------- | --------------------- |
| código-ID          | identificador gerado pelo SGBD                               | INT          | ---     | PK / Identity         |

## Excluir Usuário

|   Tabela   | Excluir Usuário  |
| ---------- | ------------- |
| Descrição  | Exclui usuários do sistema|

|  Nome         | Descrição                                                    | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | ------------------------------------------------------------ | ------------ | ------- | --------------------- |
| código-ID          | identificador gerado pelo SGBD                               | INT          | ---     | PK / Identity         |
| email      | representa o e-mail escolhido pelo usuário | VARCHAR      | 50      | Unique / Not Null     |
| CPF      | representa o Cadastro de Pessoa Física do usuário | VARCHAR      | 11      | Unique / Not Null              |
| senha      | representa a senha de usuário | VARCHAR      | 50      | Unique / Not  Null             |

## Inserir Administrador

|   Tabela   | Inserir Administrador  |
| ---------- | ------------- |
| Descrição  | Cadastra administradores no sistema|

|  Nome         | Descrição                                                    | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | ------------------------------------------------------------ | ------------ | ------- | --------------------- |
| código-ID          | identificador gerado pelo SGBD                               | INT          | ---     | PK / Identity         |
| nome          | representa o nome do administrador                      | VARCHAR      | 150     | Not Null              |
| email      | representa o e-mail escolhido pelo administrador | VARCHAR      | 50      | Unique / Not Null     |
| senha      | representa a senha de administrador | VARCHAR      | 50      | Unique / Not  Null             |
| endereço      | representa o local de moradia do administrador | VARCHAR      | 100      | Not Null              |
| CPF      | representa o Cadastro de Pessoa Física do administrador | VARCHAR      | 11      | Unique / Not Null              |
| telefone      | representa o número para contato do administrador | INT      | 11      | Unique / Not Null             |

## Alterar Administrador

|   Tabela   | Alterar Administrador  |
| ---------- | ------------- |
| Descrição  | Altera administradores no sistema|

|  Nome         | Descrição                                                    | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | ------------------------------------------------------------ | ------------ | ------- | --------------------- |
| nome          | representa o nome do administrador                      | VARCHAR      | 150     | Not Null              |
| email      | representa o e-mail escolhido pelo administrador | VARCHAR      | 50      | Unique / Not Null     |
| senha      | representa a senha de administrador | VARCHAR      | 50      | Unique / Not  Null             |
| endereço      | representa o local de moradia do administrador | VARCHAR      | 100      | Not Null              |
| CPF      | representa o Cadastro de Pessoa Física do administrador | VARCHAR      | 11      | Unique / Not Null              |
| telefone      | representa o número para contato do administrador | INT      | 11      | Unique / Not Null             |

## Excluir Administrador

|   Tabela   | Excluir Administrador  |
| ---------- | ------------- |
| Descrição  | Exclui administradores no sistema|

|  Nome         | Descrição                                                    | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | ------------------------------------------------------------ | ------------ | ------- | --------------------- |
| código-ID          | identificador gerado pelo SGBD                               | INT          | ---     | PK / Identity         |
| email      | representa o e-mail escolhido pelo administrador | VARCHAR      | 50      | Unique / Not Null     |
| senha      | representa a senha de administrador | VARCHAR      | 50      | Unique / Not  Null             |
| CPF      | representa o Cadastro de Pessoa Física do administrador | VARCHAR      | 11      | Unique / Not Null              |

## Inserir Despensa

|   Tabela   | Inserir Despensa  |
| ---------- | ------------- |
| Descrição  | Cadastra despensa no sistema|

|  Nome         | Descrição                                                    | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | ------------------------------------------------------------ | ------------ | ------- | --------------------- |
| código-ID          | identificador gerado pelo SGBD                               | INT          | ---     | PK / Identity         ||
| quantTotal          | quantidade total de produtos na despensa                               | INT          | 300     | Not Null       |
| capacidade          | capacidade total de produtos na despensa                               | INT          | 300     | Not Null         |
| categoria          | categoria dos produtos da despensa                               | VARCHAR          | ---    | Not Null         | 

## Alterar Despensa

|   Tabela   | Alterar Despensa  |
| ---------- | ------------- |
| Descrição  | Edita as informações de uma determinada Despensa|

|  Nome         | Descrição                                                    | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | ------------------------------------------------------------ | ------------ | ------- | --------------------- |
| quantTotal          | quantidade total de produtos na despensa                               | INT          | 300     | Not Null       |
| capacidade          | capacidade total de produtos na despensa                               | INT          | 300     | Not Null         |
| categoria          | categoria dos produtos da despensa                               | VARCHAR          | ---    | Not Null         | 

## Pesquisar Despensa

|   Tabela   | Pesquisar Despensa  |
| ---------- | ------------- |
| Descrição  | Pesquisa informações sobre uma despensa|

|  Nome         | Descrição                                                    | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | ------------------------------------------------------------ | ------------ | ------- | --------------------- |
| código-ID          | identificador gerado pelo SGBD                               | INT          | ---     | PK / Identity         ||

## Excluir Despensa

|   Tabela   | Excluir Despensa  |
| ---------- | ------------- |
| Descrição  |Remove permanentemente o cadastro de uma despensa|

|  Nome         | Descrição                                                    | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | ------------------------------------------------------------ | ------------ | ------- | --------------------- |
| código-ID          | identificador gerado pelo SGBD                               | INT          | ---     | PK / Identity         ||

## Inserir Categoria

|   Tabela   | Inserir Categoria  |
| ---------- | ------------- |
| Descrição  | Categoria estabelece que tipo de item pode ser armazenado em determinado depósito|

|  Nome         | Descrição                                                    | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | ------------------------------------------------------------ | ------------ | ------- | --------------------- |
| código-ID          | identificador gerado pelo SGBD                               | INT          | ---     | PK / Identity         |
| nome          | representa o nome da categoria                      | VARCHAR      | 150     | Not Null              |

## Alterar Categoria

|   Tabela   | Alterar Categoria  |
| ---------- | ------------- |
| Descrição  | Edita informações de uma categoria|

|  Nome         | Descrição                                                    | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | ------------------------------------------------------------ | ------------ | ------- | --------------------- |
| código-ID          | identificador gerado pelo SGBD                               | INT          | ---     | PK / Identity         |
| nome          | representa o nome da categoria                      | VARCHAR      | 150     | Not Null              |

## Pesquisar Categoria

|   Tabela   | Pesquisar Categoria  |
| ---------- | ------------- |
| Descrição  | Pesquisa as informações de uma categoria|

|  Nome         | Descrição                                                    | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | ------------------------------------------------------------ | ------------ | ------- | --------------------- |
| nome          | representa o nome da categoria                      | VARCHAR      | 150     | Not Null              |

## Excluir Categoria

|   Tabela   | Excluir Categoria  |
| ---------- | ------------- |
| Descrição  | Remove permanentemente o cadastro de uma categoria|

|  Nome         | Descrição                                                    | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | ------------------------------------------------------------ | ------------ | ------- | --------------------- |
| código-ID          | identificador gerado pelo SGBD                               | INT          | ---     | PK / Identity         |

## Cadastro do Histórico

|   Tabela   | Cadastro do Histórico  |
| ---------- | ------------- |
| Descrição  | Um Histórico irá constar, todo o acesso e movimentação feita por cada usuário ao despensa|

|  Nome         | Descrição                                                    | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | ------------------------------------------------------------ | ------------ | ------- | --------------------- |
| código-ID          | identificador gerado pelo SGBD                               | INT          | ---     | PK / Identity         |            |
| horários      | representa a hora em que a movimentação foi feita | DATETIME      | ---      | Unique / Not Null     |
| data      | representa a data em que a movimentação foi feita | DATETIME      | ---      | Unique / Not  Null             |
| código-ID do user          | Código ID do usuário que executou a movimentação                               | INT          | ---     | PK / Identity         |            |