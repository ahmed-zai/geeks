SELECT * FROM items
ORDER BY price ASC;

SELECT * FROM items
WHERE price >= 80
ORDER BY price DESC;

SELECT name, last_name, id
FROM customers
ORDER BY first_name ASC
LIMIT 3;

SELECT name 
FROM customers
ORDER BY last_name DESC;
