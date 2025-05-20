import pyodbc

def get_connection():
    try:
        conn = pyodbc.connect(
            r"DRIVER={SQL SERVER};"
            r"SERVER=LAPTOP-0QQ7OVBA\SQLEXPRESS01;"
            r"DATABASE=HRCORE;"
            r"UID=sa;"
            r"PWD=mcl@1234"
        )
        return conn
    except Exception as e:
        print(e)

