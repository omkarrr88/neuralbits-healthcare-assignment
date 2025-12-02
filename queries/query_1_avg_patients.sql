SELECT 
    h.hospital_id,
    h.hospital_name,
    ROUND(COUNT(*) * 1.0 / COUNT(DISTINCT strftime('%Y-%m', p.admission_datetime)), 2) as avg_patients_per_month,
    ROUND(COUNT(*) * 1.0 / COUNT(DISTINCT strftime('%Y-W%W', p.admission_datetime)), 2) as avg_patients_per_week,
    ROUND(COUNT(*) * 1.0 / COUNT(DISTINCT strftime('%Y', p.admission_datetime)), 2) as avg_patients_per_year
FROM Hospital h
LEFT JOIN Patient p ON h.hospital_id = p.hospital_id
GROUP BY h.hospital_id, h.hospital_name
ORDER BY h.hospital_id;