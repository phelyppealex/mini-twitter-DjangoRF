# Mini Twitter API

## Description

This is a project that implements an API using Django and Django Rest Framework as development tools. The intention was to develop an API that resembled in some aspects what Twitter is currently.

## How to run the application

### Required applications

- Docker
- Python >= 3
- Git

### Run these commands in a terminal

```Let's download the project from github```

~~~
git clone https://github.com/phelyppealex/mini-twitter-DjangoRF.git
cd mini-twitter-DjangoRF
~~~

```Let's activate the virtual environment```

- #### For Linux/MacOS

~~~
source ./venv/bin/activate
~~~

- #### For Windows

~~~
.\venv\bin\activate
~~~

```Set upping the database```

~~~
docker compose up -d
~~~

```Running the project```

- #### For Linux/MacOS

~~~
python3 manage.py runserver
~~~

- #### For Windows

~~~
python manage.py runserver
~~~

## Useful links

- [API documentation](https://documenter.getpostman.com/view/39288021/2sAY4skQm5)

- [Entity-Relationship Diagram](https://www.canva.com/design/DAGUPFcmU2o/r1ZTncVUJxqszoq11I8Ztw/edit?utm_content=DAGUPFcmU2o&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)