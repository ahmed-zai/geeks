CREATE TABLE actors (
    actor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    age DATE NOT NULL,
    number_oscars SMALLINT NOT NULL
);

INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES
('Leonardo', 'DiCaprio', '1974-11-11', 1),
('Meryl', 'Streep', '1949-06-22', 3),
('Denzel', 'Washington', '1954-12-28', 2),
('Natalie', 'Portman', '1981-06-09', 1),
('Tom', 'Hanks', '1956-07-09', 2);

SELECT * FROM actors;

SELECT COUNT(*) FROM actors;

INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES
('', 'bond', '1949-06-22', 2);
