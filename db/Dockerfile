FROM postgres:17.3

# Copiar los archivos SQL al contenedor
COPY init.sql /docker-entrypoint-initdb.d/init.sql
COPY insert_historical_data.sql /docker-entrypoint-initdb.d/insert_historical_data.sql

# Copiar los archivos CSV para la carga de datos
COPY departments.csv /docker-entrypoint-initdb.d/departments.csv
COPY jobs.csv /docker-entrypoint-initdb.d/jobs.csv
COPY hired_employees.csv /docker-entrypoint-initdb.d/hired_employees.csv