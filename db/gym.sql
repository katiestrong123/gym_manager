DROP TABLE IF EXISTS exercise_classes;
DROP TABLE IF EXISTS trainers;

CREATE TABLE trainers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255),
    specialism VARCHAR(255)
);

CREATE TABLE exercise_classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    duration INT,
    trainer_id INT REFERENCES trainers(id)
);
