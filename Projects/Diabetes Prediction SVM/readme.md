# Diabetes Prediction using SVM

## Overview
This project implements a machine learning model using **Support Vector Machine (SVM)** to predict diabetes based on a dataset containing various health parameters. The dataset is preprocessed, split into training and testing sets, and standardized before training the model.

## Dataset
The dataset used for this project is **diabetes.csv**, which includes multiple health-related features such as glucose level, BMI, and age to predict whether a patient has diabetes.

## Model
The model is built using **Support Vector Classifier (SVC)** with a linear kernel. The training process involves:
- Splitting the dataset into training and testing sets (75%-25%) .
- Feature scaling to standardize the dataset.
- Training the SVM classifier on the training data.
- Evaluating the model using a **Confusion Matrix** and **Accuracy Score**.

## Requirements
Ensure you have the following Python libraries installed before running the code:
```bash
pip install numpy pandas scikit-learn matplotlib
```

## Running the Project
To execute the script, run the following command:
```bash
python diabetes_prediction.py
```

## Key Features
- Uses **Support Vector Machine (SVM)** for classification.
- Standardizes features using **StandardScaler**.
- Provides accuracy assessment using a **Confusion Matrix**.
- Includes sample predictions using the trained model.

## Limitations
- The dataset has **8 features**, making 2D visualization of the decision boundary impractical.
- However the dimentionalty readuction techniques can be used.
