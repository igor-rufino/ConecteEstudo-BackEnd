<h1 align="center"> Conecte Estudo: Plataforma Web para Auxílio no Ensino à Distância </h1>
<h3 align="center"> Projeto desenvolvido para o Trabalho de Conclusão de Curso (TCC) de alunos do 10º período de Engenharia da Computação pelo <a href="https://inatel.br/home/">INATEL</a></h3>

[Conecte Estudo](https://github.com/igor-rufino/webapp-ead) é uma aplicação web para ajudar no ensino à distância e inclui uma agenda virtual de cada usuário. Para o aluno, é possível controlar seu cronograma, ver e adicionar novas tarefas de uma forma prática. Para o professor é possível criar aulas com turmas, criar tarefas para os alunos, planos de ensino e disponibilizar material de aula. Além disso é possível controlar seu próprio cronograma com tarefas do dia a dia. 

Esse projeto contém uma <a href="https://www.redhat.com/pt-br/topics/api/what-is-a-rest-api">API REST</a>, desenvolvida usando <a href="https://www.djangoproject.com/">Django Framework</a> para conectar a aplicação web que foi desenvolvida em <a href="https://pt-br.reactjs.org/">React</a>. E como banco de dados foi utilizado o <a href="https://www.mongodb.com/">MongoDB</a>.

## Tópicos 
- [Pré Requisitos](#pré-requisitos-) 
- [Autores](#autores)
- [Passo a passo da implementação](#passo-a-passo-da-implementação-)
- [Instalação](#instalação-)
- [Coleção do Postman](#coleção-do-postman)

## Pré Requisitos 📋
- python3
- Django
- Djongo
- Djoser
- MongoDB

## Autores
* **Ana Luiza Silva Terra** - [Ana Luiza](https://github.com/analuizat3)
* **Igor Rufino Ribeiro** - [Igor](https://github.com/igor-rufino)
* **Paulo Gabriel de Freitas Rotundaro** - [Paulo](https://github.com/PauloRotundaro)
* **Pedro Abritta Reis** - [Pedro](https://github.com/pedro-toodoo)

## Passo a passo da implementação 🏃

### Implementação do Django REST Framework: 
<h5>Criando os apps:</h5>

```
django-admin startapp nameapp
```

<h5>Criar tabelas de migração do banco de dados: </h5>

```
python manage.py makemigrations
python manage.py migrate
```

<h5>Iniciar localmente o servidor: </h5>

```
python manage.py runserver
```

### Conectando ao MongoDB<a href="https://www.mongodb.com/pt-br/products/compass"> Compass </a>:

![image](https://user-images.githubusercontent.com/94690905/174868977-adb65a53-58a8-4197-bca1-47b53a62be82.png)

### Configurando as constantes locais do projeto:

<h5>É recomendável por questões de segurança criar um arquivo para armazenar algumas constantes localmente como DB_USERNAME e DB_PASSWORD e DJANGO_KEY:</h5>
<h5> Nota: Crie um arquivo constant.py com as constantes e basta colocá-lo na raiz do projeto e importar em settings.py.</h5>

![image](https://user-images.githubusercontent.com/94690905/174874165-15993c75-e0dc-4312-8aad-0e0a4524f4d3.png)

![image](https://user-images.githubusercontent.com/94690905/174873982-a17c39ae-53a5-4979-a397-4d8db816d459.png)


## Instalação 🔧
- Forma genérica: instala todas as bibliotecas usadas no projeto:
```
pip install -r requirements.txt
```
- Ou é possível também instalar cada biblioteca com sua respectiva versão separadamente:
```
pip install [lib_name]
```

## Coleção do Postman
<h5>Criamos também um arquivo (webapp-ead.postman_collection.json) das coleções no <a href="https://www.postman.com/downloads/">Postman</a> onde ficará mais fácil para testar todos os endpoints criados do projeto</h5>
<h5>Imagem de alguns endpoints com seus respectivos CRUDS:</h5>

![image](https://user-images.githubusercontent.com/94690905/174872312-3d1317a8-0b55-4a2e-a651-751d5453f426.png)

