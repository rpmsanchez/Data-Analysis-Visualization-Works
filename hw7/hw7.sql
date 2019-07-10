use sakila;

select first_name, last_name from actor;

select concat(first_name, " ", last_name) as "Actor Name" from actor;

select actor_id, first_name, last_name 
from actor
where first_name = "Joe"; 

select * from actor
where last_name like "%GEN%";

select * from actor
where last_name like "%LI%"
order by last_name, first_name;

select country_id, country
from country
where country in ("Afghanistan", "Bangladesh", "China");

alter table actor
add description BLOB;
alter table actor
drop description;

select last_name, count(last_name)
from actor
group by last_name
having count(last_name) > 1;

update actor
set first_name = "HARPO"
where first_name = "GROUCHO" AND last_name = "WILLIAMS";
update actor
set first_name = "GROUCHO"
where first_name = "HARPO" AND last_name = "WILLIAMS";

SHOW CREATE TABLE address

select staff.first_name, staff.last_name, address.address, address.address2
from staff
join address on staff.address_id=address.address_id;

SELECT staff.first_name, staff.last_name,
sum(payment.amount)
FROM staff
INNER JOIN payment ON staff.staff_id = payment.staff_id
WHERE payment_date LIKE '%2005-08%'
group by first_name, last_name;

select film.title, count(film_actor.actor_id)
from film
inner join film_actor on film.film_id=film_actor.film_id
group by title;

select film.title, count(inventory.film_id)
from film
inner join inventory on film.film_id=inventory.film_id
where title = "Hunchback Impossible"
group by title;

select customer.first_name, customer.last_name, sum(payment.amount)
from customer
inner join payment on customer.customer_id=payment.customer_id
group by last_name, first_name;

select * from language;

select film.title 
from film
where film.title like "K%"
or film.title like "Q%"
and language_id in
(
select language_id
from language lng
where lng.name = "English"
);

select first_name, last_name
from actor
where actor_id in
(
select actor_id
from film_actor
where film_id in
(
select film_id
from film
where film.title = "Alone Trip"
));

select first_name, last_name, email
from customer
where address_id in
(
select address id
from address 
where city_id in
(
select city_id
from city
where country_id in
(
select country_id
from country
where country = "Canada"
)));

select title
from film
where film_id in
(
select film_id
from film_category
where category_id in
(
select category_id
from category
where name = "Family"
));

select inventory_id
from rental
);








