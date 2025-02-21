DO $$ 
BEGIN
    IF NOT EXISTS (SELECT 1 FROM departments) THEN
        COPY departments(id, department)
        FROM '/docker-entrypoint-initdb.d/departments.csv'
        WITH (FORMAT csv, HEADER false, DELIMITER ',');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM jobs) THEN
        COPY jobs(id, job)
        FROM '/docker-entrypoint-initdb.d/jobs.csv'
        WITH (FORMAT csv, HEADER false, DELIMITER ',');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM hired_employees) THEN
        COPY hired_employees(id, name, datetime, department_id, job_id)
        FROM '/docker-entrypoint-initdb.d/hired_employees.csv'
        WITH (FORMAT csv, HEADER false, DELIMITER ',');
    END IF;
END $$;