import psycopg2

def connection():
    # Configuring the connection
    conexion = None
    try:
        # Connecting to the PostgreSQL database
        conexion = psycopg2.connect(
            host="localhost",           # Address of the PostgreSQL server (localhost for local machine)
            database="postgres",        # Name of the database to connect to
            user="postgres",            # Database username
            password="1234",            # Password for the user
            port="5432"                 # Port PostgreSQL is listening on (default is 5432)
        )
        print("Conexión exitosa")  # Successful connection message
        
        # Create a cursor to execute queries
        cursor = conexion.cursor()
        
        # Execute an SQL query
        cursor.execute("SELECT version();")  # Query to get the PostgreSQL version
        
        # Get the result
        version = cursor.fetchone()
        print("Versión de PostgreSQL:", version)  # Output the PostgreSQL version
        
        # Close the cursor
        cursor.close()

    except psycopg2.Error as e:
        # Error handling if something goes wrong with the connection or query
        print("Error al conectar a la base de datos:", e)
    finally:
        # Ensure the connection is closed even if there was an error
        if conexion is not None:
            conexion.close()
            print("Conexión cerrada")  # Connection closed message