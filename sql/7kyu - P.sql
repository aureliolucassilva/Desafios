--Link -> https://www.codewars.com/kata/5ac698cdd325ad18a3000170

SELECT name, SUM(won) AS won, SUM(lost) AS lost FROM fighters
WHERE move_id BETWEEN 4 AND 10
GROUP BY name
ORDER BY won DESC
LIMIT 6
