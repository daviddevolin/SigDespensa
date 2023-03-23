# Documento de Casos De Uso

Documento construído a partir do **Modelo BSI - Doc 004 - Lista de User Stories** que pode ser encontrado no link: https://docs.google.com/document/d/1Ns2J9KTpLgNOpCZjXJXw_RSCSijTJhUx4zgFhYecEJg/edit?usp=sharing

## Descrição

Este documento descreve os User Stories criados a partir da Lista de Requisitos no Documento 001 - Documento de Visão. Este documento também pode ser adaptado para descrever Casos de Uso. Modelo de documento baseado nas características do processo easYProcess (YP).

## Histórico de revisões

| Data       | Versão  | Descrição                          | Autor                          |
| :--------- | :-----: | :--------------------------------: | :----------------------------- |
| 18/03/2023 | 0.0.1   | Template e descrição do documento  | David, Manoel, Lucas, Isadora, Ítalo |

### Caso de Uso CDU01 - Manter Usuário

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deverá manter um cadastro de usuários, que terão acesso através de um login utilizando um email e senha. Cada usuário deverá fornecer informações básicas para cadastro, como nome, endereço de email, endereço físico, número de CPF, senha e número de telefone. Os usuários terão a liberdade de alterar suas informações pessoais, excluir suas contas do sistema e pesquisar informações de um determinado usuário. Um usuário tem os seguintes atributos: código-ID, nome, email, endereço, cpf, senha e telefone. |

| **Requisitos Funcionais envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF001          | Inserir Usuário |
| RF002          | Alterar Usuário  |
| RF003          | Pesquisar Usuários        |
| RF004          | Excluir Usuário |

### Caso de Uso CDU02 - Manter Administrador

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O caso de uso "Manter Administrador" é de extrema importância para o sistema da despensa, pois é responsável pela gestão das informações de usuário com privilégios administrativos. Por meio desse caso de uso, o Administrador terá acesso através de um login utilizando um email e senha. Cada administrador deverá fornecer informações básicas para cadastro, como nome, endereço de email, cpf, endereço, senha e chave de registro. Os administradores terão liberdade de alterar suas informações pessoais, excluir suas contas do sistema e pesquisar informações de um determinado usuário. O administrador tem os seguintes atributos: código-ID, nome, senha, endereço, cpf, email e uma chave de registro. |

| **Requisitos Funcionais envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF004          | Inserir Administrador |
| RF005          | Alterar Administrador  |
| RF003          | Pesquisar Usuários        |
| RF006          | Excluir Administrador |

### Caso de Uso CDU03 - Manter Despensa

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O caso de uso Manter Despensa é uma funcionalidade essencial para o SigDespensa, pois é o pilar principal de todo o sistema, sem ele não haveria SigDespensa. Manter despensa é responsável pela gestão de todo o estoque, sendo composto de requisitos funcionais como: Inserir Despensa, Alterar Despensa, Pesquisar Despensa e Excluir Despensa. Manter Despensa é responsável por inserir novas despensas, editar informações de uma determinada despensa, pesquisar informações sobre uma despensa e até mesmo excluir permanentemente o cadastro de uma despensa. O caso de uso em questão possui os seguintes atributos: código-ID, quantidadeTotal, capacidade e categoria.  |

| **Requisitos Funcionais envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF007          | Inserir Despensa |
| RF008          | Alterar Despensa  |
| RF009          | Pesquisar Despensa        |
| RF019          | Excluir Despensa |


### Caso de Uso CDU04 - Manter Categoria

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | Manter Categorias é importante para a melhor identificação dos itens contidos em uma despensa, estabelecendo uma categoria para o item que se encontra no estoque. Este caso de uso é responsável por: inserir uma categoria ao sistema, alterar informações de uma categoria quando necessário, pesquisar por informações específicas de uma categoria e excluir permanentemente o cadastro de uma categoria. Manter Categorias possui os seguintes atributos: código-ID, nome. |

| **Requisitos Funcionais envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF011          | Inserir Categoria |
| RF013          | Alterar Categoria  |
| RF012          | Pesquisar Categoria        |
| RF014          | Excluir Categoria |

### Caso de Uso CDU05 - Manter Item

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | Assim como o caso de uso anterior, Manter Item é um caso de uso importantíssimo para o funcionamento do SigDespensa. Manter Item é responsável por inserir, alterar, pesquisar e exluir items que se encontram em uma despensa. Semelhante aos outros CRUDS dentro do sistema, é possível inserir um item completamente novo com seus atributos, alterar informações quando necessário, pesquisar o mesmo de acordo com suas informações e até mesmo excluí-lo permanentemente. Manter Item possui os seguintes atributos: código-ID, categoria, marca, tamanho e data de validade. |

| **Requisitos Funcionais envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF017          | Inserir Item |
| RF018          | Alterar Item  |
| RF019          | Pesquisar Item        |
| RF020          | Excluir Item |

### Caso de Uso CDU06 - Monitorar Níveis de Despensa

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | Este caso de uso é responsável por monitorar os níveis do estoque de um determinado produto dentro da despensa. De início, uma porcentagem é determinada, se ocorrer da quantidade de produtos ficar menor ou igual à porcentagem definida como padrão pelo sistema, os usuários e administradores da despensa serão notificados que os mantimentos estão perto de acabar. |

| **Requisitos Funcionais envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF021          | Monitorar níveis de Despensa |