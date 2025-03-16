from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Sample dataset
X = [[1], [2], [3], [4], [5]]
y = [0, 0, 1, 1, 1]  # Labels (0 or 1)

# Scaling the features (important for Logistic Regression)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Training a logistic regression model
model = LogisticRegression(solver='liblinear')  # You can try different solvers like 'lbfgs', 'saga'
model.fit(X_scaled, y)

# Making predictions
y_pred = model.predict(X_scaled)

# Evaluating the model
accuracy = accuracy_score(y, y_pred)

print(f"Accuracy: {accuracy}")
