from sqlalchemy import create_engine

def get_connection():
    connection_string = (
       "mssql+pyodbc://sa:mcl%401234@LAPTOP-0QQ7OVBA\\SQLEXPRESS01/HRCORE"
       "?driver=SQL+Server"
    )
    engine = create_engine(connection_string)
    return engine
