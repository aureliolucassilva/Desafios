--Link -> https://www.codewars.com/kata/5943a58f95d5f72cb900006a

SELECT SUBSTRING(project, 1, commits) AS project, 
       REVERSE(SUBSTRING(REVERSE(address), 1, contributors)) AS address 
FROM repositories
