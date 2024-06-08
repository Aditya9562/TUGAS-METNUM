import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the dataset
df = pd.read_csv(r"C:\Users\aditya\Downloads\archive\Student_Performance.csv")

# Prepare the data
X = df[['Hours Studied']]
y = df['Performance Index']

# Log-transform the data for power model
X_log = np.log(df['Hours Studied']).values.reshape(-1, 1)
y_log = np.log(df['Performance Index']).values

# Power Model Regression (linear regression on log-transformed data)
power_model = LinearRegression()
power_model.fit(X_log, y_log)
y_pred_power_log = power_model.predict(X_log)
y_pred_power = np.exp(y_pred_power_log)

# Calculate RMS Error
rms_error_power = np.sqrt(mean_squared_error(y, y_pred_power))

# Plotting the data and the power model regression line
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['Hours Studied'], y=df['Performance Index'], label='Data')
plt.plot(df['Hours Studied'], y_pred_power, color='green', label='Power Model Line')
plt.title(f'Power Model: RMS Error = {rms_error_power:.2f}')
plt.xlabel('Hours Studied')
plt.ylabel('Performance Index')
plt.legend()
plt.grid(True)
plt.show()

# Print RMS Error
print(f'RMS Error of Power Model: {rms_error_power:.2f}')
