import pandas as pd 
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import mlflow 
from mlflow.models import infer_signature


# Set the tracking URI 
mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")

# Load the Dataset 
X,y = datasets.load_iris(return_X_y=True)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Define the model hyperparameters
# params = {"penalty": "l2", "solver": "lbfgs", "max_iter": 1000, "random_state": 8888}
# New paramater 
params = {"solver": "newton-cg", "max_iter": 1000, "random_state": 1000}


# Train the model 
lr = LogisticRegression(**params)
lr.fit(X_train, y_train)


# Prediction on the test set 
y_pred = lr.predict(X_test)
print(y_pred)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# MlFlow Tracking 

mlflow.set_tracking_uri("http://127.0.0.1:5000")

# Create a New MLflow Experiment 
mlflow.set_experiment("Iris-Logistic-Regression-Experiment")

# Start an MLflow Run
with mlflow.start_run(run_name="Iris-Logistic-Regression-Run"):
    ## Log Model Hyperparameters
    mlflow.log_params(params)

    ## Log the accuracy metrics
    mlflow.log_metric("accuracy", accuracy)

    ## Set a Tag that we can use to remind ouselves what this run was for 
    mlflow.set_tag("Training Info", "Basic LR modle for Iris data ")

    ## Infer the model signature 

    signature = infer_signature(X_train,lr.predict(X_train)) # automatically detects the input and output schema for your model by looking at sample data.
    '''
    Instead of you manually writing:
    column names
    data types
    output types
    …it figures all that out for you.
    '''

    # Log the trained model
    model_info = mlflow.sklearn.log_model(
        sk_model=lr,
        artifact_path="iris_model",
        signature=signature,
        input_example=X_train,
        registered_model_name="Iris-Logistic-Regression-Model"
    )
