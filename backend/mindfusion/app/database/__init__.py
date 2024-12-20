from app.database.db import engine, Base
from app.models import User, Tutor, Session, Review
from app import config

# Cria todas as tabelas no banco de dados
Base.metadata.create_all(bind=engine)