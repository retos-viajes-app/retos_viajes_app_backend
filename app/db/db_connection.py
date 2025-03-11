from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import get_settings
# URL de conexión a la base de datos
SQLALCHEMY_DATABASE_URL = get_settings().database_url

# Creación del motor de conexión
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creación de la fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para los modelos
Base = declarative_base()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
