
from sqlalchemy import Date,String,Column, Integer,Float
from sqlalchemy.ext.declarative import declarative_base
import datetime

engine = get_connection
Base = declarative_base()

class CoreEmployeeModel(Base):
    _tablename_ = "Employee"
    id = Column(Integer, primary_key=True, autoincrement= True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable =False)
    age = Column(Integer, nullable= False)
    email = Column(String(50), nullable = True, unique= True)
    hire_date = Column(Date,nullable=False, default=datetime.date.today)


# Check if the table exists, then create it if not
if not engine.dialect.has_table(engine, CoreEmployeeModel.__tablename__):
    Base.metadata.create_all(engine)
    print(f"Table '{CoreEmployeeModel.__tablename__}' has been created.")
else:
    print(f"Table '{CoreEmployeeModel.__tablename__}' already exists.")