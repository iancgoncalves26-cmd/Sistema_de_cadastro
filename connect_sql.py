from sqlalchemy import create_engine,Column,Integer,String
import os
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base,sessionmaker


load_dotenv()

user_sql = os.getenv('DATABASE_URL')

conexao = create_engine(f'{user_sql}')

Base = declarative_base()

class User(Base):
    __tablename__ = 'cadastros'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    email = Column(String(50), nullable=False , unique=True)

Session = sessionmaker(bind=conexao)


