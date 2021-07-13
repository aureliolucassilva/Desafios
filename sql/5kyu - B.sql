-- Link -> https://www.codewars.com/kata/589cf45835f99b2909000115

SELECT date,
       count,
       SUM(COUNT) OVER(ORDER BY date)::INT AS total
FROM
(
  SELECT DATE(created_at) AS date,
         COUNT(*) AS count
  FROM posts
  GROUP BY DATE(created_at)
  ORDER BY DATE(created_at)
) AS T1
