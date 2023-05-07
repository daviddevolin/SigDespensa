## Documento de Modelos

Neste documento temos o modelo Conceitual (UML) ou de Dados (Entidade-Relacionamento). Temos também a descrição das entidades.

## Descrição das Entidades 

| Entidade      | Descrição                                               |
|---------------|---------------------------------------------------------|
| Usuario       | Entidade  que representa o usuario do sistema           |
| Despensa      | Entidade  que respresenta a despensa, o local onde serão armazenados os itens                              |
| Categoria     | Entidade  que respresenta uma categoria que será atribuida a um item                |
| Item          | Entidade  que respresenta um item, um produto                               |
| Histórico     | Entidade  que respresenta   o relatório da despensa, a movimentação dos itens                          |

## Modelo de Dados (Entidade-Relacionamento)

```mermaid
 erDiagram
    Usuario }|--||Despensa_Usuario : has
    Despensa }|--|| Despensa_Usuario : has
    Despensa ||--|{ Categoria : has
    Despensa ||--o{Historico : has
    Categoria ||--o{ Item : has
```


## Modelo Conceitual

```mermaid
classDiagram
    class Usuario{
        -int id
        -string nome
        -string email
        -string senha
        -string cpf
        -string telefone
        
        +updateUser(id) Usuario
        +searchUser(id) Usuario
        +insertUser(Usuario usuario) void
        +deleteUser(id) Usuario
    }
    class Despensa{
        -int id
        -int quantTotal
        -int capacidade
        -Categoria categoria

        +updateDespensa(id) Despensa
        +searchDespensa(id) Despensa
        +insertDespensa(Despensa despensa) void
        +deleteDespensa(id) Despensa
    }
    class Categoria{
        -int id
        -string nome

        +updateCategoria(id) Categoria
        +searchCategoria(id) Categoria
        +insertCategoria(Categoria categoria) void
        +deleteCategoria(id) Categoria
    }

    class Item{
        -int id
        -string nome
        -Categoria categoria
        -string marca
        -float peso
        -date data_de_validade

        +updateItem(id) Item
        +searchItem(id) Item
        +insertItem(Item item) void
        +deleteItem(id) Item
    }


```