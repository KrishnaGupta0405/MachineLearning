# California Housing Price Prediction

## Overview
This project aims to predict housing prices in California using machine learning techniques. The dataset is sourced from Scikit-Learn's `fetch_california_housing` module and is processed, analyzed, and trained using the XGBoost regression model.

## Dataset
The dataset contains various features related to housing in California, such as median income, house age, number of rooms, and population. The target variable is the median house price (in million dollars).

## Project Workflow
1. **Import Libraries**: Load essential Python libraries for data processing, visualization, and model training.
2. **Dataset Handling**:
   - Fetch the California housing dataset.
   - Store it in a CSV file if it doesn't already exist.
   - Load the dataset and preprocess it for further analysis.
3. **Exploratory Data Analysis (EDA)**:
   - Checking dataset shape, missing values, and statistical measures.
   - Understanding feature correlation using a heatmap.
4. **Data Splitting**:
   - Split the dataset into training (80%) and testing (20%) sets using `train_test_split`.
5. **Model Training**:
   - Train an `XGBRegressor` model (Self tuning is the beauty of the XGBoost).
6. **Model Evaluation**:
   - Predict values on the test set.
   - Compute performance metrics: Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R² Score.
7. **Cross-Validation**:
   - Apply k-Fold Cross Validation to evaluate the model’s stability and generalization performance.
8. **Visualization**:
   - Scatter plot to compare actual vs. predicted values.

## Dependencies
Ensure the following Python libraries are installed:
```bash
pip install numpy pandas matplotlib seaborn scikit-learn xgboost
```

## Running the Project
To execute the script, run the following command:
```bash
python housing_price_prediction.py
```

## Additional Notes
- If `scikit-learn` version incompatibility arises with XGBoost, downgrade `scikit-learn` using:
  ```bash
  pip uninstall -y scikit-learn
  pip install scikit-learn==1.3.1
  ```
- The project provides insights into model performance using metrics and visualization techniques.

## Author
This project was developed to analyze and predict California housing prices using machine learning.

