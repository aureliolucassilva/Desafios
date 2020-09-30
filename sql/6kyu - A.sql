--Link -> https://www.codewars.com/kata/58112f8004adbbdb500004fe

SELECT 'US' AS location, * FROM ussales
WHERE price > 50.00
UNION ALL
SELECT 'EU' AS location, * FROM eusales
WHERE price > 50.00
