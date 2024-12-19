-- Query 3: New User Onboarding Efficiency
SELECT 
    tp.Tradesperson_ID,
    DATEDIFF(MIN(t.Posting_Date), tp.Registration_Date) AS days_to_first_task,
    COUNT(DISTINCT c.Certification_ID) AS certifications_count
FROM TRADESPERSON tp
LEFT JOIN TASK t ON tp.Tradesperson_ID = t.Tradesperson_ID
LEFT JOIN CERTIFICATION c ON tp.Tradesperson_ID = c.Tradesperson_ID
GROUP BY tp.Tradesperson_ID, tp.Registration_Date
ORDER BY days_to_first_task DESC;