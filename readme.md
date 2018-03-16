# django-boilerplate-crud

Projeto do django apresentando as 2 formas mais comuns de se implementar um CRUD em Django.

    - Class Based View
    - Function Based View

### Instalação

Clone o projeto, crie o ambiente virtual e faça a instalação das dependências.
É necessário ter `python 3.5+` e `virtualenv`.  

```sh
$ git clone https://github.com/lucheol/django-boilerplate-crud
$ cd django-boilerplate-crud
$ virtualenv env
$ env/bin/pip install -r requeriments.txt
```

Faça o migrate, crie o superuser e execute o projeto.

```sh
$ env/bin/python manage.py makemigrations
$ env/bin/python manage.py migrate
$ env/bin/python manage.py createsuperuser
$ env/bin/python manage.py runserver
```

