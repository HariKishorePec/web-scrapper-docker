from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import config

# Define database connection string
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://{user}:{password}@{host}/{database}"
# Create SQLAlchemy engine and sessionmaker
engine = create_engine(
    SQLALCHEMY_DATABASE_URL.format(
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        host=config.DB_HOST,
        database=config.DB_NAME
    )
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define Base class for declarative models
Base = declarative_base()
