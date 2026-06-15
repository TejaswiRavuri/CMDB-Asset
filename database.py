import pyodbc

# Connect to MySQL
conn = pyodbc.connect(
    DRIVER="{MySQL ODBC 9.7 Unicode Driver}",
    SERVER="localhost;PORT=3306",
    USER="root",
    PASSWORD="Anirudh@2005",
    DATABASE="CMDB"
)

cursor = conn.cursor()

print("Database Connected Successfully")