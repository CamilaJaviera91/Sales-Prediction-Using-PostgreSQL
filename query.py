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
                    select
                        extract(month from s.date) as month, -- Format the date to month 
                        extract(year from s.date) as year,   -- Format the date to year
                        s.product_name as name,              -- Product name
                        sum(s.quantity_sold) as quantity,    -- Sum of quantities sold
                        sum(s.unit_value) as total           -- Sum of the unit values
                    from sales as s
                    group by                                 -- Grouping by month, year and product name
                        extract(month from s.date),
                        extract(year from s.date), 
                        s.product_name    
                    ORDER BY 
                        extract(month from s.date),
                        extract(year from s.date);           -- Order by month and year column
                    ''')

    # Fetch all the results from the query
    records = cursor.fetchall()

    # Close the connection after fetching the results
    cursor.close()  # Close the cursor
    con.close()    # Close the connection to free up resources

    # Return the fetched records if needed
    return records