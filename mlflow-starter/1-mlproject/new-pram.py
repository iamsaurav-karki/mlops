import pandas as pd 
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import mlflow 
from mlflow.models import infer_signature
from mlflow.models import validate_serving_input 



# Set the tracking URI 
mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")

# Load the Dataset 
X,y = datasets.load_iris(return_X_y=True)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Define the model hyperparameters
params = {"penalty": "l2", "solver": "lbfgs", "max_iter": 1000, "random_state": 8888}
# New paramater 
# params = {"solver": "newton-cg", "max_iter": 1000, "random_state": 1000}


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

# Inferencing and Validating Model 

print(model_info.model_uri)

model_uri = "models:/m-27b4c53115334405a62e2ee5654ed262"

'''
The model is logged with an input example . Mlflow converts it into the serving payload format
for the deployed model endpoint, and saves it to 'serving_input_payload.json'.
'''

serving_payload = """{
    "inputs": [
    [
        6.4,
        3.1,
        5.5,
        1.8
  ],
  [
    6.4,
    2.9,
    4.3,
    1.3
  ],
  [
    5.5,
    2.6,
    4.4,
    1.2
  ],
  [
    5.9,
    3,
    5.1,
    1.8
  ],
  [
    5.1,
    3.3,
    1.7,
    0.5
  ],
  [
    5.2,
    3.5,
    1.5,
    0.2
  ],
  [
    5.4,
    3.4,
    1.7,
    0.2
  ],
  [
    6.7,
    3,
    5.2,
    2.3
  ],
  [
    5.6,
    3,
    4.1,
    1.3
  ],
  [
    4.6,
    3.2,
    1.4,
    0.2
  ],
  [
    5,
    2,
    3.5,
    1
  ],
  [
    5.5,
    4.2,
    1.4,
    0.2
  ],
  [
    6.2,
    2.8,
    4.8,
    1.8
  ],
  [
    7.9,
    3.8,
    6.4,
    2
  ],
  [
    5.7,
    2.8,
    4.1,
    1.3
  ],
  [
    4.9,
    3,
    1.4,
    0.2
  ],
  [
    6.9,
    3.1,
    5.4,
    2.1
  ],
  [
    6.5,
    3,
    5.5,
    1.8
  ],
  [
    5.8,
    4,
    1.2,
    0.2
  ],
  [
    6.1,
    2.8,
    4,
    1.3
  ],
  [
    6.6,
    2.9,
    4.6,
    1.3
  ],
  [
    5.6,
    3,
    4.5,
    1.5
  ],
  [
    4.9,
    2.4,
    3.3,
    1
  ],
  [
    4.7,
    3.2,
    1.6,
    0.2
  ],
  [
    5.7,
    4.4,
    1.5,
    0.4
  ],
  [
    6.1,
    2.6,
    5.6,
    1.4
  ],
  [
    6.3,
    2.5,
    4.9,
    1.5
  ],
  [
    6.5,
    3.2,
    5.1,
    2
  ],
  [
    5,
    3.4,
    1.5,
    0.2
  ],
  [
    7.1,
    3,
    5.9,
    2.1
  ],
  [
    5.1,
    3.5,
    1.4,
    0.3
  ],
  [
    6.9,
    3.1,
    5.1,
    2.3
  ],
  [
    6.2,
    3.4,
    5.4,
    2.3
  ],
  [
    5.4,
    3.9,
    1.7,
    0.4
  ],
  [
    4.8,
    3.1,
    1.6,
    0.2
  ],
  [
    5.1,
    3.5,
    1.4,
    0.2
  ],
  [
    6.3,
    2.8,
    5.1,
    1.5
  ],
  [
    6.1,
    2.9,
    4.7,
    1.4
  ],
  [
    4.9,
    3.1,
    1.5,
    0.1
  ],
  [
    6.3,
    3.3,
    6,
    2.5
  ],
  [
    7.7,
    3.8,
    6.7,
    2.2
  ],
  [
    5.6,
    2.9,
    3.6,
    1.3
  ],
  [
    5.4,
    3.4,
    1.5,
    0.4
  ],
  [
    5.8,
    2.7,
    5.1,
    1.9
  ],
  [
    4.8,
    3.4,
    1.6,
    0.2
  ],
  [
    4.5,
    2.3,
    1.3,
    0.3
  ],
  [
    5,
    2.3,
    3.3,
    1
  ],
  [
    5.2,
    2.7,
    3.9,
    1.4
  ],
  [
    7,
    3.2,
    4.7,
    1.4
  ],
  [
    6.2,
    2.2,
    4.5,
    1.5
  ],
  [
    6.8,
    3,
    5.5,
    2.1
  ],
  [
    4.4,
    2.9,
    1.4,
    0.2
  ],
  [
    6.3,
    3.4,
    5.6,
    2.4
  ],
  [
    5.9,
    3.2,
    4.8,
    1.8
  ],
  [
    5.4,
    3,
    4.5,
    1.5
  ],
  [
    5,
    3.4,
    1.6,
    0.4
  ],
  [
    6.3,
    3.3,
    4.7,
    1.6
  ],
  [
    5,
    3.3,
    1.4,
    0.2
  ],
  [
    6.4,
    2.8,
    5.6,
    2.2
  ],
  [
    7.7,
    3,
    6.1,
    2.3
  ],
  [
    6.4,
    3.2,
    4.5,
    1.5
  ],
  [
    5.1,
    3.8,
    1.5,
    0.3
  ],
  [
    5,
    3,
    1.6,
    0.2
  ],
  [
    6.7,
    2.5,
    5.8,
    1.8
  ],
  [
    6.1,
    3,
    4.6,
    1.4
  ],
  [
    6,
    3.4,
    4.5,
    1.6
  ],
  [
    6.9,
    3.2,
    5.7,
    2.3
  ],
  [
    5.2,
    4.1,
    1.5,
    0.1
  ],
  [
    6.5,
    3,
    5.2,
    2
  ],
  [
    5.6,
    2.7,
    4.2,
    1.3
  ],
  [
    4.9,
    2.5,
    4.5,
    1.7
  ],
  [
    5.5,
    2.5,
    4,
    1.3
  ],
  [
    7.2,
    3.2,
    6,
    1.8
  ],
  [
    4.9,
    3.1,
    1.5,
    0.2
  ],
  [
    6.6,
    3,
    4.4,
    1.4
  ],
  [
    4.9,
    3.6,
    1.4,
    0.1
  ],
  [
    5,
    3.2,
    1.2,
    0.2
  ],
  [
    6.4,
    2.8,
    5.6,
    2.1
  ],
  [
    4.3,
    3,
    1.1,
    0.1
  ],
  [
    5,
    3.5,
    1.3,
    0.3
  ],
  [
    6,
    3,
    4.8,
    1.8
  ],
  [
    6,
    2.9,
    4.5,
    1.5
  ],
  [
    6.5,
    2.8,
    4.6,
    1.5
  ],
  [
    6.3,
    2.3,
    4.4,
    1.3
  ],
  [
    5.1,
    3.4,
    1.5,
    0.2
  ],
  [
    6.4,
    3.2,
    5.3,
    2.3
  ],
  [
    6.9,
    3.1,
    4.9,
    1.5
  ],
  [
    7.6,
    3,
    6.6,
    2.1
  ],
  [
    5,
    3.5,
    1.6,
    0.6
  ],
  [
    5.8,
    2.8,
    5.1,
    2.4
  ],
  [
    5.5,
    2.4,
    3.8,
    1.1
  ],
  [
    6.7,
    3.1,
    5.6,
    2.4
  ],
  [
    5.7,
    2.5,
    5,
    2
  ],
  [
    4.6,
    3.4,
    1.4,
    0.3
  ],
  [
    6,
    2.7,
    5.1,
    1.6
  ],
  [
    5.7,
    3,
    4.2,
    1.2
  ],
  [
    6.1,
    3,
    4.9,
    1.8
  ],
  [
    6.7,
    3.3,
    5.7,
    2.5
  ],
  [
    6.7,
    3.1,
    4.7,
    1.5
  ],
  [
    7.7,
    2.6,
    6.9,
    2.3
  ],
  [
    5.8,
    2.7,
    5.1,
    1.9
  ],
  [
    6.4,
    2.7,
    5.3,
    1.9
  ],
  [
    6.3,
    2.7,
    4.9,
    1.8
  ],
  [
    7.7,
    2.8,
    6.7,
    2
  ],
  [
    4.6,
    3.1,
    1.5,
    0.2
  ],
  [
    5.8,
    2.6,
    4,
    1.2
  ],
  [
    7.3,
    2.9,
    6.3,
    1.8
  ],
  [
    5.1,
    2.5,
    3,
    1.1
  ],
  [
    5.7,
    2.6,
    3.5,
    1
  ],
  [
    6.5,
    3,
    5.8,
    2.2
  ],
  [
    6.8,
    3.2,
    5.9,
    2.3
  ],
  [
    5.7,
    2.9,
    4.2,
    1.3
  ],
  [
    6.8,
    2.8,
    4.8,
    1.4
  ],
  [
    6,
    2.2,
    4,
    1
  ],
  [
    6.3,
    2.5,
    5,
    1.9
  ],
  [
    5.8,
    2.7,
    4.1,
    1
  ],
  [
    7.2,
    3.6,
    6.1,
    2.5
  ],
  [
    6.2,
    2.9,
    4.3,
    1.3
  ],
  [
    4.6,
    3.6,
    1,
    0.2
  ],
  [
    5.1,
    3.8,
    1.6,
    0.2
  ]
]
}"""

# Validate the serving payload works on the model 

valid_serving_input_value = validate_serving_input(model_uri,serving_payload)

print("Serving input is valid!")
print(valid_serving_input_value)

# Second option to validate and infer 
# Load the model back for prediction as a generic python function model 
loaded_model = mlflow.pyfunc.load_model(model_info.model_uri)
predictions = loaded_model.predict(X_test)

iris_feature_names = datasets.load_iris().feature_names
df_predictions = pd.DataFrame(X_test, columns=iris_feature_names)
df_predictions['actual_class'] = y_test
df_predictions['predicted_class'] = predictions
print("\nPredictions on test data:")
print(df_predictions)
print(df_predictions.head(5))