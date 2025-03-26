from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.datasets import Dataset

from datetime import datetime, timedelta


def _outlet_to_dataset(**context):
    print("This task only outlets to a Dataset!")


def _consume_from_dataset(**context):
    print("This task only consumes from a Dataset!")


with DAG(
    dag_id="outlet_to_dataset_once",
    start_date=datetime(2025, 1, 1),
    schedule="@once"
) as dag:

    # Schedule a single Task to run once
    ingest_historical_data = PythonOperator(
        task_id="ingest_historical_data",
        python_callable=_outlet_to_dataset,
        outlets=[Dataset("historical_data")]
    )

    ingest_historical_data


with DAG(
    dag_id="outlet_to_dataset_every_minute",
    start_date=datetime(2025, 1, 1),
    schedule=timedelta(minutes=1),
    catchup=False
) as dag:

    # Again, outlet to a Dataset
    ingest_nrt_data = PythonOperator(
        task_id="ingest_nrt_data",
        python_callable=_outlet_to_dataset,
        outlets=[Dataset("nrt_data")]
    )


with DAG(
    dag_id="consume_from_dataset",
    start_date=datetime(2025, 1, 1),
    schedule=(Dataset("historical_data") | Dataset("nrt_data"))
) as dag:

    consume_from_dataset = PythonOperator(
        task_id="consume_from_dataset",
        python_callable=_consume_from_dataset
    )

    empty_task = EmptyOperator(task_id="empty")

    consume_from_dataset >> empty_task
