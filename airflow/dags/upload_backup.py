from airflow import DAG
from airflow.decorators import dag, task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime

# Configuración
BACKUP_DIR = "/opt/airflow/backups"
CONN_ID = "globant_api_db"  # Conexión a la base de datos

@dag(schedule_interval=None, start_date=datetime(2024, 3, 1), catchup=False, tags=["load_backup"])
def load_backup():
    """DAG para cargar un backup específico en la base de datos."""

    @task
    def get_latest_backup(**kwargs):
        import os
        """Obtiene el archivo de backup más reciente basado en el parámetro 'table_name'."""
        conf = kwargs.get("dag_run").conf or {}
        table_name = conf.get("table_name")

        if not table_name:
            raise ValueError("Debe proporcionar el parámetro 'table_name' en conf.")

        table_files = [f for f in os.listdir(BACKUP_DIR) if f.startswith(f"{table_name}_") and f.endswith(".avro")]
        if not table_files:
            raise FileNotFoundError(f"No se encontraron backups para la tabla {table_name}")

        latest_file = max(table_files, key=lambda f: os.path.getmtime(os.path.join(BACKUP_DIR, f)))
        return {"file_path": os.path.join(BACKUP_DIR, latest_file), "table_name": table_name}

    @task.virtualenv(
        system_site_packages=True,
        requirements=["fastavro==1.10.0"]
        )
    def load_backup_to_db(context,CONN_ID):
        import os
        import fastavro
        from airflow.providers.postgres.hooks.postgres import PostgresHook
        """Carga los datos del archivo AVRO en la base de datos PostgreSQL."""
        file_path = context["file_path"]
        table_name = context["table_name"]

        pg_hook = PostgresHook(postgres_conn_id=CONN_ID)
        conn = pg_hook.get_conn()
        cursor = conn.cursor()

        with open(file_path, "rb") as avro_file:
            reader = fastavro.reader(avro_file)
            records = [record for record in reader]

        if not records:
            print(f"No hay datos en el archivo de backup {file_path}.")
            return

        # Obtener columnas desde el primer registro
        columns = records[0].keys()
        columns_str = ", ".join(columns)
        placeholders = ", ".join(["%s"] * len(columns))

        insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders}) ON CONFLICT DO NOTHING;"

        for record in records:
            values = tuple(record[col] for col in columns)
            cursor.execute(insert_query, values)

        conn.commit()
        cursor.close()
        conn.close()

        print(f"Backup {file_path} cargado en la tabla {table_name}.")

    # Flujo de tareas
    backup_info = get_latest_backup()
    load_backup_to_db(backup_info,CONN_ID)

load_backup_dag = load_backup()
