--Link -> https://www.codewars.com/kata/5809575e166583acfa000083

SELECT ROW_NUMBER() OVER (ORDER BY SUM(points) DESC) AS rank,
       CASE
         WHEN clan != '' THEN clan
         WHEN clan = '' THEN '[no clan specified]'
       END AS clan,
       SUM(points) AS total_points,
       COUNT(people) AS total_people
FROM people
GROUP BY clan
ORDER BY total_points DESC
