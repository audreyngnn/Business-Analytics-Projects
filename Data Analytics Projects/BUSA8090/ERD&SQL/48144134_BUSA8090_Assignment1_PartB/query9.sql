-- Query 9: Platform Growth
SELECT 
    YEAR(t.Posting_Date) AS year,
    MONTH(t.Posting_Date) AS month,
    COUNT(DISTINCT t.Task_ID) AS total_tasks,
    SUM(b.Bid_Amount) AS total_bid_value,
    SUM(CASE WHEN tt.Payment_Status = 'Completed' THEN b.Bid_Amount ELSE 0 END) AS completed_transaction_value
FROM TASK t
LEFT JOIN BID b ON t.Task_ID = b.Task_ID AND b.Bid_Status = 'Accepted'
LEFT JOIN TASK_TRANSACTION tt ON t.Task_ID = tt.Task_ID
GROUP BY YEAR(t.Posting_Date), MONTH(t.Posting_Date)
ORDER BY year, month;