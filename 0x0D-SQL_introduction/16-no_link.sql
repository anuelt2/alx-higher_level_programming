-- lists all records of table ``second_table`` of database
-- ``hbtn_0c_0`` in MySQL server
SELECT score, name FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;
