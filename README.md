# Azure Cosmos DB Python Script
Este repositório contém um script em Python para interagir com o Azure Cosmos DB. Ele permite criar um banco de dados, um container e realizar operações CRUD (Create, Read, Update, Delete) em itens dentro do container.

# Instalação

1. **Clone este repositório:**
     ```bash 
     git clone https://github.com/IarleySouza/Gerenciamento-CosmosDB.git
   ```
2. **Instale as dependências necessárias:**
    ```bash 
     pip install azure-cosmos python-dotenv
   ```

# Configuração
Crie um arquivo .env na raiz do projeto e adicione suas credenciais do Azure Cosmos DB:
    
```bash 
COSMOS_URL=SEU_COSMOS_URL
COSMOS_KEY=SEU_COSMOS_KEY
COSMOS_DATABASE_NAME=SEU_DATABASE_NAME
COSMOS_CONTAINER_NAME=SEU_CONTAINER_NAME
   ```

# Uso
Execute o script para criar o banco de dados e o container automaticamente:
```bash 
python script.py
   ```