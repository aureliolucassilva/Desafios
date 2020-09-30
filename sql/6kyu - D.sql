--Link -> https://www.codewars.com/kata/580d08b5c049aef8f900007c

SELECT payment.customer_id,
       email,
       COUNT(payment_id) AS payments_count,
       SUM(amount)::FLOAT AS total_amount
FROM payment
INNER JOIN customer ON payment.customer_id = customer.customer_id
GROUP BY payment.customer_id, email
ORDER BY total_amount DESC
LIMIT 10
