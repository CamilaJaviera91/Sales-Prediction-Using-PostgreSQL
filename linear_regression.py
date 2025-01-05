from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from query import query
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(query())

# Assign names to the columns
df.columns = ['month', 'year', 'product', 'quantity', 'total']

# Drop 'product' column
df = df.drop(columns=['product'])

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
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {round(mse, 2)}")

# Visualization
plt.figure(figsize=(10, 6))

# Plot of actual sales
plt.plot(df['date'], df['quantity'], label='Ventas Reales', marker='o', linestyle='-')

# Prepare the predictions for plotting
X_test['predicted_quantity'] = predictions
X_test['date'] = pd.to_datetime(X_test[['year', 'month']].assign(day=1))

# Plot the predictions
plt.plot(X_test['date'], X_test['predicted_quantity'], label='Ventas Predichas', linestyle='--', marker='x')

# Configure the plot
plt.legend()
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Real sales vs Predictions')
plt.grid(True)
plt.show()
