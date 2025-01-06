from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import seaborn as sns

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
X = df.drop(columns=['quantity', 'total', 'date'])
y = df['quantity']

# Split data into trainig and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Predict and evaluate
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {round(mse, 2)}")

# Visualization
plt.figure(figsize=(12, 8))

# Plot of actual sales
sns.lineplot(x=df['date'], y=df['quantity'], label='Real Sales', marker='o')

# Prepare the predictions for plotting
X_test['predicted_quantity'] = predictions
X_test['date'] = df.loc[X_test.index, 'date']

sns.lineplot(x=X_test['date'], y=X_test['predicted_quantity'], label='Predicted Sales', linestyle='--', marker='o')

# Prepare date range from 2022 to 2023
dates = pd.date_range(start='2022-01', end='2023-12', freq='MS')
plt.xticks(dates, labels=[date.strftime('%Y-%m') for date in dates], rotation=45)

# Configure the plot
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Real Sales vs Predictions')
plt.legend()
plt.grid(True)
plt.show()