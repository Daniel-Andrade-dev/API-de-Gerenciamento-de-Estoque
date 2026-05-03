📦 API de Gerenciamento de Estoque

Uma API REST simples para gerenciamento de estoque, desenvolvida em Python com persistência de dados utilizando SQLite3.


🚀 Funcionalidades

A API permite realizar operações completas de CRUD em produtos:

✅ Cadastrar um produto

📋 Listar todos os produtos

🔍 Buscar um produto pelo ID

✏️ Atualizar um produto completamente (PUT)

🧩 Atualizar parcialmente um produto (PATCH)

❌ Deletar um produto pelo ID

⚡ Funcionalidades Extras

Além do CRUD básico, a API possui validações e automações importantes:

🕒 Data e hora automáticas
Ao cadastrar um produto, a data e o horário são gerados automaticamente.


🛡️ Validação de dados
Preço não pode ser negativo
Quantidade não pode ser negativa
Campos obrigatórios não podem estar vazios

Essas validações evitam inconsistência no banco e tornam a API mais robusta.

🗄️ Banco de Dados

O projeto utiliza SQLite3, com os seguintes objetivos:

Persistir os dados localmente (os dados não são perdidos ao encerrar a API)

Simplicidade de configuração (não precisa instalar servidor de banco)


🔧 Atualização dinâmica (PATCH)

Foi implementado um sistema de update dinâmico, permitindo que o método PATCH:

Atualize apenas os campos enviados no JSON
Preserve os demais dados no banco

⚙️ Como executar o projeto

1. Instalar as dependências
pip install -r requirements.txt


2. Iniciar o servidor

Primeiro tente com -> flask run

Caso não funcione use:

-> python routes_estoque.py

Case estiver no Linux:

-> python3 routes_estoque.py


🧪 Testando a API

Você pode testar os endpoints utilizando ferramentas como:

Postman

Insomnia


📌 Exemplo de fluxo:

Inicie o servidor

Abra o Postman


Faça requisições para os endpoints 
(GET, POST, PUT, PATCH, DELETE)

📁 Estrutura do JSON

Exemplo de produto:

{
  "nome": "Produto A",
  "preco": 100.0,
  "quantidade": 10
}

⚠️ A data e hora não precisam ser enviadas, pois são geradas automaticamente pela API.

🧠 Observações importantes

O método PUT atualiza todos os campos do produto

O método PATCH atualiza apenas os campos enviados

O banco SQLite é armazenado localmente no projeto

A API possui validação básica para garantir integridade dos dados


🖥️ Tecnologias ultilizadas

Flask MicroFramework do Python

SQLite3


Biblioteca datetime do Python
