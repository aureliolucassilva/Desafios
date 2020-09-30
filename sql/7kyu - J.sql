--Link -> https://www.codewars.com/kata/5ab828bcedbcfc65ea000099

SELECT pokemon_name, 
       str * multiplier AS modifiedStrength,
       element 
FROM pokemon 
INNER JOIN multipliers ON pokemon.element_id = multipliers.id
WHERE str * multiplier >= 40
ORDER BY modifiedStrength DESC
