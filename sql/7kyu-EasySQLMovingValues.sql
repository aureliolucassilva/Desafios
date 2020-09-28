SELECT LENGTH(name) AS id,
       LENGTH(CAST(legs AS TEXT)) AS name,
       LENGTH(CAST(arms AS TEXT)) AS legs,
       LENGTH(characteristics) AS arms,
       LENGTH(CAST(id AS TEXT)) AS characteristics
FROM monsters
