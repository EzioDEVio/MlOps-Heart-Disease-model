
[![MLOps CI/CD Pipeline](https://github.com/EzioDEVio/MlOps-Heart-Disease-model/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/EzioDEVio/MlOps-Heart-Disease-model/actions/workflows/ci-cd.yml) 


# Heart Disease Prediction Project

This project is a web application that predicts whether a patient has heart disease based on various medical attributes. The application uses a machine learning model trained on the Cleveland Heart Disease dataset from the UCI Machine Learning Repository. You can browse other datasets from Kaggle which is opensource for all machine learning models.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Data Preprocessing](#data-preprocessing)
- [Model Training](#model-training)
- [Running the Flask App](#running-the-flask-app)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
This project demonstrates the use of machine learning and MLOps tools to create a predictive model and deploy it as a web application. The model predicts the presence of heart disease based on medical attributes such as age, sex, chest pain type, and more.

## Dataset
The dataset used in this project is the Cleveland Heart Disease dataset from the UCI Machine Learning Repository. This dataset contains 14 attributes:

- `age`: Age in years
- `sex`: Sex (1 = male, 0 = female)
- `cp`: Chest pain type (1: typical angina, 2: atypical angina, 3: non-anginal pain, 4: asymptomatic)
- `trestbps`: Resting blood pressure (in mm Hg)
- `chol`: Serum cholesterol (in mg/dl)
- `fbs`: Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
- `restecg`: Resting electrocardiographic results (0: normal, 1: having ST-T wave abnormality, 2: showing probable or definite left ventricular hypertrophy)
- `thalach`: Maximum heart rate achieved
- `exang`: Exercise induced angina (1 = yes, 0 = no)
- `oldpeak`: ST depression induced by exercise relative to rest
- `slope`: The slope of the peak exercise ST segment (1: upsloping, 2: flat, 3: downsloping)
- `ca`: Number of major vessels (0-3) colored by fluoroscopy
- `thal`: Thalassemia (3 = normal, 6 = fixed defect, 7 = reversable defect)
- `target`: Diagnosis of heart disease (1 = presence, 0 = absence)

## Project Structure
The project structure is as follows:

MlOps_Heart_Disease/
│
├── app.py # Flask application
├── preprocess.py # Data preprocessing script
├── train.py # Model training script
├── test_model.py # Script to test the model
├── test_app.py # Script to test the Flask app
├── templates/
│ └── index.html # HTML template for the web interface
├── static/
│ └── heart-logo.png # Logo image
├── model/ # Directory where the trained model is saved
├── data/ # Directory for the dataset
│ └── heart.csv # Heart disease dataset
├── requirements.txt # Python dependencies
└── README.md # Project documentation



## Getting Started

### Prerequisites
- Python 3.8+
- Pip (Python package installer)
- Virtual environment (optional but recommended)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/MlOps_Heart_Disease.git
    cd MlOps_Heart_Disease
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv mlops-env
    source mlops-env/bin/activate  # On Windows use `mlops-env\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Data Preprocessing
1. Download the dataset from [Kaggle](https://www.kaggle.com/):
    - Sign in to Kaggle and download the Cleveland Heart Disease dataset.
    - Place the downloaded `heart.csv` file in the `data/` directory.

2. Run the preprocessing script to clean and split the data:
    ```bash
    python preprocess.py
    ```

### Model Training
1. Train the model using the preprocessed data:
    ```bash
    python train.py
    ```

    This script will train a Random Forest classifier and save the model in the `model/` directory.

### Running the Flask App
1. Start the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

### Usage
- Fill out the form on the web interface with the required medical attributes.
- Click the "Predict" button to get the prediction result.
- The prediction result will indicate whether the patient has heart disease or not.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or new features to add.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


