SELECT * FROM customer;

select first_name || ' ' || last_name as full_name from customer;

select distinct create_date from customer;

select * from customer
order by first_name desc;

select * from film 
order by rental_rate asc;

select address, phone from address
where district ILIKE 'Texas%';

select address, phone from address
where district = 'Texas';

select * from film
where film_id = 15 or film_id = 150;

select * from film
where film_id in(15,150);

select  film_id, title, description, length ,rental_rate from film
where title = 'your favorite movie';

select  film_id, title, description, length ,rental_rate from film
where title ilike 'In%';

select * from film 
order by rental_rate asc
limit 10;

WITH ranked_films AS (
  SELECT *, ROW_NUMBER() OVER (ORDER BY rental_rate ASC) AS rn
  FROM film
)
SELECT * FROM ranked_films
WHERE rn > 10 AND rn <= 20;

SELECT c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY c.customer_id;

SELECT *
FROM film
WHERE film_id NOT IN (SELECT DISTINCT film_id FROM inventory);

SELECT ci.city, co.country
FROM city ci
JOIN country co ON ci.country_id = co.country_id;

SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, p.staff_id
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY p.staff_id, c.customer_id;
