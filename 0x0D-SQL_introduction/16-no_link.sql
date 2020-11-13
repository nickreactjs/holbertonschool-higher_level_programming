-- List score and name in descending order. Only if rows have a name value.
SELECT score, name FROM second_table
WHERE name IS NOT NULL ORDER BY score DESC;
