from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from query import query
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(query())

# Assign names to the columns
df.columns = ['month', 'year', 'product', 'quantity', 'total']

# Transform month and year into a int type
df['month'] = df['month'].astype(int)
df['year'] = df['year'].astype(int)

# Create a date column by combining 'year' and 'month
df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))

print(df.dtypes)

# Features and target variables
X = df[['month', 'year']]
y = df['quantity']

# Split data into trainig and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
predictions = model.predict(X_test)
print(f"Mean Squared Error: {round(mean_squared_error(y_test, predictions), 2)}")