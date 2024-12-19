-- Query 5: Tradesperson Performance and Quality Control
SELECT 
    tp.Tradesperson_ID,
    COUNT(DISTINCT t.Task_ID) AS total_tasks,
    AVG(tt.Rating) AS avg_rating,
    COUNT(DISTINCT c.Certification_ID) AS certifications_count
FROM TRADESPERSON tp
LEFT JOIN TASK t ON tp.Tradesperson_ID = t.Tradesperson_ID
LEFT JOIN TASK_TRANSACTION tt ON t.Task_ID = tt.Task_ID
LEFT JOIN CERTIFICATION c ON tp.Tradesperson_ID = c.Tradesperson_ID
GROUP BY tp.Tradesperson_ID
ORDER BY 
    CASE WHEN AVG(tt.Rating) IS NULL THEN 1 ELSE 0 END, 
    avg_rating DESC, 
    total_tasks DESC;