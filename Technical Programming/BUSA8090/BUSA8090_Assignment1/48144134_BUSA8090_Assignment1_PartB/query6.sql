-- Query 6: Supply Chain Efficiency
SELECT 
    s.Supplier_ID,
    s.SupplierName,
    COUNT(o.Order_ID) AS total_orders,
    AVG(DATEDIFF(mt.Transaction_Date, o.Order_Date)) AS avg_fulfillment_time_indays,
    SUM(o.Total_Value) AS total_order_value
FROM SUPPLIER s
JOIN `ORDER` o ON s.Supplier_ID = o.Supplier_ID
JOIN MATERIAL_TRANSACTION mt ON o.Order_ID = mt.Order_ID
GROUP BY s.Supplier_ID, s.SupplierName
ORDER BY avg_fulfillment_time_indays;