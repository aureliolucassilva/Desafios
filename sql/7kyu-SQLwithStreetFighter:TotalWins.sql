SELECT name, SUM(won) AS won, SUM(lost) AS lost FROM fighters
WHERE move_id BETWEEN 4 AND 10
GROUP BY name
ORDER BY won DESC
LIMIT 6
