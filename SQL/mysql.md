练习网站 https://sqlbolt.com/

SELECT Title FROM movies;
SELECT Director FROM movies;
SELECT Title,director FROM movies;
SELECT Title,year FROM movies;
SELECT * FROM movies;

SELECT *
FROM movies
where Id=6
;
SELECT *
FROM movies
where Year Between 2000 and 2010
;
SELECT *
FROM movies
where Year Not Between 2000 and 2010
;

SELECT year,title
FROM movies
where Id between 1 and 5

SELECT * FROM movies
where title Like "%Toy story%"
;

SELECT * FROM movies
where director = "John Lasseter"
;

SELECT * FROM movies
where director Not like "John Lasseter"
;

SELECT * FROM movies
where title like "%WALL-%"
;

SELECT distinct director FROM movies
;

SELECT * FROM movies
order by year Desc
Limit 4 
;

SELECT * FROM movies
order by Title asc
Limit 5 

SELECT * FROM movies
order by Title asc
Limit 5 offset 5  
;