import pyodbc

### ---- Connect to cloud Database ----- ###
# initialize db and connect to database
def connect_to_database():
    # connect to database
    db_name = "book.db"
    # Connection details
    server = 'ids706server.database.windows.net'
    port = 1433
    user = 'azureuser'
    password = 'Lilinke@#918918'
    database = 'IDS706Database'

    # Build connection string
    conn_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server},{port};DATABASE={database};UID={user};PWD={password}"

    # Try to establish a connection
    try:
        with pyodbc.connect(conn_string) as connection:
            print("Connected!")
    except Exception as e:
        print("Failed to connect to the database:", str(e))
    return connection


# create a cursor: a cursor is a database object used to traverse
def create_cursor(connection):
    cursor = connection.cursor()
    return cursor


### ---- CRUD ----- ###
# create a table
def create_table(connection, cursor, query_creation):
    cursor.execute(query_creation)
    connection.commit()


# insert data to the table
def insert_data(cursor, connection, sql_insertion, i1, i2, i3):
    cursor.execute(
        sql_insertion,
        (
            i1,
            i2,
            i3,
        ),
    )
    connection.commit()


# read data from table
def read_data(cursor, sql_read, input_read):
    cursor.execute(sql_read, (input_read,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)


# update data from table
def update_data(cursor, connection, query_update, stock, name):
    cursor.execute(
        query_update,
        (
            stock,
            name,
        ),
    )
    connection.commit()


# delete data from table
def delete_data(cursor, connection, sql_delete, name2):
    cursor.execute(sql_delete, (name2,))
    connection.commit()


### ---- two more queries ---- ###
def count_book_by_stock(cursor, stock):
    cursor.execute("SELECT COUNT(*) FROM books WHERE stock=?", (stock,))
    return cursor.fetchone()


def fetch_books_ordered_by_name(cursor):
    cursor.execute("SELECT * FROM books ORDER BY name")
    return cursor.fetchall()


def main():
    connection = connect_to_database()
    '''
    # create cursor
    cursor = create_cursor(connection)
    # C: create a table
    query_creation = """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        stock INTEGER NOT NULL,
        comment TEXT
    )
    """
    create_table(connection, cursor, query_creation)
    query_insertion = "INSERT INTO books (name, stock, comment) VALUES (?, ?, ?)"
    insert_data(
        cursor, connection, query_insertion, "Red Chamber", 30, "Uncopiable Love Story"
    )
    insert_data(
        cursor, connection, query_insertion, "Educated", 35, "Meaning of Education"
    )
    # R: read from table
    query_read = "SELECT * FROM books WHERE name=?"
    input_read = "Red Chamber"
    read_data(cursor, query_read, input_read)
    # U: update table
    query_update = "UPDATE books SET stock=? WHERE name=?"
    stock = 25
    name = "Red Chamber"
    update_data(cursor, connection, query_update, stock, name)
    # two more queries
    print(count_book_by_stock(cursor, 35))
    print(fetch_books_ordered_by_name(cursor))
    # D: Delete table
    query_deletion = "DELETE FROM books WHERE name=?"
    name2 = "Red Chamber"
    name3 = "Educated"
    delete_data(cursor, connection, query_deletion, name2)
    delete_data(cursor, connection, query_deletion, name3)

    # close connection
    connection.close()
    '''


if __name__ == "__main__":
    main()
