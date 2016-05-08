from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from employee_db_setup import Base, Employee, Address

engine = create_engine('sqlite:///employeeData.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create employee
employee = Employee(name='John Andersson')
session.add(employee)
session.commit()

# Read employees
employees = session.query(Employee).all()
for employee in employees:
    print employee.name


mark = session.query(Employee).filter_by(name='John Andersson').first()
session.delete(mark)
session.commit()

# Read employees
employees = session.query(Employee).all()
print('Print Employee table after deletion')
for employee in employees:
    print employee.name
