# Documento de Visão

Documento construído a partido do **Modelo BSI - Doc 001 - Documento de Visão** que pode ser encontrado no
link: https://docs.google.com/document/d/1DPBcyGHgflmz5RDsZQ2X8KVBPoEF5PdAz9BBNFyLa6A/edit?usp=sharing

## Equipe e Definição de Papéis

Membro     |     Papel   |   E-mail   |    Github   |
---------  | ----------- | ---------- |  ---------- |
David      | Gerente, Analista | davidccb@live.com | daviddevolin |
Manoel     | Analista | manoel.anizio456@gmail.com | manizio |
Lucas     | Analista | lucascantodev@gmail.com | lucascantodev |
Isadora   | Analista | isadorashs1@gmail.com | isadorazs |
Ítalo   | Analista | italog09@gmail.com | italoguil |


### Matriz de Competências

Membro     |     Competências   |
---------  | ----------- |
David      | Full-Stack Developer - Python, C, Java, JavaScript, HTML, CSS, React.js, MySQL, Django |
Manoel | Desenvolvedor Python, Java, C/C++, JavaScript, HTML, CSS, React.js, MySQL, Django |
Lucas | Desenvolvedor JavaScript, HTML, CSS, React.js, NextJS, Node, MySQL |
Isadora | Desenvolvedora Python, Java, C/C++, JavaScript, HTML, CSS, React.js, MySQL, Django |
Ítalo | Desenvolvedora Python, Java, C/C++, JavaScript, HTML, CSS, React.js, MySQL, Django |


## Perfis dos Usuários

O sistema poderá ser utilizado por diversos usuários. Temos os seguintes perfis/atores:

Perfil                                 | Descrição   |
---------                              | ----------- |
Administrador | Este usuário realiza os cadastros de despensas e pode realizar qualquer função.
Usuário | Este usuário pode visualizar, adicionar, remover e editar itens da despensa

## Lista de Requisitos Funcionais

Requisito                                 | Descrição   | Ator |
---------                                 | ----------- | ---------- |
RF001 - Inserir Usuário     | Um usuário representa um usuário autorizado para adicionar, remover e editar itens da despensa. Um Usuário tem: código-ID, nome, email, endereço, cpf, senha, telefone. | Usuário |
RF002 - Alterar um Usuário | Editar um usuário tem:  código-ID, nome, email, endereço, cpf, senha, telefone. | Usuário |
RF003 - Excluir Usuário |  Excluir Usuário tem: código-ID, email, CPF e senha. Remove permanentemente o cadastro do Usuário| Usuário, Administrador|
RF004 - Inserir Administrador | Um administrador representa um usuário com acesso completo ao sistema, podendo utilizar de todas as funções disponíveis. Um administrador tem código-ID, nome, senha, endereço, cpf, email e uma chave de registro. | Administrador |
RF005 - Alterar Administrador | Editar um Administrador tem:  código-ID, nome, email, endereço, cpf, senha, telefone. | Administrador|
RF006 - Excluir Administrador | Excluir Administrador tem: código-ID, email, CPF e senha. Remove permanentemente o cadastro do Administrador| Administrador|
RF007 - Manter o cadastro de Depósito | Um depósito tem um número, capacidade, tamanho e categoria. | Administrador |
RF008 - Manter cadastro de Categorias | As categorias estabelecem que tipo de item pode ser armazenado em determinado deposito. Uma catégoria tem: código-ID e nome. | Administrador |
RF009 - Cadastro de Horários de serviço | Um horário de serviço tem: um dia de semana, um turno, uma ordem (ordenação/identificador), uma hora de início, uma hora de final | Administrador |
RF010 - 
RF011 -  Cadastro do Histórico  | Um Histórico tem: codigo-ID, e horários, data, ID-usuário. Um histórico ira constar, todo o acesso e movimentação feita por cada usuário ao depósito. | Cliente, Administrador |

### Modelo Conceitual

Abaixo apresentamos o modelo conceitual usando o **YUML**.

 ![Modelo UML](yuml/monitoria-modelo.png)

O código que gera o diagrama está [Aqui!](yuml/monitoria-yuml.md). O detalhamento dos modelos conceitual e de dados do projeto estão no [Documento de Modelos](doc-modelos.md).

#### Descrição das Entidades

## Lista de Requisitos Não-Funcionais

Requisito                                 | Descrição   |
---------                                 | ----------- |
RNF001 - Deve ser acessível via navegador | Deve abrir perfeitamento no Firefox e no Chrome. |
RNF002 - Consultas deve ser eficiente | O sistema deve executar as consultas em milessegundos |
RNF003 - Log e histórico de acesso e funções | Deve manter um log de todos os acessos e das funções executadas pelo usuário |

## Riscos

Tabela com o mapeamento dos riscos do projeto, as possíveis soluções e os responsáveis.

Data | Risco | Prioridade | Responsável | Status | Providência/Solução |
------ | ------ | ------ | ------ | ------ | ------ |
16/03/2023 | Implementação de protótipo com as tecnologias | Alto | Todos | Vigente | Procurar por materiais de ensino abrangentes sobre a tecnologia em questão e realizar um caso simples de implementação como exercício inicial |
16/03/2023 | Falta de conhecimento das tecnologias | Alto | Todos | Vigente |Pesquisar tutoriais, assistir aulas sobre o assunto |
16/03/2023 | Distribuição inadequada de responsabilidades | Médio | Gerente | Vigente | Compreender precisamente as demandas do cliente em cada interação e ser pragmático ao estabelecer o que produzir diante do tempo disponível dos colaboradores da equipe |
16/03/2023 | Atrasos na entrega de tarefas | Alta | Todos | Vigente |  planejar e executar as atividades com antecedência, sem deixar de dedicar um pouco do tempo de cada dia ao projeto |

### Referências
