from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.http_operator import SimpleHttpOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 6),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10),  # Adjusted retry delay to match the periodicity
}

dag = DAG(
    'reload_page',
    default_args=default_args,
    description='Reloads the FastAPI page to show the current time',
    schedule_interval=timedelta(seconds=10),  # Adjusted schedule interval to 10 seconds
)

start_task = DummyOperator(task_id='start', dag=dag)

reload_page_task = SimpleHttpOperator(
    task_id='reload_page',
    method='GET',
    http_conn_id='fastapi_conn',  # You need to define a HTTP connection in Airflow with your FastAPI URL
    endpoint='/whats-the-time',
    dag=dag,
)

start_task >> reload_page_task
