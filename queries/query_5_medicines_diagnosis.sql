WITH RankedMedicines AS (
    SELECT 
        d.diagnosis_name,
        t.medicine_name,
        COUNT(*) as prescription_count,
        ROW_NUMBER() OVER (PARTITION BY d.diagnosis_name ORDER BY COUNT(*) DESC) as rank
    FROM Treatment t
    INNER JOIN Patient p ON t.patient_id = p.patient_id
    INNER JOIN Diagnosis d ON p.patient_id = d.patient_id
    GROUP BY d.diagnosis_name, t.medicine_name
)
SELECT 
    diagnosis_name,
    medicine_name,
    prescription_count,
    rank
FROM RankedMedicines
WHERE rank <= 3
ORDER BY diagnosis_name, rank;