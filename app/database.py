from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL do banco (SQLite)
DATABASE_URL = "sqlite:///./database.db"

# Engine de conexão
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  
    # necessário para SQLite
)

# Sessão do banco
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base para os models
Base = declarative_base()


# Dependency para usar nas rotas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
