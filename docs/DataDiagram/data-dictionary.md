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
| telefone      | representa o numero para contato do usuário | INT      | 11      | Unique / Not Null             |

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

