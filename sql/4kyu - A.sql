-- Link -> https://www.codewars.com/kata/589e0837e10c4a1018000028

SELECT date,
       num_posts AS count,
       CASE WHEN CONCAT(TO_CHAR(percent_growth, '99D9'), '%') = '%' THEN NULL
            ELSE REPLACE(CONCAT(TO_CHAR(percent_growth, '99D9'), '%'), ' ', '')
       END AS percent_growth
FROM
(
  SELECT date, 
         num_posts,
         100 * ((num_posts::DOUBLE PRECISION - previous_row::DOUBLE PRECISION)/ previous_row::DOUBLE PRECISION) AS percent_growth
  FROM
  (
    SELECT date, 
           num_posts, 
           LAG(num_posts, 1) OVER(ORDER BY date) AS previous_row
    FROM
    (
      SELECT DATE_TRUNC('month', created_at)::DATE AS date,
             COUNT(posts) AS num_posts
      FROM posts
      GROUP BY DATE_TRUNC('month', created_at)::DATE
    ) AS T1
    ORDER BY date ASC
  ) AS T2
) AS T3
