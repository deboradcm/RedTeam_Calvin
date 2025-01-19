from pymongo import MongoClient
import pandas as pd

def connect_to_mongo(uri, db_name, collection_name):
    client = MongoClient(uri)
    db = client[db_name]
    return db[collection_name]

def ingest_data_to_mongo(collection, dataframe):
    records = dataframe.to_dict('records')
    collection.delete_many({})  # Limpa a coleção antes de inserir novos dados
    collection.insert_many(records)
    print("Dados ingeridos no MongoDB com sucesso.")
