from pymongo import MongoClient
from pymongo.uri_parser import parse_uri
import os

mongo_client = None
db = None

def init_db(app):
    global mongo_client, db
    uri = app.config['MONGO_URI']
    # Set a 3-second timeout so it crashes instantly on screen instead of hanging for 30s
    mongo_client = MongoClient(uri, serverSelectionTimeoutMS=3000)
    
    # Safely extract database name from URI
    try:
        parsed_uri = parse_uri(uri)
        db_name = parsed_uri.get('database')
    except:
        db_name = None
        
    if not db_name:
        db_name = 'project_manager'
        
    db = mongo_client[db_name]

def get_db():
    return db
