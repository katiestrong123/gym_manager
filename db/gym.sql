DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS trainers;

CREATE TABLE trainers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone INT,
    specialism VARCHAR(255)
);

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    duration INT,
    trainer_id INT REFERENCES trainers(id)
);
