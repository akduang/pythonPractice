练习网站 https://sqlbolt.com/

```sql
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
```

Lesson 5
```sql
#List all the Canadian cities and their populations
SELECT 	City,Population FROM north_american_cities
where Country = "Canada"
;
#Order all the cities in the United States by their latitude from north to south
SELECT 	City FROM north_american_cities
where Country like "%United States%"
Order by latitude Desc
#List all the cities west of Chicago, ordered from west to east
SELECT * FROM north_american_cities
where Longitude < -87.629798
order by Longitude Asc
;
#List the two largest cities in Mexico (by population)
SELECT * FROM north_american_cities
where Country = "Mexico"
Order by Population Desc
limit 2
;
#List the third and fourth largest cities (by population) in the United States and their population
SELECT * FROM north_american_cities
where Country = "United States"
Order by Population Desc
limit 2 offset 2
```

Lesson 6
```sql
#Find the domestic and international sales for each movie
-- SELECT *column, another_table_column, …*
-- -- FROM mytable
-- -- INNER JOIN another_table 
-- --     ON mytable.id = another_table.id
-- -- WHERE condition(s)
-- -- ORDER BY column, … ASC/DESC
-- -- LIMIT num_limit OFFSET num_offset;
SELECT * FROM movies
INNER JOIN Boxoffice 
    ON movies.id = Boxoffice.Movie_id;
#Show the sales numbers for each movie that did better internationally rather than domestically
SELECT * FROM movies
INNER JOIN Boxoffice 
    ON movies.id = Boxoffice.Movie_id
where Domestic_sales < International_sales
#List all the movies by their ratings in descending order
SELECT * FROM movies
INNER JOIN Boxoffice 
    ON movies.id = Boxoffice.Movie_id
Order by Rating desc
#answer
SELECT title, rating
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id
ORDER BY rating DESC;
```

Lesson 7

```sql
#Find the list of all buildings that have employees

```