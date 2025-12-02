SELECT 
    t.medicine_name,
    COUNT(*) as times_prescribed,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Treatment), 2) as percentage_of_all,
    COUNT(DISTINCT t.patient_id) as unique_patients
FROM Treatment t
GROUP BY t.medicine_name
ORDER BY times_prescribed DESC
LIMIT 10;