from datetime import datetime
import os
from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig, RenderConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping
# test

profile_config = ProfileConfig(
    profile_name="my_profile_name",
    target_name="my_target_name",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_fieldengineer",
    ),
)

airflow_home = os.environ["AIRFLOW_HOME"]

dbt_snowflake_python_dag = DbtDag(
    project_config=ProjectConfig(
        f"{airflow_home}/dbt/dbtproject",
    ),
    operator_args={"install_deps": True},
    profile_config=profile_config,
    execution_config=ExecutionConfig(
        dbt_executable_path=f"{airflow_home}/dbt_venv/bin/dbt",
    ),
    render_config=RenderConfig(
        select=[
            "path:models/python_models",
        ]
    ),
    schedule_interval="@hourly",
    start_date=datetime(2023, 9, 10),
    catchup=False,
    dag_id="dbt_snowflake_python_dag",
    tags=["cosmos"],
)
