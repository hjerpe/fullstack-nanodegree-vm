from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_puppy_setup import Base, Puppy, Shelter
from sqlalchemy import desc
import datetime as dt
from get_connection_string import get_connection_string

engine = create_engine(get_connection_string())
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
table_deb = Puppy

def arr_table_names():
    table_names = map(lambda row: row.name, session.query(Puppy).all())
    return table_names
