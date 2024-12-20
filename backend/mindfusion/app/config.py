import os
from dotenv import load_dotenv

# Especifica o caminho do arquivo .env dentro da pasta docker
dotenv_path = os.path.join(os.path.dirname(__file__), '../../../.env')
load_dotenv(dotenv_path)

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    DEBUG = os.getenv("DEBUG", False)

config = Config()