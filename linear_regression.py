from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from query import query
import pandas as pd

df = pd.DataFrame(query())

# Assign names to the columns
df.columns = ['period', 'product', 'quantity', 'total']

# Features and target variables
X = df['period']
y = df['quantity']

# Split data into trainig and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)