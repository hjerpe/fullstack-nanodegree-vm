import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()


class Shelter(Base):
	__tablename__ = 'shelter'
	name = Column(String(80), nullable=False)
	address = Column(String(80), nullable=False)
	city = Column(String(80), nullable=False)
	state = Column(String(80), nullable=False)
	zipCode = Column(String(5), nullable=False)
	website = Column(String(80), nullable=True)
	id = Column(Integer, primary_key=True)


class Puppy(Base):
	__tablename__ = 'puppy'
	
	name = Column(String(80), nullable=False)
	dateOfBirth = Column(Date, nullable=True)
	gender = Column(String(6), nullable=False)
	weight = Column(Integer, nullable=False)
	shelter_id = Column(Integer, ForeignKey('shelter.id'))
	id = Column(Integer, primary_key=True)

	shelter = relationship(Shelter)


if __name__ == '__main__':
    engine = create_engine('sqlite:///puppyshelter.db')
    Base.metadata.create_all(engine)
