CREATE TABLE IF NOT EXISTS visitors (
    id SERIAL PRIMARY KEY,
    ip VARCHAR(255) NOT NULL,
    timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
