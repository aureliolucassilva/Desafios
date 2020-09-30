--Link -> https://www.codewars.com/kata/5942b066db68b6f35f000084

UPDATE repositories
SET address = REGEXP_REPLACE(address,'[[:digit:]]','!','g');

SELECT project, commits, contributors, address FROM repositories;
