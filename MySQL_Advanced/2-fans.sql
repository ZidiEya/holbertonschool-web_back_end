-- Group bands by origin and sum up the number of fans per origin
-- Then order the result by number of fans in descending order

SELECT origin, SUM(nb_fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
