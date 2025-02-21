CREATE TABLE IF NOT EXISTS departments (
    id SERIAL PRIMARY KEY,
    department VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS jobs (
    id SERIAL PRIMARY KEY,
    job VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS hired_employees (
    id SERIAL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "datetime" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    department_id INTEGER NOT NULL,
    job_id INTEGER NOT NULL,
    CONSTRAINT fk_department FOREIGN KEY (department_id) REFERENCES departments(id) ON DELETE CASCADE,
    CONSTRAINT fk_job FOREIGN KEY (job_id) REFERENCES jobs(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS rejected_records (
    id SERIAL PRIMARY KEY,
    table_name VARCHAR(50) NOT NULL,
    raw_data TEXT NOT NULL,
    error_message TEXT NOT NULL,
    rejected_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);


-- TODO ¿INDICES?