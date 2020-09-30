--Link -> https://www.codewars.com/kata/5802e32dd8c944e562000020

SELECT products.id AS id, 
       products.name AS name, 
       isbn, 
       company_id,
       price,
       companies.name AS company_name
FROM products
INNER JOIN companies ON products.company_id = companies.id
