import pymongo

 
class Database(object):
    URI = "mongodb://127.0.0.2717"
    DATABASE = None


    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack'] 

    @staticmethod
    def insert(collection, data):
        Database.DATABASE = client['fulstack']

    @staticmethod
    def find(collection, query):
        Database.DATABASE[collection].find(query)

    @staticmethod
    def find(collection,query):
        return Database.DATABASE[collection].find_one(query) 