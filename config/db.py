from pymongo import MongoClient

client = MongoClient("mongodb+srv://fastapi:fastapi@cluster0.qes5fnm.mongodb.net/?retryWrites=true&w=majority")

db = client.book_db

collection_name = db["books"]