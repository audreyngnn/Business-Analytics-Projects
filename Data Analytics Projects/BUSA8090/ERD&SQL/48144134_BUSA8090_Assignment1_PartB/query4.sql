-- Query 4: Task Completion Rate and Customer Satisfaction
SELECT 
    COUNT(*) AS total_tasks,
    SUM(CASE WHEN Task_Status = 'Completed' THEN 1 ELSE 0 END) AS completed_tasks,
    (SUM(CASE WHEN Task_Status = 'Completed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS completion_rate,
    AVG(CASE WHEN Task_Status = 'Completed' THEN tt.Rating ELSE NULL END) AS avg_rating
FROM TASK t
LEFT JOIN TASK_TRANSACTION tt ON t.Task_ID = tt.Task_ID;