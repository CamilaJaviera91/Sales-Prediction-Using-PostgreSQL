# Import the connection function from the 'connection' file
from connection import connection as ct

# Import necessary libraries
import psycopg2
import locale

def query():
    # Set the locale to Spanish (Spain) to ensure proper formatting
    locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
    
    # Establish a connection using the connection function (ct()) from 'connection.py'
    con = ct()
    if con is None:
        print("Error: No se pudo establecer la conexión con la base de datos.")
        return  # Stop execution if the connection is not established

    cursor = con.cursor()  # Create a cursor to interact with the database

    # Execute the SQL query to retrieve the sales data grouped by year-month and product name
    cursor.execute('''
                    SELECT 
                        TO_CHAR(date, 'YYYY-MM') AS year_month,   -- Format the date to year-month
                        product_name AS name,                      -- Product name
                        SUM(s.quantity_sold) AS quantity,          -- Sum of quantities sold
                        SUM(s.unit_value) AS value                 -- Sum of the unit values
                    FROM sales AS s
                    GROUP BY 
                        TO_CHAR(date, 'YYYY-MM'), product_name    -- Grouping by year-month and product name
                    ORDER BY 
                        TO_CHAR(date, 'YYYY-MM');                 -- Order by the year-month column
                    ''')

    # Fetch all the results from the query
    records = cursor.fetchall()

    # Print the records
    print("Registros obtenidos de la consulta:")
    for record in records:
        print(record)

    # Close the connection after fetching the results
    cursor.close()  # Close the cursor
    con.close()    # Close the connection to free up resources

    # Return the fetched records if needed
    return records

# Call the query function
query()
