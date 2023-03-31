# Documento de Visão

Documento construído a partir do **Modelo BSI - Doc 001 - Documento de Visão** que pode ser encontrado no
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
Ítalo | Desenvolvedor Python, Java, C/C++, JavaScript, HTML, CSS, React.js, MySQL, Django |


## Perfis dos Usuários

O sistema poderá ser utilizado por diversos usuários. Temos os seguintes perfis/atores:

Perfil                                 | Descrição   |
---------                              | ----------- |
Administrador | Este usuário realiza os cadastros de despensas e pode realizar qualquer função.
Usuário | Este usuário pode visualizar, adicionar, remover e editar itens da despensa

## Lista de Requisitos Funcionais

Requisito                                 | Descrição   | Ator |
---------                                 | ----------- | ---------- |
RF001 - Inserir Usuário     | Um usuário representa um usuário autorizado para adicionar, remover e editar itens da despensa. Um Usuário tem: código-ID, nome, email, endereço, CPF, senha e telefone. | Administrador, Usuário |
RF002 - Alterar Usuário | Edita as informações de um determinado Usuário. Alterar um usuário tem: nome, email, endereço, CPF, senha e telefone. | Administrador, Usuário |
RF003 - Pesquisar Usuário | Pesquisa informações de um determinado usuário. Pesquisar usuário tem: código-ID | Administrador, Usuário
RF003 - Excluir Usuário | Remove permanentemente o cadastro do Usuário. Excluir Usuário tem: código-ID, email, CPF e senha. | Administrador, Usuário|
RF004 - Inserir Administrador | Um administrador representa um usuário com acesso completo ao sistema, podendo utilizar de todas as funções disponíveis. Um administrador tem: código-ID, nome, senha, endereço, CPF, email e uma chave de registro. | Administrador |
RF005 - Alterar Administrador | Edita as informações de um Administrador. Alterar Administrador tem: nome, email, endereço, CPF, senha e telefone. | Administrador|
RF006 - Excluir Administrador | Remove permanentemente o cadastro do Administrador. Excluir Administrador tem: código-ID, email, CPF e senha. | Administrador|
RF007 - Inserir Despensa | A Despensa é onde estará o estoque de produtos. Uma Despensa tem: código-ID, quantidadeTotal, capacidade, e categoria. | Administrador |
RF008 - Alterar Despensa | Edita as informações de uma determinada Despensa. Alterar uma despensa tem: quantidadeTotal, capacidade, e categoria | Administrador |
RF009 - Pesquisar Despensa | Pesquisa informações sobre uma despensa. Pesquisar despensa tem: código-ID. | Administrador, Usuário |
RF010 - Excluir Despensa | Remove permanentemente o cadastro de uma despensa. Excluir despensa tem: código-ID | Administrador |
RF011 - Inserir Categoria |  Categoria estabelece que tipo de item pode ser armazenado em determinado depósito. Uma Categoria tem: código-ID e nome. | Administrador |
RF013 - Alterar Categoria | Edita informações de uma categoria. Editar categoria tem: código-ID, nome | Administrador |
RF012 - Pesquisar Categoria | Pesquisa informações de uma categoria. Pesquisar categoria tem: nome | Administrador, Usuário |
RF014 - Excluir Categoria | Remove permanentemente o cadastro de uma categoria. Excluir categoria tem: código-ID | Administrador |
RF015 - Cadastro do Histórico  | Um Histórico irá constar, todo o acesso e movimentação feita por cada usuário ao despensa. Um Histórico tem: codigo-ID, e horários, data e ID-usuário.  | Administrador, Usuário |
RF016 - Inserir Item | Um Item representa um produto ou objeto que pode ser armazenado e gerenciado no sistema. Um Item tem: código-ID, categoria, marca, tamanho e data de validade | Administrador, Usuário |
RF017 - Alterar Item | Altera as informações de um determinado item. Alterar um Item tem: código-ID, categoria, marca, tamanho e data de validade | Administrador, Usuário |
RF018 - Pesquisar Item | Pesquisa informações de um item. Pesquisar item tem: código-ID | Administrador, Usuário |
RF019 - Excluir Item | Remove permanentemente um Item da despensa. Excluir um Item tem: código-ID, categoria, marca, tamanho e data de validade | Administrador, Usuário |
RF020 - Monitorar níveis de Despensa | Monitora os níveis do estoque de um determinado produto dentro da despensa. Monitorar níveis de Despensa tem: código-ID, porcentagem | Administrador, Usuário |

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
RNF004 - Usabilidade | Deve ser fácil de usar e intuitivo para o usuário. |
RNF005 - Bom desempenho | Deve ser rápido, mesmo quando lida com grandes quantidades de dados ou processos complexos. |
RNF006 - Segurança | Deve ser seguro e funcionar sem erros ou falhas frequentes. Podem ser realizados testes de estresse e de carga para verificar a estabilidade do software. |
RNF007 - Adaptabilidade | Deve ser adaptável a diferentes necessidades do usuário e permitir personalização para atender a requisitos específicos. |
RNF008 - Fácil manutenção |  O software deve ser fácil de manter e atualizar.|
RNF009 - Possibilidade de backup | Deve ser capaz de realizar backups frequentes de dados armazenados. |


## Riscos

Tabela com o mapeamento dos riscos do projeto, as possíveis soluções e os responsáveis.

Data | Risco | Prioridade | Responsável | Status | Providência/Solução |
------ | ------ | ------ | ------ | ------ | ------ |
16/03/2023 | Implementação de protótipo com as tecnologias | Alta | Todos | Vigente | Procurar por materiais de ensino abrangentes sobre a tecnologia em questão e realizar um caso simples de implementação como exercício inicial |
16/03/2023 | Falta de conhecimento das tecnologias | Alta | Todos | Vigente |Pesquisar tutoriais, assistir aulas sobre o assunto |
16/03/2023 | Distribuição inadequada de responsabilidades | Médio | Gerente | Vigente | Compreender precisamente as demandas do cliente em cada interação e ser pragmático ao estabelecer o que produzir diante do tempo disponível dos colaboradores da equipe |
16/03/2023 | Atrasos na entrega de tarefas | Alta | Todos | Vigente |  Planejar e executar as atividades com antecedência, sem deixar de dedicar um pouco do tempo de cada dia ao projeto |

### Referências
