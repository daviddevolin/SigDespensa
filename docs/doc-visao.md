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
RF001 - Inserir Usuário     | Um usuário representa um usuário autorizado para adicionar, remover e editar itens da despensa. Um Usuário tem: código-ID, nome, email,  CPF, senha e telefone. | Usuário |
RF002 - Alterar Usuário | Edita as informações de um determinado Usuário. Alterar um usuário tem: nome, email,  CPF, senha e telefone. | Usuário |
RF003 - Pesquisar Usuário | Pesquisa informações de um determinado usuário. Pesquisar usuário tem: código-ID | Usuário
RF003 - Excluir Usuário | Remove permanentemente o cadastro do Usuário. Excluir Usuário tem: código-ID, email, CPF e senha. | Usuário|
RF004 - Fazer Login | Realiza o login do usuário com as informações passadas: email e senha | Usuário |
RF005 - Controle de permissões de usuários no sistema | O sistema deverá conceder permissões de administrador para usuários que criarem uma despensa e para usuários selecionados pelo administrador. | Usuário |
RF006 - Inserir Despensa | A Despensa é onde estará o estoque de produtos. Uma Despensa tem: código-ID, quantidadeTotal, capacidade, e categoria. | Usuário |
RF007 - Alterar Despensa | Edita as informações de uma determinada Despensa. Alterar uma despensa tem: quantidadeTotal, capacidade, e categoria | Usuário |
RF008 - Pesquisar Despensa | Pesquisa informações sobre uma despensa. Pesquisar despensa tem: código-ID. | Usuário |
RF009 - Excluir Despensa | Remove permanentemente o cadastro de uma despensa. Excluir despensa tem: código-ID | Usuário |
RF010 - Inserir Categoria |  Categoria estabelece que tipo de item pode ser armazenado em determinado depósito. Uma Categoria tem: código-ID e nome. | Usuário |
RF011 - Alterar Categoria | Edita informações de uma categoria. Editar categoria tem: código-ID, nome | Usuário |
RF012 - Pesquisar Categoria | Pesquisa informações de uma categoria. Pesquisar categoria tem: nome | Usuário |
RF013 - Excluir Categoria | Remove permanentemente o cadastro de uma categoria. Excluir categoria tem: código-ID | Usuário |
RF014 - Cadastro do Histórico  | Um Histórico irá constar, todo o acesso e movimentação feita por cada usuário ao despensa. Um Histórico tem: codigo-ID, e horários, data e ID-usuário.  | Usuário |
RF015 - Inserir Item | Um Item representa um produto ou objeto que pode ser armazenado e gerenciado no sistema. Um Item tem: código-ID, nome, categoria, marca, peso e data de validade | Usuário |
RF016 - Alterar Item | Altera as informações de um determinado item. Alterar um Item tem: código-ID, nome, categoria, marca, peso e data de validade | Usuário |
RF017 - Pesquisar Item | Pesquisa informações de um item. Pesquisar item tem: código-ID, nome | Usuário |
RF018 - Excluir Item | Remove permanentemente um Item da despensa. Excluir um Item tem: código-ID, nome, categoria, marca, peso e data de validade | Usuário |
RF019 - Relatório de entrada de itens na despensa | Registra o cadastro de novos itens na despensa. Relatório de entrada tem: código-ID, item, quantidade, data, código-ID-usuário | Usuário |
RF020 - Relatório de saída de itens da despensa | Registra a retirada ou exclusão de itens da despensa. Relatório de saída tem: código-ID, item, quantidade, data, código-ID-usuário | Usuário |
RF021 - Filtrar Item Por Nome | Filtra itens da despensa baseado no nome, em ordem crescente ou decrescente. Filtrar item por nome tem: nome | Usuário |
RF022 - Filtrar Item Por Data | Filtra itens da despensa baseado na data adicionada, em ordem crescente ou decrescente. Filtrar item por data tem: data | Usuário |
RF023 - Adição de notas pessoais | Adiciona notas pessoais para itens na despensa. Adição de notas pessoais tem: descrição, data | Usuário |
RF024 - Monitorar níveis de Despensa | Monitora os níveis do estoque de um determinado produto dentro da despensa. Monitorar níveis de Despensa tem: código-ID, porcentagem | Usuário |



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
