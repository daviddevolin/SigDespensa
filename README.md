# SigDespensa
### SigDespensa is a project for Software Engineering II taught by Taciano de Morais

## Sobre
SigDespensa trata-se de um aplicativo em desenvolvimento onde será possivel realizar o gerenciamento de pequenas despensas. Seu back-end será realizado por meio da linguagem Python (Django) e seu front-end JavaScript (React).


## Tutoriais de Ensino

Inventory - Tutorial em inglês

* [Inventory Tutorial-Playlist](https://www.youtube.com/watch?v=RE72oSx5ivI&list=PLo7TNe_pEoMXb9GyzueM7516fOR0gPxNX)

Connect React JS Frontend with Django Backend

* [Connect React JS with Django](https://www.youtube.com/watch?v=tiungJDoQyA)

Django 4 CRUD completo
* [Django 4 CRUD completo em ~30 minutos](https://www.youtube.com/watch?v=GGBzMpIAgz4) 

### Para implantar o projeto no Docker:

bash:
```
docker build -t sig-despensa .
```

### Para iniciar o servidor, execute o seguinte comando no terminal:

bash:
```
docker-compose up
```

# Instalando o sistema
É necessário ter alguma versão do python instalada no seu sistema. De preferência python >= 3.10

### Para criar um ambiente virtual
```
python -m venv <nome do ambiente virtual>
```

### Para iniciar o ambiente virtual

bash:
```
$ source <venv>/bin/activate
```
cmd:
```
C:\> <venv>\Scripts\activate.bat
```

### Para instalar os requisitos

```
pip install -r requirements.txt
```

### Para inicializar o servidor Django
```
python manage.py runserver
```
