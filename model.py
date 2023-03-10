from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import  Column, Integer, String

from fastapi import FastAPI

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# создаем модель, объекты которой будут храниться в бд
Base = declarative_base()
class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer,)

# создаем таблицы
Base.metadata.create_all(bind=engine)

# создаем сессию подключения к бд
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

# создаем объект Person для добавления в бд
Rik = Person(name="Rik", age=38)
db.add(Rik)
db.refresh(Rik)# добавляем в бд
db.commit()     # сохраняем изменения

print(Rik.id)   # можно получить установленный id

# приложение, которое ничего не делает
app = FastAPI()
