from azure.cosmos import CosmosClient, PartitionKey
from dotenv import load_dotenv
from azure.cosmos.exceptions import CosmosResourceExistsError
import os
load_dotenv()

URL = os.getenv("COSMOS_URL")
KEY = os.getenv("COSMOS_KEY")
DATABASE_NAME = os.getenv("COSMOS_DATABASE_NAME")
CONTAINER_NAME = os.getenv("COSMOS_CONTAINER_NAME")

client = CosmosClient(URL, KEY)

#Criar um banco de dados 
def create_database():
    try:
        database = client.create_database(DATABASE_NAME)
        print(f" O banco de dados '{database.id}' foi criado com sucesso")
    except CosmosResourceExistsError:
        database = client.get_database_client(DATABASE_NAME)
        print(f"Banco de dados '{DATABASE_NAME}' já existe")
        
    return database

#Criar um container
def create_container(database):
    try:
        container = database.create_container(id=CONTAINER_NAME, partition_key=PartitionKey(path="/ProductID"))
        print(f" O container '{container.id}' foi criado com sucesso")
        
    except CosmosResourceExistsError:
        container = database.get_container_client(CONTAINER_NAME)
        print(f"O container '{CONTAINER_NAME}' já existe")
        
    return container


#Criar item no container
def create_item(container, item):
    container.create_item(item)
    print("Item criado com sucesso")


def update_item(container):
    item = container.read_item(item="2", partition_key="1")
    item["ProductDescription"] = "Filme de fantasia 2"
    container.upsert_item(body=item)
    print("Item atualizado com sucesso")

def delete_item(container):
    container.delete_item(item="3", partition_key="1")
    print("Item deletado com sucesso")

def read_item(container):
    items = container.read_all_items()
    for item in items:
        print(item)
        
def read_item_by_id(container):
    item = container.read_item(item="3", partition_key="1")
    print(item)

if __name__ == "__main__":
    database = create_database()
    container = create_container(database)
    
    

item = {
        "id": "2",
        "ProductID": "1",
        "ProductName": "Testando banco",
        "ProductDescription": "Filme de terror",
        "ProductPrice": 10
    }
create_item(container, item)
#update_item(container)
#delete_item(container)

#read_item(container)
#read_item_by_id(container)