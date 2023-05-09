### User Story US00 - Manter Usuário

**Descrição**  O sistema deverá manter um cadastro de usuários, que terão acesso através de um login utilizando um email e senha. Cada usuário deverá fornecer informações básicas para cadastro, como nome, endereço de email, endereço físico, número de CPF, senha e número de telefone. Os usuários terão a liberdade de alterar suas informações pessoais, excluir suas contas do sistema e pesquisar informações de um determinado usuário. Um usuário tem os seguintes atributos: código-ID, nome, email, endereço, CPF, senha e telefone. 


| #    | Requisitos Envolvidos |
| ---- | --------------------- |
| RF001          | Inserir Usuário |
| RF002          | Alterar Usuário  |
| RF003          | Pesquisar Usuários |
| RF004          | Excluir Usuário |

#### Cálculo     

|#                | Valores |
|-----------------|---------|
|RLR              | Usuario 
|DERS             | (nome, cpf, telefone e email)
|ALI              | (Usuario)
|EE               | (Inserir Usuario, Alterar Usuario, Excluir Usuario) 
|CE               | (Pesquisar Usuario)
|Complexidade Funcional das funções de dados | Baixa
|Complexidade Funcional das funções de Transação | Baixa
|
```
1 ALI * 7 = 7
3 EE * 3 = 9
2 CE * 3 = 3
PF = 7+9+3 = 19
```