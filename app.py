
from flask import Flask, request, jsonify
import pandas as pd
import mlflow.pyfunc

app = Flask(__name__)
model = mlflow.pyfunc.load_model("model")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data)
    predictions = model.predict(df)
    return jsonify(predictions.tolist())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
