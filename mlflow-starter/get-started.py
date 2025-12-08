import mlflow

# Setting the tracking URI to local server
mlflow.set_tracking_uri("http://127.0.0.1:5000")

# Setting the experiment name
mlflow.set_experiment("Check Localhost connection")

# Starting a new MLflow run
with mlflow.start_run():
    mlflow.log_metric("test", 1)
    mlflow.log_metric("saurav", 2)

with mlflow.start_run():
    mlflow.log_metric("test1", 3)
    mlflow.log_metric("saurav1", 4)
