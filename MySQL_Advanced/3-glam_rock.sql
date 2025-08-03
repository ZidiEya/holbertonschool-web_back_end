-- Select glam rock bands and calculate their lifespan using formed and split years
SELECT
  band_name,
  IFNULL(split, YEAR(CURDATE())) - formed AS lifespan
FROM
  metal_bands
WHERE
  style = 'Glam rock'
ORDER BY
  lifespan DESC;
