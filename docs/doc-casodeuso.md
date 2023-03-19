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
| RF001          | Inserir Administrador |
| RF002          | Alterar Administrador  |
| RF003          | Pesquisar Usuários        |
| RF004          | Excluir Administrador |