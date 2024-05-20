
import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv('data/heart_disease.csv', header=None)

# Define column names
data.columns = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
    'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'
]

# Replace '?' with NaN
data.replace('?', pd.NA, inplace=True)

# Convert columns to numeric, forcing errors to NaN
data = data.apply(pd.to_numeric, errors='coerce')

# Fill NaN values with column mean
data.fillna(data.mean(), inplace=True)

# Split dataset into features and target variable
X = data.drop(columns=['target'])
y = data['target']

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Save the train and test sets
X_train.to_csv('data/X_train.csv', index=False)
X_test.to_csv('data/X_test.csv', index=False)
y_train.to_csv('data/y_train.csv', index=False)
y_test.to_csv('data/y_test.csv', index=False)
