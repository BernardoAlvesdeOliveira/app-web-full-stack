## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

# Aplicação web full stack com Flask e MariaDB

Este projeto é uma aplicação web full stack que utiliza Flask no backend com um banco de dados MariaDB e um frontend estático em HTML, CSS e JavaScript. O backend expõe uma API RESTful que é consumida pelo frontend para interagir com os dados do banco de dados.

## Descrição

A aplicação foi criada para demonstrar a construção de um servidor backend com Flask, conexão a um banco de dados MariaDB e integração com um frontend estático. A comunicação entre o frontend e o backend é feita por meio de uma API, que pode ser acessada pelo navegador ou outras aplicações cliente.

## Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Banco de Dados**: MariaDB
- **Frontend**: HTML, CSS, JavaScript
- **Servidor Local**: Para rodar o frontend localmente e consumir a API


## Como Rodar o Projeto Localmente

### 1. Clonar o Repositório

```bash
git clone https://github.com/BernardoAlvesdeOliveira/app-web-full-stack.git
cd app-web-full-stack
```

### 2. Instalar as Dependências do Backend

Primeiro, instale as dependências do Python:

```bash
pip install -r backend/requirements.txt
```

### 3. Configurar o Banco de Dados MariaDB

1. Certifique-se de ter o MariaDB instalado e em execução.
2. Crie um banco de dados e uma tabale com as seguintes colunas para a aplicação.
3. Importe o script de inicialização do banco de dados:

```bash
mysql -u root -p < database/init.sql
```

### 4. Rodar o Servidor Backend (API Flask)

Para rodar o servidor Flask localmente, execute o seguinte comando na pasta `backend/`:

```bash
python backend/app.py
```

O servidor será iniciado na porta `5001` por padrão.

### 5. Rodar o Frontend Localmente

Para rodar o frontend localmente, você pode usar um servidor estático simples. Um exemplo usando o `http-server` (Node.js) seria:

1. Instale o `http-server` globalmente:

```bash
npm install -g http-server
```

2. Navegue até a pasta `frontend/` e inicie o servidor:

```bash
cd frontend
http-server
```

O servidor será iniciado na porta `8000` por padrão.

### 6. Testar a Aplicação

Agora, você pode acessar o frontend em `http://localhost:8000` e testar a integração com o backend rodando em `http://localhost:5001`.

## Funcionalidades

- **API RESTful**: O backend fornece endpoints para interagir com o banco de dados.
- **Frontend**: O frontend consome a API para exibir e manipular os dados.
