from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import numpy as np
import pandas as pd
import re
import psycopg2
from sqlalchemy import create_engine

def anime_etl():
    anime_list = pd.read_csv("myanimelist_data.csv")
    anime_list.rename(columns={'MAL_ID': "anime_id", 'Name':'anime_title'}, inplace=True)

    def text_cleaning(text):
        text = re.sub(r'&quot;', '', text)
        text = re.sub(r'.hack//', '', text)
        text = re.sub(r'&#039;', '', text)
        text = re.sub(r'A&#039;s', '', text)
        text = re.sub(r'I&#039;', 'I\'', text)
        text = re.sub(r'&amp;', 'and', text)
        return text

    clean_anime_data = anime_list['anime_title'] = anime_list['anime_title'].apply(text_cleaning)

    anime_data = anime_list[['anime_id', 'anime_title', 'Score', 'Genres', 'Type', 'Episodes', 'Members', 'Premiered']]

    db_host = 'localhost'
    db_port = '5432'
    db_name = 'anime-table2'
    db_user = 'postgres'
    db_password = 'password'

    # Create the SQLAlchemy engine
    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

    # Write the anime_data DataFrame to the PostgreSQL database table
    anime_data.to_sql('anime_table2', engine, if_exists='replace', index=True)

    print("anime_data loaded to the PostgreSQL database successfully.")

default_args = {
    'owner': 'admin',
    'start_date': datetime(2023, 5, 23),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('anime_etl_pipeline', default_args=default_args, description='Pipeline for cleaning anime data')

clean_data_task = PythonOperator(
    task_id='clean_data',
    python_callable=anime_etl,
    dag=dag
)

clean_data_task

