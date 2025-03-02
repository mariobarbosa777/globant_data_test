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
        from airflow.providers.postgres.hooks.postgres import PostgresHook

        os.makedirs(backup_dir, exist_ok=True)
        backup_file = os.path.join(backup_dir, f"{table_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.avro")

        try:
            pg_hook = PostgresHook(postgres_conn_id=conn_id)
            conn = pg_hook.get_conn()
            cursor = conn.cursor()

            cursor.execute(f"""
                SELECT column_name, data_type
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE table_name = '{table_name}'
                ORDER BY ordinal_position
            """)
            
            columns_info = cursor.fetchall()

            pg_to_avro = {
                "integer": "int",
                "smallint": "int",
                "bigint": "long",
                "decimal": "float",
                "numeric": "float",
                "real": "float",
                "double precision": "double",
                "boolean": "boolean",
                "character varying": "string",
                "varchar": "string",
                "character": "string",
                "char": "string",
                "text": "string",
                "timestamp without time zone": "string",
                "timestamp with time zone": "string",
                "date": "string",
                "json": "string",
                "jsonb": "string"
            }

            # 🔥 Generar esquema AVRO con tipos correctos
            avro_schema = {
                "type": "record",
                "name": table_name,
                "fields": [
                    {"name": col, "type": ["null", pg_to_avro.get(dtype, "string")]}
                    for col, dtype in columns_info
                ]
            }

            # 🔥 Obtener los datos de la tabla
            cursor.execute(f"SELECT * FROM {table_name}")
            records = cursor.fetchall()

            # Guardar datos en formato AVRO
            with open(backup_file, "wb") as out_file:
                writer(out_file, parse_schema(avro_schema), [dict(zip([col for col, _ in columns_info], row)) for row in records])

            print(f"Backup de {table_name} creado en {backup_file}")

        except Exception as e:
            print(f"Error al procesar {table_name}: {str(e)}")

    # Crear una tarea por cada tabla
    for table in TABLES:
        backup_table.override(task_id=f"backup_{table}")(table, BACKUP_DIR, CONN_ID)

backup_dag = backup_tables()
