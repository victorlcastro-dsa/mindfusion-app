import os
from dotenv import load_dotenv

# Especifica o caminho do arquivo .env dentro da pasta docker
dotenv_path = os.path.join(os.path.dirname(__file__), '../../../../.env')
load_dotenv(dotenv_path)

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()