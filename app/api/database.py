from os import getenv
from dotenv import load_dotenv
from urllib.parse import quote
from sqlalchemy.orm import sessionmaker as SectionFactory
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


load_dotenv()
database_user = getenv('POSTGRES_USER')
database_password = getenv('POSTGRES_PASSWORD')
database_host = getenv('POSTGRES_HOST')
database_port = getenv('POSTGRES_PORT')
database_name = getenv('POSTGRES_DB')

DATABASE_URL = f'postgresql+psycopg2://{database_user}:{
    quote(database_password)}@{database_host}:{database_port}/{database_name}'
engine = create_engine(DATABASE_URL)
SessionClass = SectionFactory(autoflush=False, autocommit=False, bind=engine)
Session = SessionClass()
Base = declarative_base()
