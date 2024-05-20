
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn
import os
import shutil

def load_data():
    X_train = pd.read_csv('data/X_train.csv')
    X_test = pd.read_csv('data/X_test.csv')
    y_train = pd.read_csv('data/y_train.csv')
    y_test = pd.read_csv('data/y_test.csv')
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train.values.ravel())
    return model

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return accuracy

if __name__ == "__main__":
    mlflow.start_run()

    X_train, X_test, y_train, y_test = load_data()
    model = train_model(X_train, y_train)
    accuracy = evaluate_model(model, X_test, y_test)

    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", accuracy)
    
    # Ensure the model directory exists and is empty
    model_path = "model"
    if os.path.exists(model_path):
        shutil.rmtree(model_path)
    os.makedirs(model_path)
    
    # Save the model to the 'model' directory
    mlflow.sklearn.save_model(model, model_path)

    mlflow.end_run()
