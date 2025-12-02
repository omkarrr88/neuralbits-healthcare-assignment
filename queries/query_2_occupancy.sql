SELECT 
    h.hospital_id,
    h.hospital_name,
    ROUND(COUNT(*) * 1.0 / 
          ((julianday(MAX(p.discharge_datetime)) - julianday(MIN(p.admission_datetime))) / 7 + 1), 2) 
    as weekly_occupancy,
    ROUND(COUNT(*) * 1.0 / 
          ((julianday(MAX(p.discharge_datetime)) - julianday(MIN(p.admission_datetime))) / 30 + 1), 2) 
    as monthly_occupancy,
    ROUND(COUNT(*) * 1.0 / 
          ((julianday(MAX(p.discharge_datetime)) - julianday(MIN(p.admission_datetime))) / 365 + 1), 2) 
    as yearly_occupancy
FROM Hospital h
LEFT JOIN Patient p ON h.hospital_id = p.hospital_id
GROUP BY h.hospital_id, h.hospital_name
ORDER BY h.hospital_id;