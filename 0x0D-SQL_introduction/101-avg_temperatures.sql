-- displays the average temprature by city ordered by temperature descending
SELECT temperatures.city, AVG(temperatures.value)
AS avg_temp FROM temperatures
GROUP BY temperatures.city ORDER BY avg_temp DESC;
