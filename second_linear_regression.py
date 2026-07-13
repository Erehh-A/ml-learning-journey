import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

# Data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 20, 60, 70, 87])

# Split data FIRST
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply polynomial features AFTER split (fit only on train!)
poly = PolynomialFeatures(degree=3)
X_train_poly = poly.fit_transform(X_train)  # fit_transform on train
X_test_poly = poly.transform(X_test)        # only transform on test

# Create & train model
model = LinearRegression()
model.fit(X_train_poly, y_train)

# Predict
pred = model.predict(X_test_poly)

print("Predictions:", pred)
print("Actual:     ", y_test)

# Error
error = mean_squared_error(y_test, pred)  # compare test values only
print("Error:", error)

# Plot
X_plot = np.linspace(1, 5, 100).reshape(-1, 1)
X_plot_poly = poly.transform(X_plot)
pred_plot = model.predict(X_plot_poly)

plt.scatter(X, y, color='red', label='Actual')
plt.plot(X_plot, pred_plot, label='Predicted')
plt.legend()
plt.show()