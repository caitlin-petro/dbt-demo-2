SELECT
  BOOKING_DATES,
  SUM(count_bookings) as count_bookings
FROM {{ ref('hotel_count_by_day') }}
GROUP BY
  BOOKING_DATES