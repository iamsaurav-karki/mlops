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