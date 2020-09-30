--Link -> https://www.codewars.com/kata/58164ddf890632ce00000220

SELECT age, COUNT(age) AS total_people FROM people
GROUP BY age
HAVING COUNT(age) >= 10
