SELECT 
    strftime('%Y', p.admission_datetime) as year,
    ROUND(SUM(CASE WHEN b.payment_mode = 'Cash' THEN b.bill_amount ELSE 0 END), 2) 
        as cash_income,
    ROUND(SUM(CASE WHEN b.payment_mode = 'Credit' THEN b.bill_amount ELSE 0 END), 2) 
        as credit_income,
    ROUND(SUM(b.bill_amount), 2) as total_income,
    ROUND(SUM(CASE WHEN b.payment_mode = 'Cash' THEN b.bill_amount ELSE 0 END) * 100.0 / SUM(b.bill_amount), 2) 
        as cash_percentage,
    COUNT(*) as transaction_count
FROM Billing b
JOIN Patient p ON b.patient_id = p.patient_id
GROUP BY strftime('%Y', p.admission_datetime)
ORDER BY year DESC;

SELECT 
    strftime('%Y-%m', p.admission_datetime) as month,
    ROUND(SUM(CASE WHEN b.payment_mode = 'Cash' THEN b.bill_amount ELSE 0 END), 2) 
        as cash_income,
    ROUND(SUM(CASE WHEN b.payment_mode = 'Credit' THEN b.bill_amount ELSE 0 END), 2) 
        as credit_income,
    ROUND(SUM(b.bill_amount), 2) as total_income,
    ROUND(SUM(CASE WHEN b.payment_mode = 'Cash' THEN b.bill_amount ELSE 0 END) * 100.0 / SUM(b.bill_amount), 2) 
        as cash_percentage
FROM Billing b
JOIN Patient p ON b.patient_id = p.patient_id
GROUP BY strftime('%Y-%m', p.admission_datetime)
ORDER BY month DESC;