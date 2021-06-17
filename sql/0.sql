CREATE TABLE IF NOT EXISTS user (
    _id INTEGER PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ip TEXT NOT NULL UNIQUE,
    country TEXT,
    countryCode TEXT,
    region TEXT,
    regionName TEXT,
    city TEXT,
    zip TEXT,
    lat REAL,
    lon REAL,
    timezone TEXT,
    isp TEXT,
    org TEXT,
    _as TEXT
);