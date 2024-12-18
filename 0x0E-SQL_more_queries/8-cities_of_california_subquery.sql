-- lists all the cities of California that can be 
-- found in hbtn_0d_usa database
SELECT id, name
FROM cities
WHERE state_id = 
(SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id;
