# 📦 API de Gerenciamento de Estoque

API REST simples para gerenciamento de estoque, desenvolvida em Python com persistência de dados utilizando SQLite3.

---

## 🚀 Funcionalidades

A API permite realizar operações completas de CRUD em produtos:

* ✅ Cadastrar um produto
* 📋 Listar todos os produtos
* 🔍 Buscar um produto pelo ID
* ✏️ Atualizar um produto completamente (PUT)
* 🧩 Atualizar parcialmente um produto (PATCH)
* ❌ Deletar um produto pelo ID

---

## ⚡ Funcionalidades Extras

### 🕒 Data e hora automáticas

Ao cadastrar um produto, a data e o horário são gerados automaticamente.

### 🛡️ Validação de dados

* ❌ Preço não pode ser negativo
* ❌ Quantidade não pode ser negativa
* ❌ Campos obrigatórios não podem estar vazios

Essas validações evitam inconsistências no banco de dados e tornam a API mais robusta.

---

## 🗄️ Banco de Dados

O projeto utiliza SQLite3 com os seguintes objetivos:

* Persistência local dos dados (não são perdidos ao encerrar a API)
* Simplicidade de configuração (não requer servidor de banco de dados)

---

## 🔧 Atualização dinâmica (PATCH)

Foi implementado um sistema de atualização dinâmica que permite:

* Atualizar apenas os campos enviados no JSON
* Preservar os demais dados já existentes no banco

---

## ⚙️ Como executar o projeto

### 1. Instalar as dependências

```id="x1p9k2"
pip install -r requirements.txt
```

### 2. Iniciar o servidor

```id="l0s8qd"
flask run
```

Caso não funcione:

```id="r7m2zc"
python routes_estoque.py
```

No Linux:

```id="t4v8ne"
python3 routes_estoque.py
```

---

## 🧪 Testando a API

Você pode testar os endpoints utilizando ferramentas como:

* Postman
* Insomnia

### 📌 Fluxo básico de uso:

1. Inicie o servidor
2. Abra o Postman ou Insomnia
3. Realize requisições para os endpoints (GET, POST, PUT, PATCH, DELETE)

---

## 📁 Estrutura do JSON

Exemplo de produto:

```json id="p9w3kx"
{
  "nome": "Produto A",
  "preco": 100.0,
  "quantidade": 10
}
```

⚠️ **Observação:**
A data e hora não precisam ser enviadas, pois são geradas automaticamente pela API.

---

## 🧠 Observações importantes

* O método **PUT** atualiza todos os campos do produto
* O método **PATCH** atualiza apenas os campos enviados
* O banco SQLite é armazenado localmente no projeto
* A API possui validações básicas para garantir integridade dos dados

---

## 🛠️ Tecnologias utilizadas

* Flask (framework web em Python)
* SQLite3 (banco de dados)
* Datetime (manipulação de data e hora)

---
