# Sales Analysis and Prediction using Random Forest

This project is designed to extract sales data from a PostgreSQL database, process it, and use a Random Forest model to predict sales quantities. It also visualizes real and predicted sales for better understanding.

## Project Structure

```
project/
|-- connection.py
|-- query.py
|-- random_forest.py
```

### 1. `connection.py`
This script establishes a connection to the PostgreSQL database using the `psycopg2` library. It handles errors gracefully and ensures a reliable connection.

- **Key Functions:**
  - `connection()`: Connects to the database and returns the connection object.

### 2. `query.py`
This script queries the sales data from the database. It groups sales by year, month, and product name and calculates the total quantity sold and revenue for each group.

- **Key Functions:**
  - `query()`: Executes the SQL query and returns the grouped sales data.

### 3. `random_forest.py`
This script uses the queried sales data to train a Random Forest Regressor model and predicts future sales. It also visualizes the real and predicted sales for comparison.

- **Workflow:**
  1. Fetches data using `query()`.
  2. Processes and transforms the data.
  3. Trains a Random Forest Regressor on historical sales data.
  4. Evaluates the model using Mean Squared Error (MSE).
  5. Visualizes real and predicted sales.

## Prerequisites

- Python 3.8+
- PostgreSQL database with a `sales` table.

### Required Python Libraries
Install the dependencies using pip:
```bash
pip install psycopg2 pandas matplotlib seaborn scikit-learn
```

## Database Table Structure
The project assumes a `sales` table with the following structure:

| Column         | Type         | Description                       |
|----------------|--------------|-----------------------------------|
| `date`         | `DATE`       | Date of the sale                  |
| `product_name` | `TEXT`       | Name of the product               |
| `quantity_sold`| `INTEGER`    | Quantity of the product sold      |
| `unit_value`   | `FLOAT`      | Total sales value of the product  |

## How to Run the Project

1. **Set up the PostgreSQL Database:**
   - Ensure the `sales` table is created and populated.

2. **Configure the Database Connection:**
   - Update the `connection.py` file with your PostgreSQL credentials:
     ```python
     conn = psycopg2.connect(
         host="<your_host>",
         database="<your_database>",
         user="<your_user>",
         password="<your_password>",
         port="<your_port>"
     )
     ```

3. **Run the Scripts:**
   - Execute the scripts in the following order:
     ```bash
     python random_forest.py
     ```

## Example Output

- **Mean Squared Error:** Displays the MSE of the predictions.
- **Visualization:** A plot comparing real sales vs. predicted sales over time.

## Notes

- Ensure the locale settings in `query.py` (`es_ES.UTF-8`) match your system's configuration. If not, modify it to a suitable locale.
- This project focuses on predicting sales quantities. Future improvements could include:
  - Predicting revenue.
  - Adding seasonality and external factors to the model.
  - Using advanced machine learning techniques.