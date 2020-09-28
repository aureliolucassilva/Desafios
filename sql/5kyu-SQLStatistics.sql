SELECT MIN(score) AS min,
       PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY score)::FLOAT + 0.5 AS median,
       MAX(score) AS max
FROM result
