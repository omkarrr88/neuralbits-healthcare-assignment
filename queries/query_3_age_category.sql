SELECT 
    CASE 
        WHEN CAST((julianday('now') - julianday(p.dob)) / 365.25 AS INTEGER) < 13 THEN 'Child (0-12)'
        WHEN CAST((julianday('now') - julianday(p.dob)) / 365.25 AS INTEGER) BETWEEN 13 AND 19 THEN 'Adolescent (13-19)'
        WHEN CAST((julianday('now') - julianday(p.dob)) / 365.25 AS INTEGER) BETWEEN 20 AND 60 THEN 'Adult (20-60)'
        ELSE 'Senior (60+)'
    END as age_category,
    COUNT(*) as patient_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Patient), 2) as percentage
FROM Patient p
GROUP BY age_category
ORDER BY 
    CASE 
        WHEN age_category = 'Child (0-12)' THEN 1
        WHEN age_category = 'Adolescent (13-19)' THEN 2
        WHEN age_category = 'Adult (20-60)' THEN 3
        ELSE 4
    END;