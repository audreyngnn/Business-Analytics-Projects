-- Query 7: Certification Impact on Task Assignment
SELECT 
    c.Course_ID,
    co.Course_Name,
    COUNT(DISTINCT t.Task_ID) AS assigned_tasks,
    AVG(b.Bid_Amount) AS avg_bid_amount
FROM CERTIFICATION c
JOIN COURSE co ON c.Course_ID = co.Course_ID
JOIN TRADESPERSON tp ON c.Tradesperson_ID = tp.Tradesperson_ID
LEFT JOIN TASK t ON tp.Tradesperson_ID = t.Tradesperson_ID
LEFT JOIN BID b ON t.Task_ID = b.Task_ID AND b.Tradesperson_ID = tp.Tradesperson_ID
GROUP BY c.Course_ID, co.Course_Name
ORDER BY assigned_tasks DESC;