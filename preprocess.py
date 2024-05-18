import pandas as pd
from sklearn.model_selection import train_test_split

def load_data():
    column_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
                    'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']
    data = pd.read_csv('data/heart_disease.csv', header=None, names=column_names, na_values='?')
    data = data.dropna()  # Drop rows with missing values
    return data

def preprocess_data(data):
    X = data.drop(columns=['target'])
    y = data['target'].apply(lambda x: 1 if x > 0 else 0)  # Binary classification
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    data = load_data()
    X_train, X_test, y_train, y_test = preprocess_data(data)
    X_train.to_csv('data/X_train.csv', index=False)
    X_test.to_csv('data/X_test.csv', index=False)
    y_train.to_csv('data/y_train.csv', index=False)
    y_test.to_csv('data/y_test.csv', index=False)
