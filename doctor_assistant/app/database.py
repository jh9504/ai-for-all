from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/myweb?charset=utf8"
SQLALCHEMY_DATABASE_URL = "postgresql://db명:비번@localhost/docker명"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully")


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    api_key = Column(String(30))
    request_count = Column(Integer, default=0)
    created_at = Column(DateTime)
    last_used_at = Column(DateTime)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
