'''
# House Price Prediction with MLflow
I will: 
- Run a hyperparameter tuning while training a model 
- Log every Hyperparameter and metrics in the MLFlow UI 
- Compate the results of the various runs in the MLFlow UI
- Choose the best run and register it as a model.
'''

import pandas as pd
import mlflow 
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.datasets import fetch_california_housing
from urllib.parse import urlparse
from mlflow.models import infer_signature



housing = fetch_california_housing()
# print(housing)

# Preparing the datasets 
data = pd.DataFrame(housing.data, columns=housing.feature_names)   
data['Price'] = housing.target
print(data.head(10))

# Train test split, model hyperparameter tuning , mlflow experiments 

# Independent and dependent features
X = data.drop(columns=['Price'])
y = data['Price']

# Hyperparameter tuning using grid searchcv

def hyperparameter_tuning(X_train, y_train, param_grid):
    rf = RandomForestRegressor()
    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=3, n_jobs=-1, scoring='neg_mean_squared_error')
    grid_search.fit(X_train, y_train)
    return grid_search

# Split the dataset into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
signature = infer_signature(X_train, y_train)


## Define the hyperparameter grid
param_grid = {
    'n_estimators': [50, 100],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}

## Star the MLflow experiments
mlflow.set_tracking_uri("http://127.0.0.1:5000")

with mlflow.start_run():
    grid_search = hyperparameter_tuning(X_train, y_train, param_grid)
    best_model = grid_search.best_estimator_

    y_pred = best_model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    mlflow.log_params(grid_search.best_params_)  # cleaner
    mlflow.log_metric("mse", mse)

    tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

    if tracking_url_type_store != "file":
        mlflow.sklearn.log_model(best_model, "model", registered_model_name="HousePricePredictionModel")
    else:
        mlflow.sklearn.log_model(best_model, "model", signature=signature)

    print(f"Best Hyperparameters: {grid_search.best_params_}")
    print(f"Mean Squared Error: {mse}")


