# Documento de User Stories

Documento construído a partir do **Modelo BSI - Doc 004 - Lista de User Stories** que pode ser encontrado no link: https://docs.google.com/document/d/1Ns2J9KTpLgNOpCZjXJXw_RSCSijTJhUx4zgFhYecEJg/edit?usp=sharing

## Descrição

Este documento descreve os User Stories criados a partir da Lista de Requisitos no Documento 001 - Documento de Visão. Este documento também pode ser adaptado para descrever User Stories. Modelo de documento baseado nas características do processo easYProcess (YP).

## Histórico de revisões

| Data       | Versão  | Descrição                          | Autor                          |
| :--------- | :-----: | :--------------------------------: | :----------------------------- |
| 18/03/2023 | 0.0.1   | Template e descrição do documento  | David, Manoel, Lucas, Isadora, Ítalo |

### User Story US01 - Manter Usuário

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deverá manter um cadastro de usuários, que terão acesso através de um login utilizando um email e senha. Cada usuário deverá fornecer informações básicas para cadastro, como nome, endereço de email, endereço físico, número de CPF, senha e número de telefone. Os usuários terão a liberdade de alterar suas informações pessoais, excluir suas contas do sistema e pesquisar informações de um determinado usuário. Um usuário tem os seguintes atributos: código-ID, nome, email, endereço, CPF, senha e telefone. |

| **Requisitos Funcionais envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF001          | Inserir Usuário |
| RF002          | Alterar Usuário  |
| RF003          | Pesquisar Usuários |
| RF004          | Excluir Usuário |


|                           |              |
| ------------------------- | -------------|
| **Prioridade**            | Essencial    |
| **Estimativa**            |  10          |
| **Tempo Gasto (real):**   |              |
| **Tamanho Funcional**     |  19          |
| **Analista**              | Italo        |
| **Desenvolvedor**         | Manoel       |
| **Revisor**               | David        |
| **Testador**              | Isadora      |

 
|Contagem |      N       |
|---------|--------------|
|ALI      |      7       |
|EE       |      9       |
|CE       |      3       |


### User Story US03 - Manter Despensa

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | A user story Manter Despensa é uma funcionalidade essencial para o SigDespensa, pois é o pilar principal de todo o sistema, sem ele não haveria SigDespensa. Manter despensa é responsável pela gestão de todo o estoque, sendo composto de requisitos funcionais como: Inserir Despensa, Alterar Despensa, Pesquisar Despensa e Excluir Despensa. Manter Despensa é responsável por inserir novas despensas, editar informações de uma determinada despensa, pesquisar informações sobre uma despensa e até mesmo excluir permanentemente o cadastro de uma despensa. A user story em questão possui os seguintes atributos: código-ID, quantidadeTotal, capacidade e categoria.  |

| **Requisitos Funcionais envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF007          | Inserir Despensa |
| RF008          | Alterar Despensa  |
| RF009          | Pesquisar Despensa        |
| RF019          | Excluir Despensa |


|                           |              |
| ------------------------- | -------------|
| **Prioridade**            | Essencial    |
| **Estimativa**            |   10         |
| **Tempo Gasto (real):**   |              |
| **Tamanho Funcional**     |  19          |
| **Analista**              | Manoel       |
| **Desenvolvedor**         | Italo        |
| **Revisor**               | Isadora      |
| **Testador**              | David        |

 
|Contagem |      N       |
|---------|--------------|
|ALI      |      7       |
|EE       |      9       |
|CE       |      3       |


### User Story US04 - Manter Categoria

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | Manter Categorias é importante para a melhor identificação dos itens contidos em uma despensa, estabelecendo uma categoria para o item que se encontra no estoque. Esta user story é responsável por: inserir uma categoria ao sistema, alterar informações de uma categoria quando necessário, pesquisar por informações específicas de uma categoria e excluir permanentemente o cadastro de uma categoria. Manter Categorias possui os seguintes atributos: código-ID, nome. |

| **Requisitos Funcionais envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF011          | Inserir Categoria |
| RF013          | Alterar Categoria  |
| RF012          | Pesquisar Categoria        |
| RF014          | Excluir Categoria |

### User Story US05 - Manter Item

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | Assim como a user story anterior, Manter Item é uma user story importantíssimo para o funcionamento do SigDespensa. Manter Item é responsável por inserir, alterar, pesquisar e exluir items que se encontram em uma despensa. Semelhante aos outros CRUDS dentro do sistema, é possível inserir um item completamente novo com seus atributos, alterar informações quando necessário, pesquisar o mesmo de acordo com suas informações e até mesmo excluí-lo permanentemente. Manter Item possui os seguintes atributos: código-ID, categoria, marca, tamanho e data de validade. |

| **Requisitos Funcionais envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF017          | Inserir Item |
| RF018          | Alterar Item  |
| RF019          | Pesquisar Item        |
| RF020          | Excluir Item |

### User Story US06 - Monitorar Níveis de Despensa

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | Esta user story é responsável por monitorar os níveis do estoque de um determinado produto dentro da despensa. De início, uma porcentagem é determinada, se ocorrer da quantidade de produtos ficar menor ou igual à porcentagem definida como padrão pelo sistema, os usuários e administradores da despensa serão notificados que os mantimentos estão perto de acabar. |

| **Requisitos Funcionais envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF021          | Monitorar níveis de Despensa |
