from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    f"dbt_cli_snowflake_dag",
    schedule="@hourly",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    default_args={
        "retries": 0,
    },
    tags=["cosmos"],
) as dag:

    run_dbt = BashOperator(
        task_id="run_dbt",
        bash_command="cd /usr/local/airflow/ && \
            source dbt_venv/bin/activate && \
            cd dags/cosmos/dbt/dbtproject/ && \
            dbt deps && \
            dbt run --profiles-dir profiles --models analysis transform downstream --log-path /home/astro --target-path /home/astro",
    )

    run_dbt
