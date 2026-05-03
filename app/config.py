import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/project_manager')
