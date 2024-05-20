from flask import Flask, request, render_template
import pandas as pd
import mlflow.pyfunc
import os

app = Flask(__name__)

# Ensure the model path matches the saved model path in train.py
model_path = "model"
if not os.path.exists(model_path):
    raise Exception(f"Model path '{model_path}' does not exist. Please train the model first.")

model = mlflow.pyfunc.load_model(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    feature_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
                     'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    data = {feature: [data[feature]] for feature in feature_names}
    df = pd.DataFrame(data)
    predictions = model.predict(df)
    prediction_text = "Patient with heart disease" if predictions[0] == 1 else "Patient has no heart disease"
    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
