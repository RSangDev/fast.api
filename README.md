# 🐍 FastAPI User API
Este é o meu primeiro projeto utilizando FastAPI! 

Construi uma API RESTful simples para gerenciamento de usuários, com CRUD completo, validação de dados e testes. O objetivo deste projeto é praticar, além de criar um portfólio funcional que demonstre boas práticas de desenvolvimento de APIs modernas em Python.

Se trata de um sistema para gerenciamento de usuários, construída com FastAPI, SQLAlchemy e SQLite, com testes automatizados usando pytest.

Esta API permite criar, ler, atualizar e deletar usuários, seguindo boas práticas de arquitetura em camadas e separação de responsabilidades.

## Funcionalidades

* Criar usuários (POST /users)

* Listar todos os usuários (GET /users)

* Buscar usuário por ID (GET /users/{id})

* Atualizar usuário (PUT /users/{id})

* Deletar usuário (DELETE /users/{id})

* Testes automatizados com banco de dados em memória

* Documentação automática da API (/docs e /redoc)

## Arquitetura

O projeto segue arquitetura em camadas:

| Camada    |  Arquivo(s)  |  Responsabilidade |
|-----------|--------------|------------------|
| API / Rotas | main.py     | Recebe requisições e retorna respostas |
| Validação  | schemas.py  | Valida entrada/saída de dados |
| Banco      | models.py   | Define tabelas do banco de dados |
| Lógica CRUD| crud.py     | Lida com criação, leitura, atualização e deleção de dados |
| Conexão DB | database.py | Cria e gerencia a conexão com o banco |
| Testes     | tests/      | Testes unitários e integração usando pytest |


## Tecnologias usadas

* Python 3.11+
* FastAPI
* SQLAlchemy
* Pydantic
* SQLite
* pytest
* Uvicorn

## Instalação

Clone o repositório:
```bash
git clone https://github.com/seu-usuario/fastapi-user-api.git
cd fastapi-user-api
```

Crie e ative um ambiente virtual:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```


Instale as dependências:
```bash

pip install -r requirements.txt
```

## Executando a API

Inicie o servidor:
```bash

uvicorn app.main:app --reload
```


Acesse a documentação automática:

Swagger UI: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc

## 🧪 Testes

Os testes usam um banco SQLite em memória para não interferir no banco real.

Para rodar os testes:

```bash
pytest
```
📝 Exemplos de requisições
Criar usuário
```bash

POST /users
Content-Type: application/json

{
  "name": "João",
  "email": "joao@email.com"
}
```

Atualizar usuário
```bash

PUT /users/1
Content-Type: application/json

{
  "name": "João Atualizado"
}
```

Deletar usuário
```bash

DELETE /users/1
```

## Estrutura do projeto
```bash

app/
├── main.py          # Rotas da API
├── models.py        # Modelos do banco de dados
├── schemas.py       # Pydantic schemas para validação
├── crud.py          # Funções CRUD
├── database.py      # Conexão com o banco
tests/
├── __init__.py
├── conftest.py      # Fixtures para testes
└── test_users.py    # Testes da API
requirements.txt
README.md
```

## Observações

- O projeto utiliza SQLAlchemy com SQLite, mas pode ser facilmente adaptado para PostgreSQL ou outro banco.

- Segue FastAPI + Pydantic v2, portanto algumas configurações antigas (Config/orm_mode) foram adaptadas.

- Testes funcionam isoladamente e criam tabelas automaticamente antes da execução.
