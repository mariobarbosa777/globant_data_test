from airflow import DAG
from airflow.decorators import dag, task
from datetime import datetime


# Configuración
BACKUP_DIR = "/opt/airflow/backups"
TABLES = ["departments", "jobs", "hired_employees"]
CONN_ID = "globant_api_db"


@dag(
    schedule_interval="@daily",
    start_date=datetime(2024, 3, 1), 
    catchup=False, 
    tags=["backup"],
    max_active_runs=1,
    max_active_tasks=1
)
def backup_tables():
    """DAG para hacer backup de cada tabla en formato AVRO."""



    @task.virtualenv(
        system_site_packages=True,
        requirements=["fastavro==1.10.0"]
        )
    def backup_table(table_name, backup_dir, conn_id):
        """Extrae datos usando PostgresHook y guarda en AVRO."""
        import os
        from airflow.decorators import dag, task
        from datetime import datetime
        from fastavro import writer, parse_schema

        os.makedirs(backup_dir, exist_ok=True)
        backup_file = os.path.join(conn_id, f"{table_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.avro")

        pg_hook = PostgresHook(postgres_conn_id=conn_id)
        records = pg_hook.get_records(f"SELECT * FROM {table_name}")

        if not records:
            print(f"La tabla {table_name} está vacía. No se creó backup.")
            return

        # Obtener nombres de columnas
        columns = [desc[0] for desc in pg_hook.get_conn().cursor().description]

        # Crear esquema AVRO
        avro_schema = {
            "type": "record",
            "name": table_name,
            "fields": [{"name": col, "type": ["null", "string"]} for col in columns]
        }

        # Guardar datos en formato AVRO
        with open(backup_file, "wb") as out_file:
            writer(out_file, parse_schema(avro_schema), [dict(zip(columns, row)) for row in records])

        print(f"Backup de {table_name} creado en {backup_file}")

    # Crear una tarea por cada tabla
    for table in TABLES:
        backup_table.override(task_id=f"backup_{table}")(table, BACKUP_DIR, CONN_ID)

backup_dag = backup_tables()
