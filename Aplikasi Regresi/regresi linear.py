import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Load the dataset
df = pd.read_csv(r"C:\Users\aditya\Downloads\archive\Student_Performance.csv")

# Prepare the data
X = df[['Hours Studied']]
y = df['Performance Index']

# Linear Regression Model
linear_model = LinearRegression()
linear_model.fit(X, y)
y_pred_linear = linear_model.predict(X)

# Calculate RMS Error
rms_error_linear = np.sqrt(mean_squared_error(y, y_pred_linear))

# Plotting the data and the linear regression line
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['Hours Studied'], y=df['Performance Index'], label='Data')
plt.plot(df['Hours Studied'], y_pred_linear, color='red', label='Linear Regression Line')
plt.title(f'Linear Regression: RMS Error = {rms_error_linear:.2f}')
plt.xlabel('Hours Studied')
plt.ylabel('Performance Index')
plt.legend()
plt.grid(True)
plt.show()

# Print RMS Error
print(f'RMS Error of Linear Regression: {rms_error_linear:.2f}')
