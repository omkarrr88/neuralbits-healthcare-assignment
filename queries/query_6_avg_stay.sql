SELECT 
    h.hospital_id,
    h.hospital_name,
    ROUND(AVG(CAST(julianday(p.discharge_datetime) - julianday(p.admission_datetime) AS REAL)), 2) 
        as average_days,
    CAST(MIN(julianday(p.discharge_datetime) - julianday(p.admission_datetime)) AS INTEGER) 
        as min_days,
    CAST(MAX(julianday(p.discharge_datetime) - julianday(p.admission_datetime)) AS INTEGER) 
        as max_days,
    COUNT(*) as total_patients
FROM Hospital h
LEFT JOIN Patient p ON h.hospital_id = p.hospital_id
GROUP BY h.hospital_id, h.hospital_name;

SELECT 
    CASE 
        WHEN CAST(julianday(p.discharge_datetime) - julianday(p.admission_datetime) AS INTEGER) <= 3 THEN '1-3 Days'
        WHEN CAST(julianday(p.discharge_datetime) - julianday(p.admission_datetime) AS INTEGER) BETWEEN 4 AND 7 THEN '4-7 Days'
        WHEN CAST(julianday(p.discharge_datetime) - julianday(p.admission_datetime) AS INTEGER) BETWEEN 8 AND 14 THEN '8-14 Days'
        ELSE '15+ Days'
    END as los_category,
    COUNT(*) as patient_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Patient), 2) as percentage
FROM Patient p
GROUP BY los_category
ORDER BY 
    CASE 
        WHEN los_category = '1-3 Days' THEN 1
        WHEN los_category = '4-7 Days' THEN 2
        WHEN los_category = '8-14 Days' THEN 3
        ELSE 4
    END;