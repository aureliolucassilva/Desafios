--Link -> https://www.codewars.com/kata/594a389387a7c6a77a000005

SELECT LENGTH(name) AS id,
       LENGTH(CAST(legs AS TEXT)) AS name,
       LENGTH(CAST(arms AS TEXT)) AS legs,
       LENGTH(characteristics) AS arms,
       LENGTH(CAST(id AS TEXT)) AS characteristics
FROM monsters
