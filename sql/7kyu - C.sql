--Link -> https://www.codewars.com/kata/59401c25c15cbeb58d000028

SELECT id, 
       name, 
       CASE
         WHEN STRPOS(characteristics, ',') > 0 THEN SUBSTRING(characteristics, 0, STRPOS(characteristics, ','))
         WHEN STRPOS(characteristics, ',') = 0 THEN characteristics
       END AS characteristic 
FROM monsters
ORDER BY id
