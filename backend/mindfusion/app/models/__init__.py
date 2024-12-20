from app.database.db import Base, engine
from app.models.user import User
from app.models.tutor import Tutor
from app.models.session import Session
from app.models.review import Review

# Adicione todos os modelos à base
Base.metadata.create_all(bind=engine)