from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_puppy_setup import Base, Puppy, Shelter
from sqlalchemy import desc
import datetime as dt
from get_connection_string import get_connection_string


class TableHandler:

    def __init__(self, con_string):
        engine = create_engine(con_string)
        Base.metadata.create_all(engine)
        DBSession = sessionmaker(bind=engine)

        self.session = DBSession()
        self.table_def = Puppy

    def get_row_names(self):
        return [row.name for row in self.session.query(self.table_def).all()]
