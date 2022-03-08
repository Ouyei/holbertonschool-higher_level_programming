-- Inserts a new row in the table `first_table`
-- in database `hbtn_0c_0` in MySQL Server.

SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city ORDER BY avg_temp DESC;
