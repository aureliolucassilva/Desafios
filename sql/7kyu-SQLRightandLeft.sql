SELECT SUBSTRING(project, 1, commits) AS project, 
       REVERSE(SUBSTRING(REVERSE(address), 1, contributors)) AS address 
FROM repositories
