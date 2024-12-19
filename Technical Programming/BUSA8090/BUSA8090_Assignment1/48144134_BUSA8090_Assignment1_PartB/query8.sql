-- Query 8: User Specialization Trends
SELECT 
    co.Field,
    COUNT(DISTINCT c.Tradesperson_ID) AS tradesperson_count,
    AVG(b.Bid_Amount) AS avg_bid_amount
FROM COURSE co
JOIN CERTIFICATION c ON co.Course_ID = c.Course_ID
JOIN TASK t ON c.Tradesperson_ID = t.Tradesperson_ID
JOIN BID b ON t.Task_ID = b.Task_ID AND b.Tradesperson_ID = c.Tradesperson_ID
GROUP BY co.Field
ORDER BY tradesperson_count DESC;