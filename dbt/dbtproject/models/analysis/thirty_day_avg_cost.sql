SELECT
  BOOKING_DATE,
  HOTEL,
  AVG(COST) as AVG_COST
FROM {{ ref('prepped_data') }}
GROUP BY 1, 2