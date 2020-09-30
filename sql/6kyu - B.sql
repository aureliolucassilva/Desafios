--Link -> https://www.codewars.com/kata/58094559c47d323ebd000035

SELECT people.id,
       name, 
       COUNT(people_id) AS sale_count,
       ROW_NUMBER() OVER(ORDER BY COUNT(people_id) ASC) AS sale_rank
FROM people
INNER JOIN sales ON people.id = sales.people_id 
GROUP BY people.id
ORDER BY sale_count
