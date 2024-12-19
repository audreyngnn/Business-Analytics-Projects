-- Query 2: Geographic Distribution of Users
SELECT 
    State, 
    COUNT(*) AS user_count,
    'Tradesperson' AS user_type
FROM TRADESPERSON
GROUP BY State
UNION ALL
SELECT 
    State, 
    COUNT(*) AS user_count,
    'Customer' AS user_type
FROM CUSTOMER
GROUP BY State
ORDER BY State, user_type;