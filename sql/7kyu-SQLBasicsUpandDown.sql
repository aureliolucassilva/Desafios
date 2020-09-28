SELECT 
CASE 
WHEN MOD(SUM(number1), 2) != 0 THEN MIN(number1) 
WHEN MOD(SUM(number1), 2) = 0 THEN MAX(number1)
END AS number1,
CASE
WHEN MOD(SUM(number2), 2) != 0 THEN MIN(number2) 
WHEN MOD(SUM(number2), 2) = 0 THEN MAX(number2)
END AS number2
FROM numbers
