# Projeto Arquitetural - SIGDESPENSA 

Neste documento mostraremos o projeto arquitetural do sistema com uma breve descrição de cada componente utilizado.

## Diagrama 

```mermaid
    stateDiagram-v2
    direction LR
    CLIENT --> WEB.SERVER
    WEB.SERVER --> CLIENT
    WEB.SERVER --> WSGI
    WSGI --> WEB.SERVER
    WSGI -->  REQUEST
    REQUEST --> URL.RESOLUTION
    URL.RESOLUTION --> VIEW1
    VIEW1 --> VIEW2
    VIEW2 --> TEMPLATE1
    VIEW2 --> RESPONSE
    TEMPLATE1 --> TEMPLATE2
    TEMPLATE2 --> RESPONSE
    RESPONSE --> WSGI
    VIEW2 --> MODEL
    MODEL --> MANAGERS
    MANAGERS --> MODEL
    MANAGERS --> DATABASE
    DATABASE --> MANAGERS
    VIEW2 --> EXCEPTION
    EXCEPTION --> RESPONSE



    state CLIENT {
        Browser 
    }
    state WEB.SERVER {
         (Nginx/Apache)
    }
    state WSGI {
         wsgi.py
         direction LR
         (Gunicorn/uWSGI)
        
    }
    state REQUEST {
         Middleware1
    }
    state URL.RESOLUTION {
         urls.py
    }
    state VIEW1 {
         Middleware2
    }
    state VIEW2 {
         views.py
    }
    state TEMPLATE1 {
         Middleware3
    }
    state TEMPLATE2 {
         exemple.html
    }
    state RESPONSE {
         Middleware4
    }
    state MODEL {
        models.py
    }
    state EXCEPTION {
        Middleware5
    }
   
```

## Descrição

| Componente | Tecnologia | Descrição
|------------|------------|----------
|View|ReactJS| Criação de componentes visuais para a tela
|Service|Axios| Comunicação via HTTP com a API
|Controller| Express| Servidor para receber as requisições HTTP
|Repository| PrismaJS| ORM para fazer comunicação com o banco de dados
|Database|PostgreSQL| Banco de dados para guardar as informações salvas
