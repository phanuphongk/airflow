from airflow import DAG
from airflow.utils import timezone
from airflow.operators.python import PythonOperator


def _hello():
    return "Hello"

def _world():
    return "world"

with DAG(
    "etl",
    start_date=timezone.datetime(2024, 5, 8),
    schedule=None,


):


    hello = PythonOperator(
        task_id ="hello",
        python_callbel =,
    )

    world = PythonOperator(
        task_id ="world",
        python_callbel =,
    )

    hello >> world