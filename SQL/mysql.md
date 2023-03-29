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
SELECT  distinct Building
FROM Employees
  Left JOIN Buildings
    ON Employees.Building = Buildings.Building_name;
#Find the list of all buildings and their capacity
SELECT * FROM buildings;
#answer

#List all buildings and the distinct employee roles in each building (including empty buildings) 
SELECT  distinct building_name,role,building
FROM Employees
  Left JOIN Buildings
    ON Employees.Building = Buildings.Building_name;
#answer
SELECT DISTINCT building_name, role 
FROM buildings 
  LEFT JOIN employees
    ON building_name = building;

```

Lesson 8
```sql
#Find the name and role of all employees who have not been assigned to a building 
SELECT Name,role FROM employees
where 	Building is null
;

#Find the names of the buildings that hold no employees
SELECT Building_name
FROM buildings 
  LEFT JOIN employees
    ON building_name = building
where Name is null
;
```

Lesson 9
```sql
#List all movies and their combined sales in millions of dollars 
#answer
SELECT title, (domestic_sales + international_sales) / 1000000 AS gross_sales_millions
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id;
#List all movies and their ratings in percent
#answer
SELECT title, rating * 10 AS rating_percent
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id;
#List all movies that were released on even number years
#answer
SELECT title, year
FROM movies
WHERE year % 2 = 0;

```

Lesson 10
```sql
#Find the longest time that an employee has been at the studio 
SELECT name,Max(Years_employed) FROM employees

#For each role, find the average number of years employed by employees in that role
#answer
SELECT role, AVG(years_employed) as Average_years_employed
FROM employees
GROUP BY role;
#Find the total number of employee years worked in each building 
SELECT building, Sum(years_employed) as Sum_years_employed
FROM employees
GROUP BY building;
```

Lesson 11
```sql
#Find the number of Artists in the studio (without a HAVING clause) 
SELECT count(Role) as Artists_Num FROM employees
where Role = "Artist"
#Find the number of Employees of each role in the studio
SELECT distinct role,count(Role) as Artists_Num FROM employees
Group by role
#Find the total number of years employed by all Engineers 
#answer
SELECT role, SUM(years_employed)
FROM employees
GROUP BY role
HAVING role = "Engineer";
```

Lesson 12
```sql
#Find the number of movies each director has directed
SELECT director,count(title) FROM movies
group by director

#Find the total domestic and international sales that can be attributed to each director
#answer
SELECT director, SUM(domestic_sales + international_sales) as Cumulative_sales_from_all_movies
FROM movies
    INNER JOIN boxoffice
        ON movies.id = boxoffice.movie_id
GROUP BY director;


```

Exercise 13 — Tasks
```sql
#Add the studio's new production, Toy Story 4 to the list of movies (you can use any director)

#Toy Story 4 has been released to critical acclaim! It had a rating of 8.7, and made 340 million domestically and 270 million internationally. Add the record to the BoxOffice table.

INSERT INTO boxoffice VALUES (4, 8.7, 340000000, 270000000);

```
Exercise 13 — Tasks
```sql
#The director for A Bug's Life is incorrect, it was actually directed by John Lasseter
UPDATE Movies
SET director = "John Lasseter" 
where title = "A Bug's Life"

#The year that Toy Story 2 was released is incorrect, it was actually released in 1999
UPDATE Movies
SET Year = "1999" 
where title = "Toy Story 2"

#Both the title and director for Toy Story 8 is incorrect! The title should be "Toy Story 3" and it was directed by Lee Unkrich

UPDATE Movies
SET director = "Lee Unkrich", title = "Toy Story 3"
where title = "Toy Story 8"

```
Exercise 16 — Tasks
```sql
#This database is getting too big, lets remove all movies that were released before 2005.
delete from movies
where year < 2005
#Andrew Stanton has also left the studio, so please remove all movies directed by him.
delete from movies
where director = "Andrew Stanton"
```

Exercise 16 — Tasks
```sql
-- Create a new table named Database with the following columns:
-- – Name A string (text) describing the name of the database
-- – Version A number (floating point) of the latest version of this database
-- – Download_count An integer count of the number of times this database was downloaded
-- This table has no constraints.
#answer
CREATE TABLE Database (
    Name TEXT,
    Version FLOAT,
    Download_count INTEGER
);
```
```sql
-- Exercise 17 — Tasks
-- Add a column named Aspect_ratio with a FLOAT data type to store the aspect-ratio each movie was released in.
#answer
ALTER TABLE Movies
  ADD COLUMN Aspect_ratio FLOAT DEFAULT 2.39;
-- Add another column named Language with a TEXT data type to store the language that the movie was released in. Ensure that the default for this language is English.
ALTER TABLE Movies
  ADD COLUMN Language TEXT DEFAULT "English";

-- Exercise 18 — Tasks
-- We've sadly reached the end of our lessons, lets clean up by removing the Movies table
DROP TABLE IF EXISTS Movies;

-- And drop the BoxOffice table as well
DROP TABLE IF EXISTS BoxOffice;
