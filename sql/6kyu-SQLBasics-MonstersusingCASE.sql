SELECT top_half.id,
       heads,
       arms,
       legs,
       tails,
       CASE
       WHEN heads > arms THEN 'BEAST'
       WHEN tails > legs THEN 'BEAST'
       WHEN tails < legs THEN 'WEIRDO'
       WHEN heads < arms THEN 'WEIRDO'
       END AS species
FROM top_half
INNER JOIN bottom_half ON top_half.id = bottom_half.id
ORDER BY species
