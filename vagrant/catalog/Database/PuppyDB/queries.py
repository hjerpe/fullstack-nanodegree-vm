from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Puppy, Shelter
from sqlalchemy import desc
import datetime as dt

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Read employees
# puppies = session.query(Puppy).order_by(desc(Puppy.name)).all()
puppies = session.query(Puppy).order_by(Puppy.name).all()
for pup in puppies:
    print pup.name

# Query all of the puppies that are less than 6 months old organized by the youngest first
def timeDelta():
    time_diff = dt.date.today() - dt.timedelta(days=180)
    return time_diff

puppies = session.query(Puppy).\
	filter(Puppy.dateOfBirth > timeDelta()).all()
for pup in puppies:
    print pup.name
    print pup.dateOfBirth
    print pup.shelter_id

# Query all puppies grouped by the shelter in which they are staying
print('\nGroup by shelter_id')
puppies = session.query(Puppy).filter(Puppy.shelter_id != None).\
    order_by(Puppy.shelter_id).all()
for pup in puppies:
    print pup.name
    print pup.shelter_id
