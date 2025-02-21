-- Departamets 

CREATE TEMP TABLE temp_departments (
    id INTEGER,
    department VARCHAR(255)
);

COPY temp_departments(id, department)
FROM '/docker-entrypoint-initdb.d/departments.csv'
WITH (FORMAT csv, HEADER false, DELIMITER ',');

INSERT INTO departments(id, department)
SELECT id, department
FROM temp_departments
WHERE id IS NOT NULL AND department IS NOT NULL;

INSERT INTO rejected_records (table_name, raw_data, error_message)
SELECT 
    'departments', 
    json_build_object('id', id, 'department', department)::JSONB, 
    'Null values found'
FROM temp_departments
WHERE id IS NULL OR department IS NULL;

DROP TABLE temp_departments;

--Jobs
CREATE TEMP TABLE temp_jobs (
    id INTEGER,
    job VARCHAR(255)
);

COPY temp_jobs(id, job)
FROM '/docker-entrypoint-initdb.d/jobs.csv'
WITH (FORMAT csv, HEADER false, DELIMITER ',');

INSERT INTO jobs(id, job)
SELECT id, job
FROM temp_jobs
WHERE id IS NOT NULL AND job IS NOT NULL;

INSERT INTO rejected_records (table_name, raw_data, error_message)
SELECT 
    'jobs', 
    json_build_object('id', id, 'job', job)::JSONB, 
    'Null values found'
FROM temp_jobs
WHERE id IS NULL OR job IS NULL;

DROP TABLE temp_jobs;

-- Cargar datos en hired_employees con validación
CREATE TEMP TABLE temp_hired_employees (
    id INTEGER,
    name VARCHAR(255),
    datetime TIMESTAMPTZ,
    department_id INTEGER,
    job_id INTEGER
);

COPY temp_hired_employees(id, name, datetime, department_id, job_id)
FROM '/docker-entrypoint-initdb.d/hired_employees.csv'
WITH (FORMAT csv, HEADER false, DELIMITER ',');

INSERT INTO hired_employees(id, name, datetime, department_id, job_id)
SELECT id, name, datetime, department_id, job_id
FROM temp_hired_employees
WHERE id IS NOT NULL
  AND name IS NOT NULL
  AND datetime IS NOT NULL
  AND department_id IS NOT NULL
  AND job_id IS NOT NULL;

INSERT INTO rejected_records (table_name, raw_data, error_message)
SELECT 
    'hired_employees', 
    json_build_object('id', id, 'name', name, 'datetime', datetime, 'department_id', department_id, 'job_id', job_id)::JSONB, 
    'Null values found'
FROM temp_hired_employees
WHERE id IS NULL OR name IS NULL OR datetime IS NULL OR department_id IS NULL OR job_id IS NULL;

DROP TABLE temp_hired_employees;