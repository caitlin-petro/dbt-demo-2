SELECT id 
    , FIRST_NAME
    , LAST_NAME
    , birthdate
FROM {{ ref('customers') }}