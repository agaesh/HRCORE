from connection import get_connection
from sqlalchemy import Date,String,Column, Integer,Float
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class CoreEmployeeModel(Base):
    _tablename_ = "Employee"
    id = Column(Integer, primary_key=True, autoincrement= True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable =False)
    age = Column(Integer, nullable= False)
    email = Column(String(50), nullable = True, unique= True)
    hire_date = Column(Date,nullable=False, default=datetime.date.today)

Base.metadata.create_all(get_connection)