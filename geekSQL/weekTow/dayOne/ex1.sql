CREATE DATABASE public;

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price NUMERIC(6, 2) NOT NULL
);

INSERT INTO items (name, price)
VALUES 
    ('Small Desk', 100),
    ('Large Desk', 300),
    ('Fan', 80);

SELECT * FROM items;

SELECT * FROM items
WHERE price > 80;

SELECT * FROM items
WHERE price <= 300;

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

INSERT INTO customers (name, last_name)
VALUES 
    ('Greg', 'Jones'),
    ('Sandra', 'Jones'),
    ('Scott', 'Scott'),
    ('Trevor', 'Green'),
    ('Melanie', 'Johnson');

SELECT * FROM customers
WHERE last_name = 'Smith';

SELECT * FROM customers
WHERE last_name = 'Jones';

SELECT * FROM customers
WHERE name <> 'Scott';
