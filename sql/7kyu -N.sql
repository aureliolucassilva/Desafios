--Link -> https://www.codewars.com/kata/5ad90fb688a0b74111000055

SELECT INITCAP(CONCAT(firstname, ' ', lastname)) AS shortlist FROM Elves 
WHERE firstname LIKE '%tegil%'
OR lastname LIKE '%astar%'
