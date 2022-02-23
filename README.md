<p align="center">
  <img src="./images/crud.png" width="360" >
</p>

## 📋 Índice

- [Sobre](#-Sobre)
- [Tecnologias utilizadas](#-Tecnologias-utilizadas)
- [Como executar o projeto](#-Como-executar-o-projeto)
- [Preview](#-Preview)

---

## 🖥 Preview 

<p align="center">
  <img src="./images/swagger.png" width="700" >
  <img src="./images/create.png" width="700" >
  <img src="./images/dbeaver.png" width="700" >
</p>

---

## 📖 Sobre 

A proposta do desafio é uma aplicação simples que possa:
- Cadastrar novas pessoas 
- Editar um cadastro, 
- Apagar um cadastro, 
- Listar o cadastro pelo ID 
- Listar todos os cadastrados

--- 

## 🚀 Tecnologias utilizadas

O projeto está desenvolvido utilizando as seguintes tecnologias:

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL

--- 

### Configuração do projeto

```sh
# clone o repositório
git clone git@github.com:JoshuelNobre/lapisco-challenge.git

# entre no diretório
cd lapisco-challenge
```

### Ambiente virtual

- Crie um ambiente virtual de sua prefência, no meu caso utilizei virtualenv.

```shell
# criando ambiente virtual
virtualenv venv

# ative o ambiente virtual, no Windows ativo da seguinte forma
.\venv\Scripts\activate.ps1
```

### Executando o projeto

```shell
# instale todas as dependências com
pip install -r requirements.txt

# execute usando o comando
uvicorn src.main:app
```

Feito isso, abra o seu navegador e acesse `http://localhost:8000/docs`

---


Desenvolvido por Joshuel Nobre 🚀