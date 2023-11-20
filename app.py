import pyodbc

# Dane do polaczenia z baza danych
server = '20.215.221.18,1433'  # Adres serwera i portu SQL Servera w kontenerze
database = 'master'  # Nazwa bazy danych
username = 'sa'  # Nazwa uzytkownika (domyslnie 'sa' dla SQL Servera)
password = 'myPassword1.'  # Haslo uzytkownika
print("bbbb")
# Tworzenie ciagu polaczenia
connection_string = 'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={};DATABASE={};UID={};PWD={}'.format(server, database, username, password)

print("Trying to connect to database.")
# Proba nawiazania polaczenia z baza danych
try:
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # Wykonaj dowolne zapytanie SQL
    cursor.execute("SELECT @@VERSION AS SQL_Version")
    row = cursor.fetchone()
    print('Connected to SQL Server. Server version: {}'.format(row.SQL_Version))

except pyodbc.Error as e:
    print('Error connecting to SQL Server: {}'.format(e))

finally:
    # Zamknij polaczenie
    if 'connection' in locals():
        connection.close()
