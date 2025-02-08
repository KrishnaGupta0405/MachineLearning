
## Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

import os
from sklearn.datasets import fetch_california_housing

#Fetch dataset from the sklearn datasets
filename = 'california_housing.csv'
if not os.path.exists(filename):
    housing = fetch_california_housing()
    housing_df = pd.DataFrame(data=housing.data, columns=housing.feature_names) # Create a DataFrame
    housing_df['price($Millon)'] = housing.target # Add the target column
    housing_df.to_csv(filename, index=False)

#import the dataset
dataset = pd.read_csv(filename)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

"""
**Exploratory Data Analysis (EDA)**:
   - Checking dataset shape, missing values, and statistical measures.
   - Understanding feature correlation using a heatmap.
"""

# checking the number of rows and Columns in the data frame
dataset.shape

# check for missing values
dataset.isnull().sum()

# In case you have missing value, we can apply the Simple Imputer, code given below->

# from sklearn.impute import SimpleImputer
# imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
# imputer.fit(X[:, 1:3])
# X[:, 1:3] = imputer.transform(X[:, 1:3])


# Print First 5 rows of our DataFrame
dataset.head()

# checking the number of rows and Columns in the data frame
dataset.shape

# statistical measures of the dataset
dataset.describe()

"""**Understanding the correlation between various features in the dataset**
1. Positive Correlation
2. Negative Correlation
"""

# correlation = dataset.corr()
# print(correlation)

"""# constructing a heatmap to nderstand the correlation"""

# import seaborn as sns
# plt.figure(figsize=(10,10))
# sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')

"""## Splitting the dataset into the Training set (80%) and Test set (20%)"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""## Training XGBoost on the Training set
        -> Self tuning is the beauty of the XGBoost ;)"""

# Due to some incompatibily issues in skitlearn lib and XGBoost, i reffered to stackOverFlowlink below which says to install prev. version of skit learn, which worked for me...
# Link-> [https://stackoverflow.com/questions/79290968/super-object-has-no-attribute-sklearn-tags]
# !pip uninstall -y scikit-learn
# !pip install scikit-learn==1.3.1

from xgboost import XGBRegressor
Regressor = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=6)
Regressor.fit(X_train, y_train)

"""## Making the Confusion Matrix"""

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

""""
**Model Evaluation**:
   - Compute performance metrics:
        1. Absolute Error (MAE), 
        2. Mean Squared Error (MSE), 
        3. Root Mean Squared Error (RMSE), and 
        4. R² Score.
"""

# Calculate Regression Metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)  # Root Mean Squared Error
r2 = r2_score(y_test, y_pred)

# Print Results
print(f"Mean Absolute Error (MAE): {mae:.4f}")  #rounding off to 4 zeros after decimal point
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"R² Score: {r2:.4f}")

# This validation is not compulsory.
"""## Applying k-Fold Cross Validation"""

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = Regressor, X = X_train, y = y_train, cv = 10)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))

"""#Visulaizing the results"""

# Visualize the actual vs. predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs. Predicted Values")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--') # Add a diagonal line
plt.show()

# Feature Importance Plot (requires the Regressor object)
plt.figure(figsize=(10,6))
feature_importance = Regressor.feature_importances_
sorted_idx = np.argsort(feature_importance)
pos = np.arange(sorted_idx.shape[0]) + 0.5
plt.barh(pos, feature_importance[sorted_idx], align='center')
plt.yticks(pos, np.array(dataset.columns[:-1])[sorted_idx])
plt.title("Feature Importance")
plt.show()