import json
import pymongo

class mongoDatabase:
    def __init__(self) -> None:
        with open ('mondo-db-details.json', 'r') as fp:
            data = json.load(fp)

        self.connectionString = data[0]['connection-string']
        self.dataBase = data[0]['database']
        self.collection = data[0]['collection']
    
    def connect(self):
        with open ('data.json', 'r') as fp:
            self.data = json.load(fp)
        self.client = pymongo.MongoClient(self.connectionString)
        self.db = self.client[self.dataBase]
        self.collection = self.db[self.collection]
        self.collection.insert_many(self.data)

